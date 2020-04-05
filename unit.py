from game import tps

basicDuration = 5
bossDuration = 3

basicDPT = 2
speedyDPT = 4
bossDPT = 1

basicSlowing = 0.7
fatSlowing = 0.5
bossSlowing = 0.8


class Unit():
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

    def simulate_tick(self):
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
            # todo: kill unit
            return
        # todo: screen_mooving & (x, y)_moving


class FastUnit(Unit):
    """Fast unit class, it fires well"""

    def __init__(self):
        super().__init__(0, 0, 0, None)

    def light(self):
        """if unit stroken by fire tower"""
        self.dDuration = basicDuration
        self.dpt = speedyDPT


class FatUnit(Unit):
    """Fat unit class, it freeze well"""

    def __init__(self):
        super().__init__(0, 0, 0, None)

    def slow_down(self):
        """if unit is stroken by slowing tower"""
        self.sDuration = basicDuration
        self.slowing = fatSlowing


class BossUnit(Unit):
    """Boss unit class, it fires and freeze bad"""

    def __init__(self):
        super().__init__(0, 0, 0, None)

    def light(self):
        """if unit stroken by fire tower"""
        self.dDuration = bossDuration
        self.dpt = bossDPT

    def slow_down(self):
        """if unit is stroken by slowing tower"""
        self.sDuration = bossDuration
        self.slowing = bossSlowing