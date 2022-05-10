from random import random

from smart_home.devices.base_device import BaseDevice


class Barometer(BaseDevice):
    """ Барометр """

    def __init__(self, **params):
        BaseDevice.__init__(self, **params)
        self.device_type = "barometer"

    def _set_data(self, msg_dict):
        if msg_dict['cmd'] in ['settings']:
            if msg_dict['settings'].get("period", None) is not None:
                self.dev_params['period'] = msg_dict['settings']['period']

    def _generate_data(self):
        """ сгенерировать данные устройства """
        return {"pressure": 700 + round(100*random(), 1)}
