from network.classificator import clasificator
from network.dataset import THING_TO_DATA, DO_TO_DATA
from core.model_home import home

__all__ = ['text_to_data']


def text_to_data(text: str):
    _dev = None
    text = text.lower()
    data = clasificator(text)
    _data = {
        'id': None,
        'cmd': None,
        'settings': None
    }
    for key, llist in THING_TO_DATA.items():
        if data['class_thing'] in llist:
            # Search device
            for _id, dev in home.dev_dict_id.items():
                if dev.device_type == key:
                    _data['id'] = _id
                    _dev = dev

    for key, llist in DO_TO_DATA.items():
        if data['class_do'] in llist:
            if key in ['on', 'off']:
                _data['cmd'] = key
            else:
                _data['cmd'] = 'settings'
                _data['settings'] = {key: data['class_number']}

    if _dev is not None:
        return _dev.generate_msg(_data)
