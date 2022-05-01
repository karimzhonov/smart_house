from smart_home.devices.base_device import BaseDevice


class Ventilation(BaseDevice):
    """ Управление ветиляцией """

    def __init__(self, **params):
        BaseDevice.__init__(self, **params)
        self.device_type = 'ventilation'
        self.speed = 100

    def _set_data(self, msg_dict):
        if msg_dict['cmd'] in ['stop', 'off']:
            self.status = "stop"
        elif msg_dict['cmd'] in ['start', 'on']:
            self.status = "work"
        if msg_dict['cmd'] in ['settings']:
            if msg_dict['settings'].get('speed', None) is not None:
                self.speed = msg_dict['settings']['speed']

    def __generate_data(self):
        """ сгенерировать данные устройства """
        return {"status": self.status,
                "speed": self.speed}
