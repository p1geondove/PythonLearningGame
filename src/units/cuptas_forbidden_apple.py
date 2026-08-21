import random
from time import sleep

import pygame
from pygame import Vector2, Surface

from ..utils import random_position
from ..globals import Globals
from ..const import Colors, Sizes
from ..var import Units
from .cupta import Cupta
from .player import Player
from .troll import Troll
from .unit import Unit

class CuptasForbiddenApple(Unit):
    image = pygame.image.load("assets/cupta.png")

    def __init__(self, *args, **kwargs):
        super().__init__(
            color = Colors.cuptas_apple,
            radius = Sizes.cuptas_apple_radius,
            line_width = Sizes.cuptas_apple_line_width,
            attack = 0,
            hit_points = Sizes.cuptas_apple_hit_points,
            *args, **kwargs
        )
        self.speed = Vector2(1,0).rotate(random.random()*360) * Sizes.cuptas_apple_speed
        self.collected = False

    def step(self):
        super().step()

    def collision(self, other:Player|Troll|Cupta):
        if isinstance(other, Player):
            print("Cupta's ancient powers course through your veins. You are healed.")
            Globals.player.hitpoints += Sizes.cuptas_apple_heal_amount
            self.collected = True
        elif isinstance(other, Troll):
            print("Oh no! Cupta's dark magic have been bestowed upon the troll!")
            for _ in range(Sizes.cuptas_apple_troll_spawn_amount):
                Units.units.append(Troll(position=random_position(away_from=Globals.player.get_position())))
            self.collected = True
        elif isinstance(other, Cupta):
            print("Cupta devours the apple and laughs. His veins glow purple and his eyes become a deep black. For millenia he waited in the caverns beneath the Earth for his powers to return, and you let him. He stares at you intently for several seconds then pounces. In a fraction of a second his fangs are slicing through your flesh. You feel them drain your life. You lose.")
            self.collected = True
            Globals.player.hitpoints = -float("inf")
            sleep(3)

    def draw(self, surface:Surface):
        surface.blit(
            CuptasForbiddenApple.image,
            (self.position.elementwise() - 32, (64,64)),
            (0, 192, 64, 64)
        )

    def is_alive(self):
        return not self.collected
