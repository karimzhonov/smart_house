from random import random

from smart_home.devices.base_device import BaseDevice


class Thermometer(BaseDevice):
    """ датчик температуры. отправляет показания температуры окружающей среды """

    def __init__(self, **params):
        BaseDevice.__init__(self, **params)
        self.device_type = "thermometer"

    def _set_data(self, msg_dict):
        if msg_dict['cmd'] in ['settings']:
            if msg_dict['settings'].get("period", None) is not None:
                self.dev_params['period'] = msg_dict['settings']['period']

    def __generate_data(self):
        """ сгенерировать данные устройства """
        return {"temperature": 25 + round(random(), 2)}
