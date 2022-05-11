from typer import Typer, Argument
from core.dialog import get_answer
from core.model_home import home
from telegram.loader import dp
from aiogram import executor

app = Typer()


def console_dialog():
    while True:
        text = input('[Person] - ')
        print(f'[BOT] - {get_answer(text)}')


def telegram_dialog():
    executor.start_polling(dp, skip_updates=True)


@app.command()
def main(mode: str = Argument('console', help='console, telegram')):
    home.start()
    if mode == 'console':
        console_dialog()
    elif mode == 'telegram':
        telegram_dialog()


if __name__ == '__main__':
    app()
