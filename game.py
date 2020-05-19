import pygame
import pygame.freetype
import utils
import unit
import tower
from os import path
from board import Board
import commands


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
info_font = pygame.freetype.Font(path.join("fonts", "info_font.ttf"), 18)
fonts = [game_font, info_font]

# title and icon
pygame.display.set_caption("TowerDefenceGame")

if __name__ == "__main__":
    # initial settings
    board = Board()

    # game loop
    board.get_new_wave()

    while board.running:
        event_commands = list()
        for event in pygame.event.get():
            # quit the game
            if event.type == pygame.QUIT:
                event_commands.append(commands.QuitCommand(board))
            # key press event
            if event.type == pygame.KEYDOWN:
                event_commands.append(commands.TowerChooseCommand(event.key, board))
            # tower to place choosing
            if event.type == pygame.MOUSEBUTTONUP:
                event_commands.append(commands.TowerPlacingCommand(board))

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
            utils.show(tow, screen)
            if pygame.time.get_ticks() - tow.prev_attack >= tow.attackTime:
                tow.attack(board.wave)
                tow.prev_attack = pygame.time.get_ticks()

        for monster in board.wave:
            monster.simulate_tick(board)
            utils.show(monster, screen)

        for event_command in event_commands:
            event_command.apply()
        utils.display_text(board, fonts, screen)
        pygame.display.update()
        clock.tick(tps)
