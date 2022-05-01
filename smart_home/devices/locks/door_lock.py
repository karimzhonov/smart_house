from smart_home.devices.base_device import BaseDevice


class DoorLock(BaseDevice):
    """ Электронный дверной замок """

    def __init__(self, **params):
        BaseDevice.__init__(self, **params)
        self.device_type = 'door_lock'
