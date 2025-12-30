"""
devices > novation > launchkey > incontrol > controls > navigation

Authors:
* Maddy Guthridge [hello@maddyguthridge.com, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""
__all__ = [
    'LkMk2DirectionNext',
    'LkMk2DirectionPrevious',
    'Mk3DirectionLeft',
    'Mk3DirectionRight',
    'MiniMk3DirectionUp',
    'MiniMk3DirectionDown',
    'Mk3DirectionUp',
    'Mk3DirectionDown',
    'Mk3DirectionUpSilenced',
    'Mk3DirectionDownSilenced',
    'Mk4DirectionLeft',
    'Mk4DirectionRight',
    'MiniMk4DirectionLeft',
    'MiniMk4DirectionRight',
    'MiniMk4DirectionUp',
    'MiniMk4DirectionDown',
    'Mk4DirectionUp',
    'Mk4DirectionDown',
    'Mk4DirectionUpSilenced',
    'Mk4DirectionDownSilenced',
]

from .mk2 import (
    LkMk2DirectionNext,
    LkMk2DirectionPrevious,
)
from .mk3 import (
    MiniMk3DirectionDown,
    MiniMk3DirectionUp,
    Mk3DirectionDown,
    Mk3DirectionDownSilenced,
    Mk3DirectionLeft,
    Mk3DirectionRight,
    Mk3DirectionUp,
    Mk3DirectionUpSilenced,
)
from .mk4 import (
    MiniMk4DirectionDown,
    MiniMk4DirectionUp,
    MiniMk4DirectionLeft,
    MiniMk4DirectionRight,
    Mk4DirectionDown,
    Mk4DirectionDownSilenced,
    Mk4DirectionLeft,
    Mk4DirectionRight,
    Mk4DirectionUp,
    Mk4DirectionUpSilenced,
)
