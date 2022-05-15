from network.classificator import clasificator
from network.dataset import THING_TO_DATA, DO_TO_DATA
from core.model_home import home

__all__ = ['text_to_data']


def text_to_data(text: str):
    text = text.lower()
    data = clasificator(text)
    for key, llist in THING_TO_DATA.items():
        if data['class_thing'] in llist:
            # Search device
            for _id, dev in home.dev_dict_id.items():
                if dev.device_type == key:
                    data['id'] = _id

    for key, llist in DO_TO_DATA.items():
        if data['class_do'] in llist:
            if key in ['on', 'off']:
                data['cmd'] = key
            else:
                data['cmd'] = 'settings'
                data['settings'] = key

    return data
