import json
from typer import Typer, Option
from smart_home.producer import Producer

app = Typer()


@app.command()
def main(dev_id: int = Option(None), cmd: str = Option(None), period: int = Option(None),
         motion_signal: int = Option(None), temperature: int = Option(None), intensity: int = Option(None),
         red_intensity: int = Option(None), green_intensity: int = Option(None), blue_intensity: int = Option(None),
         top_point: int = Option(None), bottom_point: int = Option(None), signal: int = Option(None),
         speed: int = Option(None)):
    if dev_id is None or cmd is None:
        return print('--dev-id and --cmd options must be given')
    data = {
        "id": dev_id,
        "cmd": cmd,
        "settings": {
            "period": period,
            "motion_signal": motion_signal,
            "temperature": temperature,
            "intensity": intensity,
            "red_intensity": red_intensity,
            "green_intensity": green_intensity,
            "blue_intensity": blue_intensity,
            "top_point": top_point,
            "bottom_point": bottom_point,
            "speed": speed,
            "signal": signal,
        }
    }
    data = json.dumps(data, indent=4)
    prod = Producer()
    prod.send(data.encode('utf-8'))
    prod.flush()
    print(data)


if __name__ == '__main__':
    app()
