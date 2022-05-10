import threading
from smart_home.devices.base_device import BaseDevice


class SmartHome:
    def __init__(self, home_params=None):
        self.home_params = home_params
        self.dev_dict_id = {}
        self.dev_dict_name = {}

    def add_device(self, device: BaseDevice):
        """
        Добавление нового устройства в модель умного дома.
        Имя и id должны быть уникальными.
        Объект device относится к классу объектов из модуля smartDevices.py
        """
        if self.dev_dict_id.get(device.dev_id, None) is not None or device.dev_id is None:
            # Generation id
            id_list = list(self.dev_dict_id.keys())
            id_list.sort()
            device.dev_id = id_list[-1] + 1
        if device.dev_name is None:
            # Generating name
            types = [dev.device_type for dev in self.dev_dict_name.values()]
            count = types.count(device.device_type)
            device.dev_name = f'{device.device_type}_{count + 1}'
        self.dev_dict_name[device.dev_name] = device
        self.dev_dict_id[device.dev_id] = device

    def start(self):
        threads = []
        for key, val in self.dev_dict_id.items():
            threads.append(threading.Thread(target=val.start_read, args=()))
            threads.append(threading.Thread(target=val.start_generate, args=()))

        for thread in threads:
            thread.start()
