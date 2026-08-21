from ..const import Colors, Sizes
from .unit import Unit

class Token(Unit):
    spawn_chance = Sizes.token_spwan_chance
    count = 0
    max_count = Sizes.token_max_count

    def __init__(self, *args, **kwargs):
        super().__init__(
            color = Colors.token,
            radius = Sizes.token_radius,
            line_width = Sizes.token_line_width,
            *args, **kwargs
        )
        Token.count += 1

    def __del__(self):
        Token.count -= 1
