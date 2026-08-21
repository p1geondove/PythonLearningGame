from random import random, uniform

from pygame import Vector2

from .globals import Globals

def random_vector_rectangle(width:int|float, height:int|float):
    return Vector2(random()*width, random()*height)

def random_display_position(margin:int|float=20):
    width, height = Globals.display.get_size()
    return random_vector_rectangle(width - 2 * margin, height - 2 * margin).elementwise() + margin

def random_vector_circle(min_radius:int|float, max_radius:int|float):
    return Vector2(uniform(min_radius, max_radius),).rotate(random()*360)

def random_position(away_from:Vector2, distance:int|float=200, margin:int|float=20, tries:int=50):
    delta = random_vector_circle(distance, distance)
    return away_from + delta
