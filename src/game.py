import random
from typing import List

import numpy as np
import pygame
from icecream import ic


class Game:

    def __init__(self, ports: dict, config: dict):
        self.config = config
        self.board_size = config.get("board_size")
        self.card_back = config.get("back_color_card")
        self.card_front = config.get("front_color_card")
        self.tile_size = config.get("tile_size")
        self.n_cards = self.board_size ** 2
        self.port_to_protocol = ports
        self.protocol_to_port = {v: k for k, v in ports.items()}
        self.mapper = self.get_mapper()

        self.flipped = np.zeros(self.n_cards, dtype=bool)
        self.flipped = self.flipped.reshape((self.board_size, self.board_size))

        self.solved = np.zeros(self.n_cards, dtype=bool)
        self.solved = self.solved.reshape((self.board_size, self.board_size))

        self.board = np.arange(self.n_cards)
        np.random.shuffle(self.board)
        self.board = self.board.reshape((self.board_size, self.board_size))

    def get_mapper(self):
        mapper = {}
        int_index = 0
        for port in self.port_to_protocol.values():
            mapper[int_index] = port
            int_index += 1
        for protocol in self.protocol_to_port.values():
            mapper[int_index] = protocol
            int_index += 1
        return mapper

    def draw_board(self, surface):
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.draw_card(surface, i, j)

    def draw_card(self, surface, i, j):

        if self.solved[i,j]:
            return

        card_rect = (j * self.tile_size,
                     i * self.tile_size,
                     self.tile_size,
                     self.tile_size)

        if self.flipped[i][j]:
            pygame.draw.rect(surface=surface,
                             color=self.card_front,
                             rect=card_rect)
            font = pygame.font.Font(None, 36)
            tile_value = str(self.mapper.get(self.board[i][j]))
            text = font.render(tile_value, True, (0, 0, 0))
            text_rect = text.get_rect(center=(j * self.tile_size + self.tile_size // 2,
                                              i * self.tile_size + self.tile_size // 2))
            surface.blit(text, text_rect)
        else:
            pygame.draw.rect(surface=surface,
                             color=self.card_back,
                             rect=card_rect)

    def filp_card(self, screen_position):
        x, y = screen_position
        x_new = int(x // self.tile_size)
        y_new = int(y // self.tile_size)
        x_new = min(max(0, x_new), self.tile_size)
        y_new = min(max(0, y_new), self.tile_size)
        self.flipped[y_new][x_new] = not self.flipped[y_new][x_new]
