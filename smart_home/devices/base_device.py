import json
import time
from datetime import datetime
from collections import OrderedDict

from smart_home.consumer import Consumer
from smart_home.producer import Producer


class BaseDevice:
    """Базовый класс умного устройства с базовым набором функций"""

    def __init__(self, kafka_params: dict = None, dev_id: int = None, dev_name: str = None, dev_params: dict = None):
        """ инициализация устройства

        kafka_params:dict:
            должен содержать обязательные параметры topic и bootstrap_servers (ip:port)

        dev_params:dict:
            может содержать параметры: period, room, floor

        параметры dev_id и dev_name должны быть уникальными
        """
        self.kafka_params = kafka_params
        self.dev_id = dev_id
        self.dev_name = dev_name
        self.dev_params = dev_params
        self.status = "stop"  # work/stop
        self.device_type = "smart_device_base"

        if self.dev_id == 0:
            raise Exception("'dev_id' cannot be equal 0")

    @staticmethod
    def error_callback():
        print("Error while sending data to kafka")

    def start_read(self):
        """запуск устройства для чтения данных"""
        cons = Consumer(kafka_topic=self.kafka_params['topic'],
                             kafka_servers=self.kafka_params['bootstrap_servers'])
        for msg in cons:
            msg_dict = json.loads(msg.value.decode('utf-8'))
            if msg_dict.get('dev', None) is not None:
                if msg_dict['dev'].get('id', None) == self.dev_id:
                    self._set_data(msg_dict['data'])

    def _set_data(self, msg_dict):
        if msg_dict.get('cmd', None) in ['stop', 'off']:
            self.status = "stop"
        elif msg_dict.get('cmd', None) in ['start', 'on']:
            self.status = "work"

    def start_generate(self):
        """ запуск устройства для генерации данных.
        Возможные состояния/статусы устройства:
            - work   -- работает
            - stop   -- ожидает
        """
        t0 = time.time()
        self.status = "work"
        prod = Producer()
        while True:
            if self.status == "stop":
                time.sleep(5)
            elif self.status == "work":
                if t0 + self.dev_params['period'] < time.time():
                    self.send_data(prod)
                    t0 = time.time()

    def send_data(self, producer):
        """ подготовить и отправить данные в kafka """
        data = self._generate_data()
        msg = self.generate_msg(data)
        self._kafka_send(json.dumps(msg), producer)

    def _generate_data(self):
        """ сгенерировать данные устройства """
        return {"status": self.status}

    def generate_info(self):
        """ сгенерировать инфо данные устройства """
        return {"room": self.dev_params.get("room", "none"),
                "floor": self.dev_params.get("floor", 0)}

    def generate_msg(self, data):
        """ сгенерировать сообщение """
        return OrderedDict({
            "dt": datetime.now().strftime("%Y.%m.%d %H:%M:%S.%f")[:-3],
            "msg_type": "data",
            "dev": {
                "id": self.dev_id,
                "dev_name": self.dev_name,
                "type": self.device_type
            },
            "data": data,
            "info": self.generate_info()
        })

    def _kafka_send(self, msg, producer: Producer):
        """ отправка сообщения в kafka """
        producer.send(value=msg.encode('utf-8')).add_errback(self.error_callback)
        producer.flush()