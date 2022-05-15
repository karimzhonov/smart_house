from random import randint

from smart_home.devices.base_device import BaseDevice


class LeakSensor(BaseDevice):
    """ Датчик протечки """

    def __init__(self, **params):
        BaseDevice.__init__(self, **params)
        self.device_type = 'leak_sensor'
        self.signal = 0

    def _set_data(self, msg_dict):
        if msg_dict.get('cmd', None) in ['settings'] and msg_dict.get('settings', None) is not None:
            if msg_dict['settings'].get("period", None) is not None:
                self.dev_params['period'] = msg_dict['settings']['period']
            if msg_dict['settings'].get('signal', None) is not None:
                self.signal = msg_dict['settings']['signal']

    def _generate_data(self):
        """ сгенерировать данные устройства """
        return {"status": self.status,
                "leak_sensor_signal": self.signal}
