"""
devices > novation > launchkey > incontrol > controls > knob

Definitions for knob controls shared between Launchkey devices

Authors:
* Maddy Guthridge [hello@maddyguthridge.com, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""

from control_surfaces import Knob
from control_surfaces.event_patterns import BasicPattern, ForwardedPattern
from control_surfaces.matchers import IndexedMatcher
from control_surfaces.value_strategies import (
    Data2Strategy,
    ForwardedStrategy,
)

__all__ = [
    'LkKnob',
    'LkKnobSet',
    'Lk4Knob',
    'Lk4KnobSet',
]

# Fader start
K_START = 0x15
K4_START = 0x15


class LkKnob(Knob):
    def __init__(self, index: int) -> None:
        super().__init__(
            ForwardedPattern(2, BasicPattern(0xBF, K_START + index, ...)),
            ForwardedStrategy(Data2Strategy()),
            (0, index)
        )


class LkKnobSet(IndexedMatcher):
    def __init__(self) -> None:
        super().__init__(0xBF, K_START, [
            LkKnob(i) for i in range(8)
        ], 2)
        
class Lk4Knob(Knob):
    def __init__(self, index: int) -> None:
        super().__init__(
            ForwardedPattern(2, BasicPattern(0xBF, K4_START + index, ...)),
            ForwardedStrategy(Data2Strategy()),
            (0, index)
        )


class Lk4KnobSet(IndexedMatcher):
    def __init__(self) -> None:
        super().__init__(0xBF, K4_START, [
            Lk4Knob(i) for i in range(8)
        ], 2)
