from network.model import Model
from network.dataset import THING_TO_DATA, DO_TO_DATA

classes_do = []
for v in DO_TO_DATA.values():
    classes_do = [*classes_do, *v]

classes_thing = []
for v in THING_TO_DATA.values():
    classes_thing = [*classes_thing, *v]

model = Model(classes_do=classes_do, classes_thing=classes_thing)


def clasificator(text: str, pers_thing: float = 0.3, pers_do: float = 0.1, pers_number: float = 0.1):
    return_data = {
        'class_thing': None,
        'class_do': None,
        'class_number': None,
        'pers_thing': None,
        'pers_do': None,
        'pers_number': None,
    }
    text = text.lower()
    # Predicts
    predicts_thing = model.predict(text, model.classes_thing)
    predicts_do = model.predict(text, model.classes_do)
    predicts_number = model.predict(text, model.classes_numbers)
    # Index clasnum
    classnum_thing = predicts_thing.argmax()
    classnum_do = predicts_do.argmax()
    classnum_number = predicts_number.argmax()
    # Persent predict
    return_data['pers_thing'] = str(predicts_thing[classnum_thing])
    return_data['pers_do'] = str(predicts_do[classnum_do])
    return_data['pers_number'] = str(predicts_number[classnum_number])
    # If not predict thing
    if predicts_thing[classnum_thing] > pers_thing:
        return_data['class_thing'] = model.classes_thing[classnum_thing]

    # If not predict what do
    if predicts_do[classnum_do] > pers_do:
        return_data['class_do'] = model.classes_do[classnum_do]

    # If not predict number
    if predicts_number[classnum_number] > pers_number:
        return_data['class_number'] = model.classes_numbers[classnum_number]

    return return_data
