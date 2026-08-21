
import pygame
import random

from ..globals import Globals
from ..const import Colors, Sizes
from .unit import Unit

class Troll(Unit):
    spawn_chance = Sizes.troll_spwan_chance
    count = 0
    max_count = Sizes.troll_max_count
    image = pygame.image.load("assets/troll.png")

    def __init__(self, *args, **kwargs):
        width, height = Troll.image.get_size()
        super().__init__(
            color = Colors.troll,
            radius = (width+height)//4,
            line_width = 1,
            attack = Sizes.troll_attack,
            hit_points = Sizes.troll_hit_points,
            *args, **kwargs
        )
        self.randomize_acceleration()
        Troll.count += 1

    def __del__(self):
        Troll.count -= 1
        Globals.player.token_count += Sizes.troll_token_surplus

    def randomize_acceleration(self):
        self.acceleration = random.uniform(Sizes.troll_accel_min, Sizes.troll_accel_max)

    def step(self):
        if random.randint(1, Sizes.troll_accel_probability) == 1:
            self.randomize_acceleration()
        direction = Globals.player.get_position() - self.get_position()
        direction.normalize_ip()
        self.speed += direction * self.acceleration
        self.speed *= Sizes.troll_friction
        super().step()

    def draw(self, surface):
        dst = self.position.copy()
        width, height = Troll.image.get_size()
        dst.x -= width / 2
        dst.y -= height / 2
        surface.blit(Troll.image, dst)
