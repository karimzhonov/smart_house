from smart_home.devices.base_device import BaseDevice


class Button(BaseDevice):
    """ Кнопка """

    def __init__(self, **params):
        BaseDevice.__init__(self, **params)
        self.device_type = 'button'
        self.status = 'off'
