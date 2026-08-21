from pygame import Surface, Vector2, Color

class Animation:
    def __init__(self, radius:int, color:Color, position:Vector2):
        self.radius = radius
        self.color = color
        self.position = position

    def step(self):
        pass

    def is_running(self):
        return True

    def draw(self, surface:Surface):
        pass
