from smart_home.devices.base_device import BaseDevice


class Bulb(BaseDevice):
    """ обычная лампочка. вкл/выкл. отправляет своё состояние только"""

    def __init__(self, **params):
        BaseDevice.__init__(self, **params)
        self.status = "off"
        self.device_type = "bulb"

