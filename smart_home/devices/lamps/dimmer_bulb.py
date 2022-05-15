from smart_home.devices.lamps.bulb import Bulb


class DimmerBulb(Bulb):
    """ Лампа с диммером """

    def __init__(self, **params):
        Bulb.__init__(self, **params)
        self.device_type = "dimmer_bulb"
        self.intensity = 100

    def _set_data(self, msg_dict):
        if msg_dict.get('cmd', None) in ['stop', 'off']:
            self.status = "stop"
        elif msg_dict.get('cmd', None) in ['start', 'on']:
            self.status = "work"
        if msg_dict.get('cmd', None) in ['settings'] and msg_dict.get('settings', None) is not None:
            if msg_dict['settings'].get('intensity', None) is not None:
                self.intensity = msg_dict['settings']['intensity']

    def _generate_data(self):
        """ сгенерировать данные устройства """
        return {"status": self.status,
                "intensity": self.intensity}
