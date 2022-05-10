from network.model import Model

model = Model()


def clasificator(text: str, pers: float = 0.0):
    return_data = {
        'status_thing': False,
        'status_do': False,
        'class_thing': None,
        'class_do': None,
        'pers_thing': None,
        'pers_do': None
    }
    text = text.lower()
    predicts_thing = model.predict(text, model.classes_thing)
    predicts_do = model.predict(text, model.classes_do)
    classnum_thing = predicts_thing.argmax()
    classnum_do = predicts_do.argmax()
    return_data['pers_thing'] = predicts_thing[classnum_thing]
    return_data['pers_do'] = predicts_do[classnum_do]
    # If not predict thing
    if return_data['pers_thing'] < pers:
        return return_data

    return_data['status_thing'] = True
    # If not predict what do
    if return_data['pers_do'] < pers:
        return_data['status_thing'] = False
        return return_data

    return_data['status_do'] = True
    return_data['class_thing'] = model.classes_thing[classnum_thing]
    return_data['class_do'] = model.classes_do[classnum_do]
    return return_data
