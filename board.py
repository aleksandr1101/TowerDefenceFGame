import unit
from cell import Cell


class Board:
    """information about the current game stats"""
    def __init__(self):
        self.hp = 10
        self.gold = 20
        self.wave_number = 0
        self.wave = list()
        self.towers = list()
        self.running = True
        self.tower_type = None
        self.cells = [Cell(110, 60, 189, 135), Cell(279, 60, 358, 135), Cell(448, 60, 527, 135),
                      Cell(615, 60, 695, 135), Cell(194, 225, 273, 303), Cell(362, 225, 443, 303),
                      Cell(530, 225, 611, 303), Cell(699, 225, 779, 303), Cell(110, 398, 189, 473),
                      Cell(279, 398, 358, 473), Cell(448, 398, 527, 473), Cell(615, 398, 695, 473)]

    def get_new_wave(self):
        self.wave = list()
        fact = None
        if self.wave_number % 4 == 0:
            fact = unit.StandartUnitFactory()
        elif self.wave_number % 4 == 1:
            fact = unit.FastUnitFactory()
        elif self.wave_number % 4 == 2:
            fact = unit.FatUnitFactory()
        else:
            fact = unit.BossUnitFactory()
        cnt = self.wave_number // 4 + 1
        for i in range(cnt):
            t = fact.generateUnit()
            t.y = 162
            t.x = (-70) * (i + 1)
            self.wave.append(t)
