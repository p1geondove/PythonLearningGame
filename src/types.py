from .units.bullet import Bullet
from .units.cupta import Cupta
from .units.hazard import Hazard
from .units.player import Player
from .units.putler import Putler
from .units.seeker import Seeker
from .units.token import Token
from .units.tail import Tail
from .units.troll import Troll

NON_COLLIDE_TYPE = {
    (Tail, Bullet),
    (Tail, Player),
    (Tail, Tail),
    (Tail, Token),
    (Bullet, Tail),
    (Player, Tail),
    (Token, Tail),
}

SPAWN_TYPE = [Token, Hazard, Seeker, Troll, Putler, Cupta]
