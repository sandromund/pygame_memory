import random
from typing import List
import pygame


class Game:

    def __init__(self, ports: dict, config: dict):
        self.config = config
        self.board_size = config.get("board_size")
        self.card_back = config.get("back_color_card")
        self.card_front = config.get("front_color_card")
        self.tile_size = config.get("tile_size")

        self.port_to_protocol = ports
        self.protocol_to_port = {v: k for k, v in ports.items()}
        self.n_pairs = len(ports.items())
        self.board = self.init_board()
        self.flipped = [[True] * self.board_size] * self.board_size

    def init_board(self) -> List[List[str]]:
        board = [["0"] * self.board_size] * self.board_size
        cards = list(self.port_to_protocol.values()) + \
                list(self.protocol_to_port.values())
        random.shuffle(cards)
        print(cards)
        card_index = 0
        for i in range(self.board_size):
            for j in range(self.board_size):
                board[i][j] = cards[card_index]
                card_index += 1
        return board

    def draw_board(self, surface):
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.draw_card(surface, i, j)

    def draw_card(self, surface, i, j):

        card_rect = (j * self.tile_size,
                     i * self.tile_size,
                     self.tile_size,
                     self.tile_size)

        if self.flipped[i][j]:
            pygame.draw.rect(surface=surface,
                             color=self.card_front,
                             rect=card_rect)
            font = pygame.font.Font(None, 36)
            tile_value = str(self.board[i][j])
            text = font.render(tile_value, True, (0, 0, 0))
            text_rect = text.get_rect(center=(j * self.tile_size + self.tile_size // 2,
                                              i * self.tile_size + self.tile_size // 2))
            surface.blit(text, text_rect)
        else:
            pygame.draw.rect(surface=surface,
                             color=self.card_back,
                             rect=card_rect)
