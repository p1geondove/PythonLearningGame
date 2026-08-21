from ..const import Colors, Sizes
from .unit import Unit

class Bullet(Unit):
    def __init__(self, *args, **kwargs):
        super().__init__(
            color = Colors.bullet,
            radius = Sizes.bullet_radius,
            line_width = 0,
            attack = Sizes.bullet_attack,
            hit_points = Sizes.bullet_hit_points,
            *args, **kwargs
        )

    def collide_border(self):
        self.hitpoints = -1  # destroy the bullet when it hits a border
