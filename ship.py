class Ship:
    def __init__(self, size, x, y, rotation):
        self.size = size
        self.x = x
        self.y = y
        self.rotation = rotation

    def set_position(self, x, y, rotation):
        self.x = x
        self.y = y
        self.rotation = rotation
