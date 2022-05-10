from smart_home.devices.base_device import BaseDevice


class FloorHeating(BaseDevice):
    """ Теплый пол """

    def __init__(self, **params):
        BaseDevice.__init__(self, **params)
        self.device_type = 'floor_heating'
        self.status = 'off'
        self.temperature = 40

    def _set_data(self, msg_dict):
        if msg_dict['cmd'] in ['stop', 'off']:
            self.status = "stop"
        elif msg_dict['cmd'] in ['start', 'on']:
            self.status = "work"
        if msg_dict['cmd'] in ['settings']:
            if msg_dict['settings'].get('temperature', None) is not None:
                self.temperature = msg_dict['settings']['temperature']

    def _generate_data(self):
        """ сгенерировать данные устройства """
        return {"status": self.status,
                "temperature": self.temperature}
