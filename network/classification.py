import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# скачивание модели
model_checkpoint = 'cointegrated/rubert-base-cased-nli-threeway'
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint)
if torch.cuda.is_available():
    model.cuda()


# инициализация функции
def predict_zero_shot(text, label_texts, model, tokenizer, label='entailment', normalize=True):
    tokens = tokenizer([text] * len(label_texts), label_texts, truncation=True, return_tensors='pt', padding=True)
    with torch.inference_mode():
        result = torch.softmax(model(**tokens.to(model.device)).logits, -1)
    proba = result[:, model.config.label2id[label]].cpu().numpy()
    if normalize:
        proba /= sum(proba)
    return proba

classes_do = ['включи', 'определение', 'управление', 'выключи']
classes_thing = ['свет', 'музыка', 'кондиционер', 'дверь', 'влажност', 'температура']

while True:
    txt = input('Person - ')
    predicts_thing = predict_zero_shot(txt, classes_thing, model, tokenizer)
    predicts_do = predict_zero_shot(txt, classes_do, model, tokenizer)

    classnum_thing = predicts_thing.argmax()
    classnum_do = predicts_do.argmax()

    if predicts_thing[classnum_thing] < 0.5:
        print('Попробуйте по другому')
        continue
    else:
        if predicts_do[classnum_do] < 0.5:
            print('Что делать ?')
            txt = input('Person - ')
            predicts_do = predict_zero_shot(txt, classes_do, model, tokenizer)
            classnum_do = predicts_do.argmax().item()
            if predicts_do[classnum_do] < 0.5:
                pass
            print(f'Bot - "{classes_thing[classnum_thing]}" === "{classes_do[classnum_do]}"')
            continue
    print(f'Bot - "{classes_thing[classnum_thing]}" === "{classes_do[classnum_do]}"')