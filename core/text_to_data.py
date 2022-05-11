from network.classificator import clasificator
from core.dataset import THING_TO_DATA, DO_TO_DATA
from core.model_home import home

__all__ = ['text_to_data']


def text_to_data(text: str):
    text = text.lower()
    return_data = {
        'id': None,
        'cmd': None,
        'settings': None,
    }
    data = clasificator(text)
    for key, llist in THING_TO_DATA.items():
        if data['class_thing'] in llist:
            # Search device
            for _id, dev in home.dev_dict_id.items():
                if dev.device_type == key:
                    return_data['id'] = _id

    for key, llist in DO_TO_DATA.items():
        if data['class_do'] in llist:
            if key in ['on', 'off']:
                return_data['cmd'] = key
            else:
                return_data['cmd'] = 'settings'
                return_data['settings'] = {
                    key: data['class_number']
                }

    return return_data
