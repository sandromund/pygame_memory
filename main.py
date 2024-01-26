import json
import sys

import pygame
import yaml

from src.game import Game

CONFIG_FILE = "config.yaml"
PORTS_FILE = "ports.json"
IMG_BACK = "assets/memory_back.png"
IMG_FRONT = "assets/memory_front.png"

with open(PORTS_FILE) as json_file:
    ports = json.load(json_file)

with open(CONFIG_FILE) as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
pygame.init()

window_size = int(config.get("tile_size")) * int(config.get("board_size"))
screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption(config.get("game_title"))
img_back = pygame.image.load(IMG_BACK).convert()
img_front = pygame.image.load(IMG_FRONT).convert()
size = (config.get("tile_size"), config.get("tile_size"))
img_back = pygame.transform.scale(img_back, size)
img_front = pygame.transform.scale(img_front, size)

game = Game(ports=ports, config=config, img_front=img_front, img_back=img_back)

running = True
while running:
    screen.fill(tuple(config.get("background_color")))
    game.draw_board(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.filp_card(event.pos)
    pygame.display.flip()

pygame.quit()
sys.exit()
