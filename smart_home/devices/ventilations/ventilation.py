from smart_home.devices.base_device import BaseDevice


class Ventilation(BaseDevice):
    """ Управление ветиляцией """

    def __init__(self, **params):
        BaseDevice.__init__(self, **params)
        self.device_type = 'ventilation'
        self.speed = 100

    def _set_data(self, msg_dict):
        if msg_dict.get('cmd', None) in ['stop', 'off']:
            self.status = "stop"
        elif msg_dict.get('cmd', None) in ['start', 'on']:
            self.status = "work"
        if msg_dict.get('cmd', None) in ['settings']:
            if msg_dict.get('settings', None) is not None and msg_dict.get('settings', None).get('speed', None) is not None:
                self.speed = msg_dict['settings']['speed']

    def _generate_data(self):
        """ сгенерировать данные устройства """
        return {"status": self.status,
                "speed": self.speed}
