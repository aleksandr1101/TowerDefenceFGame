from utils import dist
import utils
import random
import pygame
from unit import Unit
from unit import BossUnit
from unit import FatUnit
from unit import FastUnit

tps = 60


class Tower:
    """Base class of towers"""

    def __init__(self, damage, attackTime, towerRange, img):
        self.damage = damage
        self.attackTime = attackTime
        self.prev_attack = 0
        self.range = towerRange
        self.lvl = 1
        self.img = img
        self.x = 0
        self.y = 0

    def upgrade(self):
        """upgrade tower lvl for more damage and special effects"""
        if self.lvl != 3:
            self.lvl += 1

    def getTarget(self, units):
        """Get target for attacking it"""
        # attacking the nearest unit

        eq = list()
        for unit in units:
            cX, cY = self.center()
            uX, uY = unit.center()
            newDist = dist(cX, cY, uX, uY)
            if newDist <= self.range:
                eq.append(unit)
        if len(eq) == 0:
            return None
        return eq[random.randint(0, len(eq) - 1)]

    def attack(self, units):
        """attacking the enemy with self.damage"""
        enemy = self.getTarget(units)
        if enemy is None:
            return
        enemy.get_damage(self.damage[self.lvl])
        # todo: flying bullet

    def show(self, screen):
        pic = utils.get_picture(self.img, (80, 80))
        # pygame.draw.circle(screen, (255, 255, 255), self.center(), self.range, 1)
        screen.blit(pic, (self.x, self.y))

    def center(self):
        return self.x + 40, self.y + 40


class FireTower(Tower):
    """Firing tower"""

    def __init__(self):
        super().__init__([1, 1, 1], tps, 100, "firing.png")

    def attack(self, units):
        """attacking the enemy with self.damage"""
        enemy = self.getTarget(units)
        if enemy is None:
            return
        enemy.get_damage(self.damage[self.lvl])
        enemy.light()
        # todo: flying bullet


class SlowingTower(Tower):
    """Firing tower"""

    def __init__(self):
        super().__init__([1, 1, 1], tps // 2, 200, "freezing.png")

    def attack(self, units):
        """attacking the enemy with self.damage"""
        enemy = self.getTarget(units)
        if enemy is None:
            return
        enemy.get_damage(self.damage[self.lvl])
        enemy.slow_down()
        # todo: flying bullet


class StandartTower(Tower):
    """Standart tower"""

    def __init__(self):
        super().__init__([1, 1, 1], tps, 130, "damaging.png")


class TowerFactory:
    def generateTower(self):
        return None

    @staticmethod
    def get_value():
        return 0


class FireTowerFactory(TowerFactory):
    def generateTower(self):
        return FireTower()

    @staticmethod
    def get_value():
        return 15


class SlowingTowerFactory(TowerFactory):
    def generateTower(self):
        return SlowingTower()

    @staticmethod
    def get_value():
        return 20


class StandartTowerFactory(TowerFactory):
    def generateTower(self):
        return StandartTower()

    @staticmethod
    def get_value():
        return 10
