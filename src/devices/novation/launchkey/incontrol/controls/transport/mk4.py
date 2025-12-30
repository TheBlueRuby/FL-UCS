"""
devices > novation > launchkey > incontrol > controls > transport > mk4

Definitions for transport controls used by Launchkey Mk4 Launchkey devices

Authors:
* Maddy Guthridge [hello@maddyguthridge.com, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""

from control_surfaces import (
    CaptureMidiButton,
    LoopButton,
    PlayButton,
    RecordButton,
    StopButton,
)
from control_surfaces.event_patterns import BasicPattern, ForwardedPattern
from control_surfaces.value_strategies import (
    ButtonData2Strategy,
    ForwardedStrategy,
)

from ...colors.grayscale import COLORS
from ..incontrol_surface import GrayscaleInControlSurface

__all__ = [
    'LkMk4LoopButton',
    'LkMk4StopButton',
    'LkMk4PlayButton',
    'LkMk4RecordButton',
]


class LkMk4StopButton(StopButton):
    def __init__(self) -> None:
        val = 0x74
        StopButton.__init__(
            self,
            ForwardedPattern(2, BasicPattern(0xB0, val, ...)),
            ForwardedStrategy(ButtonData2Strategy()),
        )


class LkMk4LoopButton(LoopButton):
    def __init__(self) -> None:
        val = 0x76
        LoopButton.__init__(
            self,
            ForwardedPattern(2, BasicPattern(0xB0, val, ...)),
            ForwardedStrategy(ButtonData2Strategy()),
        )


class LkMk4PlayButton(PlayButton):
    def __init__(self) -> None:
        val = 0x73
        PlayButton.__init__(
            self,
            ForwardedPattern(2, BasicPattern(0xB0, val, ...)),
            ForwardedStrategy(ButtonData2Strategy()),
            color_manager=GrayscaleInControlSurface(
                0x0,
                val,
                COLORS,
                0xB,
            )
        )


class LkMk4RecordButton(RecordButton):
    def __init__(self) -> None:
        val = 0x75
        RecordButton.__init__(
            self,
            ForwardedPattern(2, BasicPattern(0xB0, val, ...)),
            ForwardedStrategy(ButtonData2Strategy()),
            color_manager=GrayscaleInControlSurface(
                0x0,
                val,
                COLORS,
                0xB,
            )
        )


class LkMk4CaptureMidiButton(CaptureMidiButton):
    def __init__(self) -> None:
        super().__init__(
            ForwardedPattern(2, BasicPattern(0xB0, 0x4A, ...)),
            ForwardedStrategy(ButtonData2Strategy()),
        )
