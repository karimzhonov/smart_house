import torch
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification


class Model:
    classes_do = ['включи', 'определение', 'управление', 'выключи']
    classes_thing = ['свет', 'музыка', 'кондиционер', 'дверь', 'влажност', 'температура']

    def __init__(self, model_checkpoint='cointegrated/rubert-base-cased-nli-threeway'):
        self.model_checkpoint = model_checkpoint

        self.tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint)
        if torch.cuda.is_available():
            self.model.cuda()

    def predict(self, text, label_texts, label='entailment', normalize=True):
        tokens = self.tokenizer([text] * len(label_texts), label_texts, truncation=True, return_tensors='pt',
                                padding=True)
        with torch.inference_mode():
            result = torch.softmax(self.model(**tokens.to(self.model.device)).logits, -1)
        proba = result[:, self.model.config.label2id[label]].cpu().numpy()
        if normalize:
            proba /= sum(proba)
        return proba
