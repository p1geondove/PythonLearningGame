import pygame

from ..const import Colors, Sizes
from .animation import Animation

class Explosion(Animation):
    def __init__(self, radius=Sizes.explosion_radius_start, color=Colors.explosion, position=None):
        super().__init__(radius=radius, color=color, position=position)

    def step(self):
        self.radius += Sizes.explosion_growth_rate
        self.color = self.color.lerp(Colors.background, Sizes.explosion_color_step)

    def is_running(self):
        return self.radius < Sizes.explosion_radius_max

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius, Sizes.explosion_line_width)
