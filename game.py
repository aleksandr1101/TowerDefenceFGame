import pygame
import pygame.freetype
import utils
import unit
import tower
from os import path
from board import Board


# initializing game
pygame.init()

# ticks per second
tps = 60
clock = pygame.time.Clock()

# create the screen
screenX = 900
screenY = 580
screen = pygame.display.set_mode((screenX, screenY))
bg = utils.get_picture("bg.png", (screenX, screenY))
game_font = pygame.freetype.Font(path.join("fonts", "game_font.ttf"), 24)

# title and icon
pygame.display.set_caption("TowerDefenceGame")
# icon = utils.get_picture("checkers.png")
# pygame.display.set_icon(icon)

# initial settings
board = Board()

# game loop
running = True
board.get_new_wave()
tower_type = None

while running:
    for event in pygame.event.get():
        # quit the game
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                tower_type = tower.StandartTowerFactory()
            elif event.key == pygame.K_w:
                tower_type = tower.SlowingTowerFactory()
            elif event.key == pygame.K_e:
                tower_type = tower.FireTowerFactory()
            elif event.key == pygame.K_s:
                tower_type = None
        if event.type == pygame.MOUSEBUTTONUP:
            if tower_type is not None:
                x, y = pygame.mouse.get_pos()
                cell = utils.find_square(x, y, board)
                if cell and board.gold >= tower_type.get_value():
                    board.gold -= tower_type.get_value()
                    t = tower_type.generateTower()
                    t.x, t.y = cell.x1, cell.y1
                    board.towers.append(t)
                    print(x, y)

    if board.hp <= 0:
        board = Board()
        pygame.time.wait(1000)
        board.get_new_wave()
        continue

    cnt = 0
    for monster in board.wave:
        cnt += monster.visible
    if cnt == 0:
        pygame.time.wait(1000)
        board.wave_number += 1
        board.get_new_wave()
        continue

    screen.blit(bg, (0, 0))

    for tow in board.towers:
        tow.show(screen)
        if pygame.time.get_ticks() - tow.prev_attack >= tow.attackTime:
            tow.attack(board.wave)
            tow.prev_attack = pygame.time.get_ticks()

    for monster in board.wave:
        monster.simulate_tick(board)
        monster.show(screen)

    utils.display_text(board, game_font, screen)
    pygame.display.update()
    clock.tick(tps)
