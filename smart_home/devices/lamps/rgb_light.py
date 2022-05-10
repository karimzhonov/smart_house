from smart_home.devices.lamps.bulb import Bulb


class RGBLight(Bulb):
    """ RGB источник света """

    def __init__(self, **params):
        Bulb.__init__(self, **params)
        self.device_type = 'rgb_light'
        self.red_intensity = 100
        self.green_intensity = 100
        self.blue_intensity = 100

    def _set_data(self, msg_dict):
        if msg_dict['cmd'] in ['stop', 'off']:
            self.status = "stop"
        elif msg_dict['cmd'] in ['start', 'on']:
            self.status = "work"
        if msg_dict['cmd'] in ['settings']:
            if msg_dict['settings'].get('red_intensity', None) is not None:
                self.red_intensity = msg_dict['settings']['red_intensity']
            if msg_dict['settings'].get('green_intensity', None) is not None:
                self.green_intensity = msg_dict['settings']['green_intensity']
            if msg_dict['settings'].get('blue_intensity', None) is not None:
                self.blue_intensity = msg_dict['settings']['blue_intensity']

    def _generate_data(self):
        """ сгенерировать данные устройства """
        return {"status": self.status,
                "red_intensity": self.red_intensity,
                "green_intensity": self.green_intensity,
                "blue_intensity": self.blue_intensity}
