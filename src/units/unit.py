import pygame
from pygame import Vector2, Color

from ..const import Sizes
from ..globals import Globals

class Unit:
    spawn_change = None
    count = None
    max_count = None
    initial_hitpoints = Sizes.unit_initial_hit_points

    def __init__(self,
                 color:Color,
                 position:Vector2,
                 speed:Vector2,
                 radius = Sizes.unit_radius,
                 line_width = Sizes.unit_line_width,
                 hit_points = Sizes.unit_hitpoints,
                 attack = Sizes.unit_attack
                 ):
        self.radius = radius
        self.color = color
        self.line_width = line_width
        self.position = position
        self.speed = speed
        self.hitpoints = hit_points
        self.attack = attack

    def step(self):
        self.position += self.speed

    def collide_border(self):
        pass

    def collide_display_border(self):
        width, height = Globals.display.get_size()
        if self.position.x - self.radius < 0:
            self.position.x = self.radius
            self.speed.x *= -1
            self.collide_border()
        elif self.position.x + self.radius > width:
            self.position.x = width - self.radius
            self.speed.x *= -1
            self.collide_border()
        if self.position.y - self.radius < 0:
            self.position.y = self.radius
            self.speed.y *= -1
            self.collide_border()
        elif self.position.y + self.radius > height:
            self.position.y = height - self.radius
            self.speed.y *= -1
            self.collide_border()

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def collision(self, other):
        self.hitpoints -= other.attack

    def is_alive(self):
        return self.hitpoints > 0

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius, self.line_width)

    def dies(self):
        pass
