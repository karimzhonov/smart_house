import json
from smart_home.consumer import Consumer


class ConsoleInterface:

    def __init__(self):
        self.cons = Consumer()

    @staticmethod
    def _format(date, dev_type, _id, dev_name, value, room, floor):
        value = value.center(60)
        dev_type = dev_type.upper().center(20)
        dev_name = dev_name.center(25)
        _id = str(_id).center(10)
        room = room.center(10)
        floor = floor.center(10)
        date = date.center(30)
        return f'{date} | {dev_type} | {_id} | {dev_name} | {value} | {room} | {floor}'

    def run(self):
        print(self._format('Date', 'Devace type', 'Id', 'Device name', 'Data', 'Room', 'Floor'))
        for msg in self.cons:
            data = json.loads(msg.value.decode('utf-8'))
            value = [f'{k}={v}' for k, v in data['data'].items()]
            print(self._format(data['dt'], data["dev"]["type"], data["dev"]["id"], data["dev"]["dev_name"],
                  f'{", ".join(value)}', data["info"]["room"], f'floor-{data["info"]["floor"]}'))
