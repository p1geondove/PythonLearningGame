from typing import TYPE_CHECKING
from dataclasses import dataclass

import pygame
from pygame import Vector2, Surface

if TYPE_CHECKING: # this is usually not how you wanna do this, but it kinda works
    from .units.player import Player
    @dataclass
    class _Globals:
        display:Surface = pygame.display.set_mode((800, 600), pygame.RESIZABLE) # the only surface, should make some more, display doesnt have alpha
        player:Player = Player(position = Vector2(400,300), speed=Vector2())
else:
    @dataclass
    class _Globals:
        display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        player = None

Globals = _Globals()
