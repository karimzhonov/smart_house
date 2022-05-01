from smart_home.devices.base_device import BaseDevice


class RollerShutter(BaseDevice):
    """ Роль-ставни """

    def __init__(self, **params):
        BaseDevice.__init__(self, **params)
        self.device_type = 'roller_shutter'
        self.top_point = 0
        self.bottom_point = 100

    def _set_data(self, msg_dict):
        if msg_dict['cmd'] in ['stop', 'off']:
            self.status = "stop"
            self.top_point = 0
            self.bottom_point = 100
        elif msg_dict['cmd'] in ['start', 'on']:
            self.status = "work"
            self.top_point = 0
            self.bottom_point = 0
        if msg_dict['cmd'] in ['settings']:
            if msg_dict['settings'].get('top_point', None) is not None:
                self.top_point = msg_dict['settings']['top_point']
            if msg_dict['settings'].get('bottom_point', None) is not None:
                self.top_point = msg_dict['settings']['bottom_point']

    def __generate_data(self):
        """ сгенерировать данные устройства """
        return {"status": self.status,
                "top_point": self.top_point,
                "bottom_point": self.bottom_point}
