import random

import pygame
from pygame import Vector2, Rect

from .globals import Globals
from .var import Units, Animations, Variables
from .const import Colors, Sizes
from .types import *
from .animations.explosion import Explosion
from .utils import random_position, random_vector_circle

class Game:
    def __init__(self):
        self.running = True
        pygame.display.set_caption('PythonLearningGame')
        self.frames_per_second = 60
        Globals.player = Player()
        Units.units.append(Globals.player)
        for _ in range(Sizes.player_tail_length):
            Globals.player.add_tail() # start with tail of 10 segments
        self.mouse_buttons_down = {}

    def spawn_units(self):
        for spawn_type in SPAWN_TYPE:
            if spawn_type.count < spawn_type.max_count:
                if random.random() < spawn_type.spawn_chance:
                    position = random_position(away_from=Globals.player.get_position())
                    if position is not None:  # only if valid position found
                        if spawn_type is Cupta:
                            speed = Vector2(0, -random.randint(Sizes.cupta_speed_min, Sizes.cupta_speed_max))
                        else:
                            speed = random_vector_circle(1, 3)
                        unit = spawn_type(position=position, speed=speed)
                        Units.units.append(unit)

    def handle_events(self):
        for event in pygame.event.get():  # handle events
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    def does_collide(self, unit1, unit2):
        return (type(unit1), type(unit2)) not in NON_COLLIDE_TYPE

    def collision(self, unit1, unit2):
        # Switched to elastic collision response based on https://en.wikipedia.org/wiki/Elastic_collision
        # first compute the normal vector between the two units
        delta = unit1.get_position() - unit2.get_position()
        normal = delta.normalize()
        # compute the relative speed along the normal
        relative_speed = unit1.speed - unit2.speed
        velocity_along_normal = relative_speed.dot(normal)
        mass1 = unit1.radius  # mass proportional to radius looks better than area (radius**2)
        mass2 = unit2.radius
        # compute impulse using the formula for elastic collisions
        impulse_strength = -(2 * velocity_along_normal) / ((1 / mass1) + (1 / mass2))
        impulse = normal * impulse_strength
        # apply impulse to the units' speeds
        unit1.speed += impulse / mass1
        unit2.speed -= impulse / mass2

    def step_units(self):
        for unit in Units.units:
            pos_old = unit.get_position().copy() # when colliding, we will revert to this position
            unit.step()
            for other in Units.units:
                if unit is other: continue # don't collide with self
                square_distance = (unit.get_position() - other.get_position()).length_squared()
                square_radius_sum = (unit.radius + other.radius) ** 2
                if square_distance < square_radius_sum:
                    if self.does_collide(unit, other):  # test if units should collide
                        self.collision(unit, other)  # Handle collision
                        unit.set_position(pos_old)
                        unit.collision(other)
                        other.collision(unit)
            unit.collide_display_border()

    def kill_dead_units(self):
        if Globals.player.hitpoints <= 0:
            self.running = False
        alive_units = []
        for unit in Units.units:
            if unit.is_alive():
                alive_units.append(unit)
            else:
                unit.dies()
                expl = Explosion(radius = unit.radius,
                                color = unit.color,
                                position = unit.get_position())
                Animations.animations.append(expl)
        Units.units = alive_units

    def draw_units(self):
        for unit in Units.units:
            unit.draw(Globals.display)

    def draw_panel(self):
        width = Globals.display.get_width() - 2 * Sizes.bar_margin_x
        health_percent = min(1,max(0,Globals.player.hitpoints / Player.initial_hitpoints))
        token_percent = min(1,max(0,Globals.player.token_count / Variables.win_token_count))
        rect_health = Rect(Sizes.bar_margin_x, Sizes.bar_margin_y, width * health_percent, Sizes.bar_width)
        rect_token = Rect(Sizes.bar_margin_x, Sizes.bar_margin_y * 3, width * token_percent, Sizes.bar_width)
        rect_cap_left = Rect(Sizes.bar_margin_x - Sizes.bar_width, Sizes.bar_margin_y, Sizes.bar_width, Sizes.bar_width * 3)
        rect_cap_right = Rect(Globals.display.get_width() - Sizes.bar_margin_x, Sizes.bar_margin_y, Sizes.bar_width, Sizes.bar_width * 3)
        pygame.draw.rect(Globals.display, Colors.health_bar, rect_health)
        pygame.draw.rect(Globals.display, Colors.token_bar, rect_token)
        pygame.draw.rect(Globals.display, Colors.bar_caps, rect_cap_left)
        pygame.draw.rect(Globals.display, Colors.bar_caps, rect_cap_right)

    def test_win(self):
        return Globals.player.token_count >= Variables.win_token_count

    def step_animations(self):
        for animation in Animations.animations:
            animation.step()

    def draw_animations(self):
        for animation in Animations.animations:
            animation.draw(Globals.display)

    def remove_animations(self):
        Animations.animations = [animation for animation in Animations.animations if animation.is_running()]

    def start(self):
        print("Game Started")
        print("- use cursor or WASD or ZX/' keys to move")
        print("- catch green tokens to gain points")
        print("- avoid red hazards to stay alive")
        print("- avoid blue seekers that chase you")
        print("- press SPACE or RETURN to shoot bullets")
        clock = pygame.time.Clock()

        self.running = True
        while self.running:
            Globals.display.fill(Colors.background) # clear display

            self.spawn_units()
            keys = pygame.key.get_pressed()
            Globals.player.handle_keys(keys)
            self.handle_events()
            self.step_units()
            self.draw_panel()
            self.draw_units()
            self.step_animations()
            self.draw_animations()
            self.kill_dead_units()
            self.remove_animations()
            if self.test_win():
                print("You Win!")
                self.running = False

            pygame.display.flip() # draw everything to the display
            clock.tick(self.frames_per_second)
        print("Game Over")
