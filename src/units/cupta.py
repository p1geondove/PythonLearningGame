import random

import pygame
from pygame import Rect

from ..globals import Globals
from ..utils import random_display_position
from ..const import Colors, Sizes
from .unit import Unit

SPRITE_WIDTH = 64
SPRITE_HEIGHT = 64

def get_sprite(row, col):
    return Rect(col * SPRITE_WIDTH, row * SPRITE_HEIGHT, SPRITE_WIDTH, SPRITE_HEIGHT)

class Cupta(Unit):
    spawn_chance = 1
    count = 0
    max_count = 1
    image = pygame.image.load("assets/cupta.png")
    # cupta_health_lost_until_death = 600

    HEAD = get_sprite(0, 3)
    BODY_STRAIGHT = get_sprite(1, 2)
    TAIL = get_sprite(2, 3)


    def __init__(self, *args, **kwargs):
        super().__init__(
            color = Colors.cupta,
            radius = 1,
            line_width = 1,
            attack = Sizes.cupta_attack,
            hit_points = Sizes.cupta_hit_points,
            *args, **kwargs
        )

        Cupta.count += 1
        print('CUPTA HAS ARRIVED')
        self.position.y = 2000
        pos = random_display_position(0)
        self.x = pos.x
        self.cupta_snake_parts = [self.HEAD]
        for _ in range(random.randint(Sizes.cupta_length_min, Sizes.cupta_length_max)):
            self.cupta_snake_parts.append(self.BODY_STRAIGHT)

        self.cupta_snake_parts.append(self.TAIL)

    def __del__(self):
        Cupta.count -= 1
        Globals.player.token_count += Sizes.cupta_token_surplus

    def step(self):
        super().step()
        self.position.x = self.x
        cupta_snake_rectangle_collision_shape_box = Rect(
            self.position.x,
            self.position.y,
            SPRITE_WIDTH,
            SPRITE_HEIGHT * len(self.cupta_snake_parts)
        )
        player_pos = Globals.player.get_position()
        player_rectangle_collision_shape_box = Rect(player_pos.x, player_pos.y, Globals.player.radius, Globals.player.radius)

        if cupta_snake_rectangle_collision_shape_box.colliderect(player_rectangle_collision_shape_box):
            print('Cupta has begun siphoning your life essence.')
        

    def draw(self, surface: pygame.Surface):
        for i, part in enumerate(self.cupta_snake_parts):
            dst = self.position.copy()
            dst.y += i * SPRITE_HEIGHT
            surface.blit(Cupta.image, dst, part)

    def collide_display_border(self):
        if self.position.y + SPRITE_HEIGHT * len(self.cupta_snake_parts) < -30:
            pos = random_display_position(0)
            self.position.y = 2000
            self.position.x = pos.x
            self.x = pos.x
