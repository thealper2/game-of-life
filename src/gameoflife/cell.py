class Cell:
    def __init__(self, x: int, y: int, alive: bool = False):
        self.alive = alive
        self.next_state = alive
        self.x = x
        self.y = y