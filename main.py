import requests
import pygame
import sys
import os
import math


def update(lon, lat, z):
    api_server = "http://static-maps.yandex.ru/1.x/"

    params = {
        "ll": ",".join([str(lon), str(lat)]),
        "z": z,
        "l": "map"
    }

    response = requests.get(api_server, params=params)

    if not response:
        pass

    with open('tmp.png', 'wb') as image_file:
        image_file.write(response.content)

    sc = pygame.display.set_mode((600, 450))
    maps = pygame.image.load('tmp.png')
    maps_rect = maps.get_rect()
    sc.blit(maps, maps_rect)
    pygame.display.update()


# Подобранные константы для поведения карты.
LAT_STEP = 0.008 * 5  # Шаги при движении карты по широте и долготе
LON_STEP = 0.002 * 5
coord_to_geo_x = 0.0000428  # Пропорции пиксельных и географических координат.
coord_to_geo_y = 0.0000428

lon = 37.530887
lat = 55.703118
z = 17
changed = False
pygame.init()
update(lon, lat, z)

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            os.remove('tmp.png')
            sys.exit()
        elif i.type == pygame.KEYDOWN and i.key == pygame.K_PAGEUP and z < 17:
            z += 1
            changed = True
        elif i.type == pygame.KEYDOWN and i.key == pygame.K_PAGEDOWN and z > 0:
            z -= 1
            changed = True
        elif i.type == pygame.KEYDOWN and i.key == pygame.K_LEFT:
            lon -= LON_STEP * math.pow(2, 15 - z)
            changed = True
        elif i.type == pygame.KEYDOWN and i.key == pygame.K_RIGHT:
            lon += LON_STEP * math.pow(2, 15 - z)
            changed = True
        elif i.type == pygame.KEYDOWN and i.key == pygame.K_UP:
            lat -= LAT_STEP * math.pow(2, 15 - z)
            changed = True
        elif i.type == pygame.KEYDOWN and i.key == pygame.K_DOWN:
            lat += LAT_STEP * math.pow(2, 15 - z)
            changed = True

        if changed:
            update(lon, lat, z)
            changed = False

