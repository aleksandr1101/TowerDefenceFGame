import math
import pygame
from os import path
from cell import Cell


def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# load picture ./src/name with rect
def get_picture(name, rect=None):
    if rect is not None:
        p = pygame.transform.scale(pygame.image.load(path.join("img", name)), rect)
    else:
        p = pygame.image.load(path.join("img", name))
    return p


def display_text(board, game_font, screen):
    hp_text, hp_rect = game_font.render("hp: {}".format(board.hp), (0, 0, 0))
    wave_text, wave_rect = game_font.render("wave: {}".format(board.wave_number), (0, 0, 0))
    gold_text, gold_rect = game_font.render("gold: {}".format(board.gold), (0, 0, 0))
    screen.blit(hp_text, (10, 10))
    screen.blit(wave_text, (400, 10))
    screen.blit(gold_text, (780, 10))


def find_square(x, y, board):
    for cell in board.cells:
        t = cell.in_cell(x, y)
        if not t:
            continue
        return cell
    return False
