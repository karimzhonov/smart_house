from smart_home import SmartHome
from smart_home.devices.buttons import Button
from smart_home.devices.locks import DoorLock
from smart_home.devices.sensors import LeakSensor
from smart_home.devices.detectors import MotionDetector
from smart_home.devices.ventilations import Ventilation
from smart_home.devices.roller_shutters import RollerShutter
from smart_home.devices.floor_heatings import FloorHeating
from smart_home.devices.electric_points import ElectricPoint
from smart_home.devices.lamps import Bulb, RGBLight, DimmerBulb
from smart_home.devices.measuring_devices import Thermometer, Barometer, Hygrometer


if __name__ == '__main__':
    # параметры kafka
    kafka_params = {"bootstrap_servers": "164.92.231.185:9092", "topic": "testTopic"}

    home = SmartHome()

    # создание устройств
    lamps = [
        Bulb(kafka_params=kafka_params, dev_id=1, dev_params={"period": 2, "room": "room_1", "floor": 1}),
        DimmerBulb(kafka_params=kafka_params, dev_id=2, dev_params={"period": 3, "room": "room_2", "floor": 1}),
        RGBLight(kafka_params=kafka_params, dev_id=3, dev_params={"period": 4, "room": "room_3", "floor": 2})
    ]
    measuring_diveces = [
        Barometer(kafka_params=kafka_params, dev_id=4, dev_params={"period": 5, "room": "room_1", "floor": 1}),
        Thermometer(kafka_params=kafka_params, dev_id=5, dev_params={"period": 2.5, "room": "room_1", "floor": 2}),
        Hygrometer(kafka_params=kafka_params, dev_id=5, dev_params={"period": 6, "room": "room_1", "floor": 1})
    ]
    devices = [
        *lamps, *measuring_diveces,
        Button(kafka_params=kafka_params, dev_params={"period": 2.5, "room": "room_1", "floor": 1}),
        DoorLock(kafka_params=kafka_params, dev_params={"period": 2.5, "room": "room_1", "floor": 1}),
        LeakSensor(kafka_params=kafka_params, dev_params={"period": 2.5, "room": "room_1", "floor": 2}),
        MotionDetector(kafka_params=kafka_params, dev_params={"period": 8, "room": "room_2", "floor": 1}),
        Ventilation(kafka_params=kafka_params, dev_params={"period": 2.5, "room": "room_1", "floor": 1}),
        RollerShutter(kafka_params=kafka_params, dev_params={"period": 3, "room": "room_4", "floor": 2}),
        FloorHeating(kafka_params=kafka_params, dev_params={"period": 2.5, "room": "room_1", "floor": 1}),
        ElectricPoint(kafka_params=kafka_params, dev_params={"period": 2.5, "room": "room_1", "floor": 1}),
    ]
    # добавление устройств в дом
    for _d in devices:
        home.add_device(_d)

    # запуск модели для генерации сигналов от устройств умного дома
    home.start()
