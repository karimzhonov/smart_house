from dialog2 import BOT_CONFIG

def load_dataset_thing():
    x, y = [], []
    for card in BOT_CONFIG:
        items = card['examples']
        for item in items:
            x.append(item)
            y.append(card['thing'])
    return x, y


def load_dataset_do():
    x, y = [], []
    for card in BOT_CONFIG:
        items = card['examples']
        for item in items:
            x.append(item)
            y.append(card['do'])
    return x, y

if __name__ == '__main__':
    print(load_dataset_do())