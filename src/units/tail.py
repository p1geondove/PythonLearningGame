from __future__ import annotations

from ..globals import Globals
from ..const import Colors, Sizes
from .unit import Unit

class Tail(Unit):
    spawn_chance = Sizes.tail_spawn_chance
    count = 0
    max_count = Sizes.tail_max_count

    def __init__(self, direction, prev:Tail|None=None, next:Tail|None=None, *args, **kwargs):
        super().__init__(
            color = Colors.tail,
            radius = Sizes.tail_radius,
            line_width = Sizes.tail_line_width,
            attack = Sizes.tail_attack,
            hit_points = Sizes.tail_hit_points,
            *args, **kwargs,
        )
        self.direction = direction
        self.prev = prev
        self.next = next
        Tail.count += 1

    def __del__(self):
        Tail.count -= 1

    def step(self):
        super().step()  # normal step behavior super class Unit
        if self.next:
            self.direction = self.next.get_position() - self.get_position()
            dist = self.direction.length()
            if dist == 0:
                return
            self.direction.normalize_ip()
            sum_radius = self.radius + self.next.radius
            min_dist = sum_radius * Sizes.tail_min_dist_factor
            accel_dist = sum_radius * Sizes.tail_accel_dist_factor
            max_dist = sum_radius * Sizes.tail_max_dist_factor
            if dist < min_dist:
                delta = dist - min_dist
                self.position += self.direction * delta
            else:
                if dist > accel_dist:
                    self.speed += self.direction * Sizes.tail_accel
                if dist > max_dist:
                    delta = dist - max_dist
                    self.position += self.direction * delta
        self.speed *= Sizes.tail_friction  # apply friction to slow down the tail over time

    def dies(self):
        if self is Globals.player.last_tail:
            Globals.player.last_tail = self.next
        if self.prev:
            self.prev.next = self.next
        if self.next is not Globals.player:  # only update next.prev if next is not the player
            self.next.prev = self.prev # what in the ever living fuck is going on here??? -p1geon
