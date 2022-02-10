import os

import requests
from io import BytesIO
from PIL import Image


def get_image():
    api_server = "http://static-maps.yandex.ru/1.x/"

    lon = "37.530887"
    lat = "55.703118"
    delta = "0.002"

    params = {
        "ll": ",".join([lon, lat]),
        "z": 8,
        "l": "map"
    }
    response = requests.get(api_server, params=params)

    if not response:
        # обработка ошибочной ситуации
        pass

    return response.content


# query = input()
with open('tmp.png', 'wb') as image_file:
    image_file.write(get_image())

Image.open('tmp.png').show()
os.remove('tmp.png')
