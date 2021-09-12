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


def display_text(board, fonts, screen):
    game_font = fonts[0]
    info_font = fonts[1]
    hp_text, hp_rect = game_font.render("hp: {}".format(board.hp), (0, 0, 0))
    wave_text, wave_rect = game_font.render("wave: {}".format(board.wave_number), (0, 0, 0))
    gold_text, gold_rect = game_font.render("gold: {}".format(board.gold), (0, 0, 0))
    s = "Q = StandartTower(10), W = SlowingTower(20), E = FiringTower(15), S = unchoose"
    info_text, info_rect = info_font.render("info: {}".format(s), (0, 0, 0))
    screen.blit(hp_text, (10, 10))
    screen.blit(wave_text, (400, 10))
    screen.blit(gold_text, (780, 10))
    screen.blit(info_text, (10, 558))


def find_square(x, y, board):
    for cell in board.cells:
        t = cell.in_cell(x, y)
        if not t:
            continue
        return cell
    return False


def logger(foo):
    def wrapper(*args, **kwargs):
        print(foo.__name__)
        return foo(*args, **kwargs)
    return wrapper


@logger
def create_tower(x, y, board):
    cell = find_square(x, y, board)
    if cell and board.gold >= board.tower_type.get_value():
        board.gold -= board.tower_type.get_value()
        t = board.tower_type.generateTower()
        t.x, t.y = cell.x1, cell.y1
        board.towers.append(t)
        board.tower_type = None


def show(obj, screen):
    if obj.visible == 0:
        return
    pic = get_picture(obj.img, (obj.size, obj.size))
    screen.blit(pic, (obj.x, obj.y))
