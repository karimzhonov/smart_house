from random import randint

from smart_home.devices.base_device import BaseDevice


class MotionDetector(BaseDevice):
    """ Датчик движения """

    def __init__(self, **params):
        BaseDevice.__init__(self, **params)
        self.device_type = 'motion_detector'
        self.motion_signal = 0

    def _set_data(self, msg_dict):
        if msg_dict['cmd'] in ['settings']:
            if msg_dict['settings'].get("period", None) is not None:
                self.dev_params['period'] = msg_dict['settings']['period']
            if msg_dict['settings'].get('motion_signal', None) is not None:
                self.motion_signal = msg_dict['settings']['motion_signal']

    def __generate_data(self):
        """ сгенерировать данные устройства """
        return {"motion_signal": self.motion_signal}
