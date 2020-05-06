class Cell:
    """tower zone"""
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.filled = False

    def in_cell(self, x, y):
        if self.filled:
            return False
        if (x >= self.x1) and (x <= self.x2) and (y >= self.y1) and (y <= self.y2):
            return self.x1, self.y1
