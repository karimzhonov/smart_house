from typer import Typer, Option
from network.classificator import clasificator

app = Typer()


@app.command()
def main(text: str = Option(None, help='Input text'),):
    if text is not None:
        data = clasificator(text)
        print(data)
        return

    while True:
        text = input('[Person] - ')
        data = clasificator(text)
        print(f'[BOT] - {data}')


if __name__ == '__main__':
    app()