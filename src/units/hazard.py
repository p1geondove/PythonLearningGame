from ..const import Colors, Sizes
from .unit import Unit

class Hazard(Unit):
    spawn_chance = Sizes.hazard_spawn_chance
    count = 0
    max_count = Sizes.hazard_max_count

    def __init__(self, *args, **kwargs):
        super().__init__(
            color = Colors.hazard, 
            radius = Sizes.hazard_radius,
            line_width = Sizes.hazard_line_width,
            attack = Sizes.hazard_attack,
            *args, **kwargs
        )
        Hazard.count += 1

    def __del__(self):
        Hazard.count -= 1
