from typer import Typer, Option
from network.classificator import clasificator

app = Typer()


@app.command()
def main(text: str = Option(None, help='Input text'),
         pers: float = Option(None, help='Persent errors')):
    if text is None:
        print('Run with option --text')
        return
    if pers is None: pers = 0.0
    data = clasificator(text, pers)
    print(data)


if __name__ == '__main__':
    app()