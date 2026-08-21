from dataclasses import dataclass

@dataclass
class _Units:
    units = []

@dataclass
class _Variables:
    win_token_count = 20

@dataclass
class _Animations:
    animations = []

Units = _Units()
Variables = _Variables()
Animations = _Animations()
