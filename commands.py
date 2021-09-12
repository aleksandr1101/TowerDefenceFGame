import pygame
import tower
import utils


class QuitCommand:
    def __init__(self, board):
        self.board = board

    def apply(self):
        self.board.running = False


class TowerChooseCommand:
    def __init__(self, key_type, board):
        self.key_type = key_type
        self.board = board

    def apply(self):
        kt = self.key_type
        board = self.board
        if kt == pygame.K_q:
            board.tower_type = tower.StandartTowerFactory()
        elif kt == pygame.K_w:
            board.tower_type = tower.SlowingTowerFactory()
        elif kt == pygame.K_e:
            board.tower_type = tower.FireTowerFactory()
        elif kt == pygame.K_s:
            board.tower_type = None


class TowerPlacingCommand:
    def __init__(self, board):
        self.board = board

    def apply(self):
        board = self.board
        if board.tower_type is not None:
            x, y = pygame.mouse.get_pos()
            utils.create_tower(x, y, board)
