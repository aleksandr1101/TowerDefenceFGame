# from game import tps
import utils
import pygame

basicDuration = 5
bossDuration = 3

basicDPT = 2
speedyDPT = 4
bossDPT = 1

basicSlowing = 0.7
fatSlowing = 0.5
bossSlowing = 0.8
stop_lvl = [811, 330, 45, 500, 678]


class Unit:
    """Base class for walking monsters"""
    def __init__(self, speed, hp, goldGaining, img):
        """Init of basic unit"""
        self.speed = speed
        self.hp = hp
        self.goldGaining = goldGaining
        self.img = img
        self.slowing = 1.0
        self.dDuration = 0
        self.sDuration = 0
        self.dpt = 0
        self.x = 0
        self.y = 0
        self.pos_l = 0
        self.visible = 1

    def light(self):
        """if unit stroken by fire tower"""
        self.dDuration = basicDuration
        self.dpt = basicDPT

    def slow_down(self):
        """if unit is stroken by slowing tower"""
        self.sDuration = basicDuration
        self.slowing = basicSlowing

    def get_damage(self, dmg):
        """getting damage from any tower"""
        self.hp -= dmg

    def move_monster(self, real_speed):
        if self.pos_l % 2 == 0:
            self.x += real_speed
            if self.pos_l == 2:
                self.x -= real_speed * 2
            if ((self.pos_l != 2 and self.x >= stop_lvl[self.pos_l]) or
                    (self.pos_l == 2 and self.x <= stop_lvl[self.pos_l])):
                self.x = stop_lvl[self.pos_l]
                self.pos_l += 1
        else:
            self.y += real_speed
            if self.y >= stop_lvl[self.pos_l]:
                self.y = stop_lvl[self.pos_l]
                self.pos_l += 1

    def simulate_tick(self, board):
        """simulating one tick of game behind the unit"""
        self.dDuration -= 1
        self.sDuration -= 1

        # if slowing is off
        if self.sDuration <= 0:
            self.sDuration = 0
            self.slowing = 1.0
        # if fire damage is off
        if self.dDuration <= 0:
            self.dDuration = 0
            self.dpt = 0

        real_speed = round(self.speed * self.slowing)
        self.hp -= self.dpt

        if self.hp <= 0:
            self.hp = 0
            if self.visible:
                board.gold += 1
            self.visible = 0
            # todo: kill unit
            return

        if self.pos_l == 5:
            self.visible = 0
            self.pos_l = 6
            board.hp -= 1

        if self.pos_l == 6:
            return

        self.move_monster(real_speed)

    def show(self, screen):
        if self.visible == 0:
            return
        pic = utils.get_picture(self.img, (40, 40))
        screen.blit(pic, (self.x, self.y))

    def center(self):
        return self.x + 20, self.y + 20


class StandartUnit(Unit):
    """Standart unit"""

    def __init__(self):
        super().__init__(6, 40, 0, "red.png")


class FastUnit(Unit):
    """Fast unit class, it fires well"""

    def __init__(self):
        super().__init__(8, 25, 0, "dog.png")

    def light(self):
        """if unit stroken by fire tower"""
        self.dDuration = basicDuration
        self.dpt = speedyDPT


class FatUnit(Unit):
    """Fat unit class, it freeze well"""

    def __init__(self):
        super().__init__(4, 100, 0, "por.png")

    def slow_down(self):
        """if unit is stroken by slowing tower"""
        self.sDuration = basicDuration
        self.slowing = fatSlowing


class BossUnit(Unit):
    """Boss unit class, it fires and freeze bad"""

    def __init__(self):
        super().__init__(5, 80, 0, "yolo.png")

    def light(self):
        """if unit stroken by fire tower"""
        self.dDuration = bossDuration
        self.dpt = bossDPT

    def slow_down(self):
        """if unit is stroken by slowing tower"""
        self.sDuration = bossDuration
        self.slowing = bossSlowing


class UnitFactiory:
    def generateUnit(self):
        return None


class StandartUnitFactory(UnitFactiory):
    def generateUnit(self):
        return StandartUnit()


class FastUnitFactory(UnitFactiory):
    def generateUnit(self):
        return FastUnit()


class FatUnitFactory(UnitFactiory):
    def generateUnit(self):
        return FatUnit()


class BossUnitFactory(UnitFactiory):
    def generateUnit(self):
        return BossUnit()
