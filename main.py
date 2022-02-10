import requests
import pygame
import sys
import os

def get_image():
    api_server = "http://static-maps.yandex.ru/1.x/"

    lon = "37.530887"
    lat = "55.703118"

    params = {
        "ll": ",".join([lon, lat]),
        "z": 8,
        "l": "map"
    }
    response = requests.get(api_server, params=params)

    if not response:
        pass

    return response.content


with open('tmp.png', 'wb') as image_file:
    image_file.write(get_image())

sc = pygame.display.set_mode((600, 450))
maps = pygame.image.load('tmp.png')
maps_rect = maps.get_rect()
sc.blit(maps, maps_rect)
pygame.display.update()
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            os.remove('tmp.png')
            sys.exit()
