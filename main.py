import pygame
import sys
import yaml
import json


CONFIG_FILE = "config.yaml"
PORTS_FILE = "ports.json"


with open(PORTS_FILE) as json_file:
    ports = json.load(json_file)

with open(CONFIG_FILE) as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

pygame.init()
screen = pygame.display.set_mode((config.get("window_size"),
                                  config.get("window_size")))
pygame.display.set_caption(config.get("game_title"))

running = True
while running:
    screen.fill(tuple(config.get("background_color")))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_buttons = pygame.mouse.get_pressed()
            # mouse position event.pos
            # left click  mouse_buttons[0]
    pygame.display.flip()

pygame.quit()
sys.exit()
