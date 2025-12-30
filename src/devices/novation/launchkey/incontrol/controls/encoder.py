"""
devices > novation > launchkey > incontrol > controls > encoder

Definitions for encoder controls shared between Launchkey Mk4 devices

Authors:
* Maddy Guthridge [hello@maddyguthridge.com, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""

from control_surfaces import Encoder
from control_surfaces.event_patterns import BasicPattern, ForwardedPattern
from control_surfaces.matchers import IndexedMatcher
from control_surfaces.value_strategies import (
    Data2Strategy,
    ForwardedStrategy,
)

__all__ = [
    'LkEncoder',
    'LkEncoderSet',
]

# Fader start
E_START = 0x15

        
class LkEncoder(Encoder):
    def __init__(self, index: int) -> None:
        super().__init__(
            ForwardedPattern(2, BasicPattern(0xBF, E_START + index, ...)),
            ForwardedStrategy(Data2Strategy()),
            (0, index)
        )


class LkEncoderSet(IndexedMatcher):
    def __init__(self) -> None:
        super().__init__(0xBF, E_START, [
            LkEncoder(i) for i in range(8)
        ], 2)
