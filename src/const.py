from dataclasses import dataclass

from pygame import Color

@dataclass
class Colors:
    background = Color("grey10")
    bar_caps = Color("grey50")
    bullet = Color("white")
    cupta = Color("green")
    cuptas_apple = Color("blue")
    explosion = Color("red")
    hazard = Color("red")
    health_bar = Color("red")
    player = Color("grey80")
    player_line = Color("white")
    putler = Color("green")
    putler_hole = Color("black")
    seeker = Color("blue")
    token = Color("green")
    token_bar = Color("green")
    troll = Color("green")
    tail = Color("white")
    unit = Color("green")

@dataclass
class Sizes:
    bar_margin_x = 20
    bar_margin_y = 4
    bar_width = bar_margin_y

    bullet_radius = 4
    bullet_attack = 9
    bullet_hit_points = 1

    cupta_attack = 2
    cupta_hit_points = 600
    cupta_length_min = 3
    cupta_length_max = 20
    cupta_token_surplus = 5 # how many tokens the player gest after cupta is gone
    cupta_speed_min = 6
    cupta_speed_max = 12

    cuptas_apple_speed = 3
    cuptas_apple_radius = 32
    cuptas_apple_line_width = 8
    cuptas_apple_hit_points = 40
    cuptas_apple_heal_amount = 100
    cuptas_apple_troll_spawn_amount = 17 # does this really mean that the apple spwans 17 troll when it touches a troll?? wtf...

    explosion_radius_start = 20
    explosion_radius_max = explosion_radius_start * 8
    explosion_growth_rate = 7
    explosion_color_step = 0.2
    explosion_line_width = 2

    hazard_spawn_chance = 0.01
    hazard_max_count = 6
    hazard_radius = 12
    hazard_line_width = 3
    hazard_attack = 25

    player_radius = 20
    player_line_width = 6
    player_hitpoints = 100
    player_tail_length = 10
    player_bullet_cooldown = 100 # in ms
    player_bullet_speed = 12
    player_friction = 0.94

    putler_spawn_chance = 0.0005
    putler_attack = 1
    putler_hit_points = 300
    putler_hole_size = 7

    seeker_spawn_chance = 0.002
    seeker_max_count = 3
    seeker_radius = 14
    seeker_line_width = 8
    seeker_attack = 15
    seeker_hit_points = 40
    seeker_accel = 0.15
    seeker_friction = 0.95

    tail_spawn_chance = 0.005
    tail_max_count = 3
    tail_radius = 10
    tail_line_width = 2
    tail_attack = 30
    tail_hit_points = 40
    tail_min_dist_factor = 1.1
    tail_accel_dist_factor = 1.3
    tail_max_dist_factor = 1.5
    tail_accel = 0.3
    tail_friction = 0.96

    token_spwan_chance = 0.005
    token_max_count = 3
    token_radius = 10
    token_line_width = 2

    troll_spwan_chance = 0.0005
    troll_max_count = 1
    troll_attack = 999999
    troll_hit_points = 400
    troll_token_surplus = 5 # amount of tokens the player gets when defeated
    troll_accel_min = -.1
    troll_accel_max = .3
    troll_accel_probability = 30 # meaning 1/30 chance to accelerate
    troll_friction = 0.95

    unit_radius = 10     # these are just the base units standard variables,
    unit_line_width = 2  # usually every subclass overwrites these values
    unit_attack = 10
    unit_hitpoints = 100
    unit_initial_hit_points = 100
