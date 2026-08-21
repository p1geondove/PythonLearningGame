from ..globals import Globals
from ..const import Colors, Sizes
from .unit import Unit

class Seeker(Unit):
    spawn_chance = Sizes.seeker_spawn_chance
    count = 0
    max_count = Sizes.seeker_max_count

    def __init__(self, *args, **kwargs):
        super().__init__(
            color = Colors.seeker,
            radius = Sizes.seeker_radius,
            line_width = Sizes.seeker_line_width,
            attack = Sizes.seeker_attack,
            hit_points = Sizes.seeker_hit_points,
            *args, **kwargs
        )
        Seeker.count += 1

    def __del__(self):
        Seeker.count -= 1

    def step(self):  # overwrite normal Unit step
        direction = Globals.player.get_position() - self.get_position()  # direction to player
        direction.normalize_ip()  # make direction vector length 1
        self.speed += direction * Sizes.seeker_accel  # accelerate towards player
        self.speed *= Sizes.seeker_friction  # add some friction
        super().step()  # do normal Unit step
