from random import random

from smart_home.devices.base_device import BaseDevice


class Hygrometer(BaseDevice):
    """ Датчик влажности """

    def __init__(self, **params):
        BaseDevice.__init__(self, **params)
        self.device_type = "hygrometer"

    def _set_data(self, msg_dict):
        if msg_dict.get('cmd', None) in ['settings'] and msg_dict.get('settings', None) is not None:
            if msg_dict['settings'].get("period", None) is not None:
                self.dev_params['period'] = msg_dict['settings']['period']

    def _generate_data(self):
        """ сгенерировать данные устройства """
        return {"humidity": 70 + round(20 * random(), 1)}
