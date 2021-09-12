from utils import dist
import utils
from random import choice
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
        self.size = 80
        self.visible = 1

    def upgrade(self):
        """upgrade tower lvl for more damage and special effects"""
        if self.lvl != 3:
            self.lvl += 1

    def get_target(self, units):
        """Get target for attacking it"""
        # attacking the nearest unit

        suitable_units = list()
        for unit in units:
            towerX, towerY = self.center()
            unitX, unitY = unit.center()
            new_dist = dist(towerX, towerY, unitX, unitY)
            if new_dist <= self.range:
                suitable_units.append(unit)
        if len(suitable_units) == 0:
            return None
        return choice(suitable_units)

    def attack(self, units):
        """attacking the enemy with self.damage"""
        enemy = self.get_target(units)
        if enemy is None:
            return
        enemy.get_damage(self.damage[self.lvl])

    def center(self):
        return self.x + 40, self.y + 40


class FireTower(Tower):
    """Firing tower"""

    def __init__(self):
        super().__init__([1, 1, 1], tps, 100, "firing.png")

    def attack(self, units):
        """attacking the enemy with self.damage"""
        enemy = self.get_target(units)
        if enemy is None:
            return
        enemy.get_damage(self.damage[self.lvl])
        enemy.light()
        # todo: flying bullet


class SlowingTower(Tower):
    """Firing tower"""

    def __init__(self):
        super().__init__([0, 0, 0], tps // 2, 200, "freezing.png")

    def attack(self, units):
        """attacking the enemy with self.damage"""
        enemy = self.get_target(units)
        if enemy is None:
            return
        enemy.get_damage(self.damage[self.lvl])
        enemy.slow_down()


class StandartTower(Tower):
    """Standart tower"""

    def __init__(self):
        super().__init__([3, 3, 3], tps, 130, "damaging.png")


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
