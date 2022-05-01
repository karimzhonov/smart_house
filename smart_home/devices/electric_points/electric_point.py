from smart_home.devices.base_device import BaseDevice


class ElectricPoint(BaseDevice):
    """ Розетка """

    def __init__(self, **params):
        BaseDevice.__init__(self, **params)
        self.device_type = 'electric_point'
        self.status = 'on'
