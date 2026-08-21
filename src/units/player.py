import random

import pygame
from pygame import Vector2

from ..var import Units
from ..const import Colors, Sizes
from ..utils import random_display_position
from .unit import Unit
from .token import Token
from .bullet import Bullet
from .tail import Tail

class Player(Unit):
    def __init__(self, *args, **kwargs):
        super().__init__(
            color = Colors.player,
            radius = Sizes.player_radius,
            line_width = Sizes.player_line_width,
            speed = Vector2(),
            position = random_display_position(),
            *args, **kwargs
        )

        self.direction = Vector2()
        self.token_count = 0
        self.last_shot_time = 0
        self.last_tail = self

    def handle_keys(self, keys):
        acceleration = 0.5
        rotate_speed = 4  # degrees per frame
        if keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_z]:
            self.direction.rotate_ip(-rotate_speed)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_x]:
            self.direction.rotate_ip(rotate_speed)
        if keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_QUOTE]:
            self.speed += self.direction * acceleration
        if keys[pygame.K_DOWN] or keys[pygame.K_s] or keys[pygame.K_SLASH]:
            self.speed -= (self.direction/2) * acceleration
        if pygame.mouse.get_pressed()[0] or keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
            self.shoot()

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time < Sizes.player_bullet_cooldown:  # ms between shots
            return  # too soon to shoot again
        bullet_speed = Sizes.player_bullet_speed
        bullet_position = self.get_position() + self.direction * (self.radius * 1.5)  # spawn bullet just outside the player
        gaus = random.gauss(0, 2)  # small random angle for bullet spread
        direction = self.direction.rotate(gaus)
        bullet_speed = direction * bullet_speed
        Units.units.append(Bullet(position=bullet_position, speed=bullet_speed))
        self.last_shot_time = pygame.time.get_ticks()  # update last shot time

    def step(self):
        if pygame.mouse.get_focused():  # if mouse is on screen
            mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
            self.direction = mouse_pos - self.position
            self.direction.normalize_ip()
        super().step()      # normal step behavior super class Unit
        self.speed *= Sizes.player_friction

    def draw(self, surface):
        super().draw(surface)  # normal draw behavior super class Unit
        end_pos = self.position + self.direction * (self.radius * 1.5)
        pygame.draw.line(surface, Colors.player_line, self.position, end_pos, self.line_width)

    def add_tail(self):
        prev_tail = self.last_tail
        self.last_tail = Tail(prev=None,
                    next=self.last_tail,
                    direction=self.direction.copy(),
                    position=self.last_tail.position - 
                       self.last_tail.direction * (self.last_tail.radius * 2),
                    speed=self.speed.copy(), # whatever the tail implementation is, im not fixing that ... -p1geon
                    )
        if prev_tail is not self:
            prev_tail.prev = self.last_tail 
        Units.units.append(self.last_tail)

    def collision(self, other):
        if isinstance(other, Token):  # special collision behavior for Token
            self.token_count += 1
            other.hitpoints = -1  # destroy the token
            print('token_count:', self.token_count)
            self.add_tail()
        else:
            super().collision(other)  # normal collision behavior super class Unit
            print('hitpoints:', self.hitpoints)

