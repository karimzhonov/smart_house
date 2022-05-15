import json
from core.text_to_data import text_to_data
from smart_home.producer import Producer
from smart_home.consumer import Consumer
from config import *

prod = Producer(kafka_topic=KAFKA_TOPIC, kafka_servers=KAFKA_SERVERS)
cons = Consumer(kafka_topic=KAFKA_TOPIC, kafka_servers=KAFKA_SERVERS)


def get_answer(text: str):
    data = text_to_data(text)

    if data is None:
        return 'Bot not undestand what do you want'
    if data['data']['cmd'] is None:
        # Get data from device
        for msg in cons:
            msg_dict = json.loads(msg.value.decode('utf-8'))
            if msg_dict.get('dev', None) is not None and msg_dict['dev'].get('id', None) == data['data']['id']:
                # Generate answer about status device
                return f'[RECIVE DATA] - {json.dumps(msg_dict, indent=4, ensure_ascii=False)}'
    else:
        data = json.dumps(data, indent=4, ensure_ascii=False)
        # Send data
        prod.send(data.encode('utf-8'))
        prod.flush()
        # Generating answer about response
        return f'[SEND DATA] - {data}'
