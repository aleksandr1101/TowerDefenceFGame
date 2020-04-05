from utils import dist
from unit import Unit
from unit import BossUnit
from unit import FatUnit
from unit import FastUnit
from game import tps


class Tower:
    """Base class of towers"""

    def __init__(self, damage, attackTime, towerRange, img):
        self.damage = damage
        self.attackTime = attackTime
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

        best = None
        for unit in units:
            newDist = dist(self.x, self.y, unit.x, unit.y)
            if newDist <= self.range and (best is None or dist(self.x, self.y, best.x, best.y) > newDist):
                best = unit

        return best

    def attack(self, units):
        """attacking the enemy with self.damage"""
        enemy = self.getTarget(units)
        if enemy is None:
            return
        enemy.getDamage(self.damage[self.lvl])
        # todo: flying bullet


class FireTower(Tower):
    """Firing tower"""

    def __init__(self):
        super().__init__([0, 0, 0], tps, 0, None)

    def attack(self, units):
        """attacking the enemy with self.damage"""
        enemy = self.getTarget(units)
        if enemy is None:
            return
        enemy.getDamage(self.damage[self.lvl])
        enemy.light()
        # todo: flying bullet


class SlowingTower(Tower):
    """Firing tower"""

    def __init__(self):
        super().__init__([0, 0, 0], tps // 2, 0, None)

    def attack(self, units):
        """attacking the enemy with self.damage"""
        enemy = self.getTarget(units)
        if enemy is None:
            return
        enemy.getDamage(self.damage[self.lvl])
        enemy.slow_down()
        # todo: flying bullet


class StandartTower(Tower):
    """Standart tower"""

    def __init__(self):
        super().__init__([0, 0, 0], tps, 0, None)


class TowerFactory:
    def generateTower(self):
        return None


class FireTowerFactory(TowerFactory):
    def generateTower(self):
        return FireTower()


class SlowingTowerFactory(TowerFactory):
    def generateTower(self):
        return SlowingTower()

class StandartTowerFactory(TowerFactory):
    def generateTower(self):
        return StandartTower()