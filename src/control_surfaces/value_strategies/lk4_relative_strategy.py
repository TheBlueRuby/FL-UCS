"""
control_surfaces > value_strategies > lk4_relative_strategy

Contains the definitions for Launchkey Mk4 relative encoder value strategies

Authors:
* Maddy Guthridge [hello@maddyguthridge.com, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""
from fl_classes import FlMidiMsg, isMidiMsgStandard

from common.util.misc import clamp

from . import IValueStrategy


class Lk4RelativeStrategy(IValueStrategy):
    """
    Defines a value strategy that uses 0x40 as a center for a pivot,
    using the data2 property of events
    This is used by the Launchkey Mk4 endless encoders.
    """
    def __init__(self, scaling: float = 1.0) -> None:
        """
        Create a Lk4RelativeStrategy

        ### Args:
        * `scaling` (`float`, optional): amount to scale delta by. Defaults to
          `1.0`.
        """
        self.__scaling = scaling

    def getValueFromEvent(self, event: FlMidiMsg, value: float) -> float:
        assert isMidiMsgStandard(event)
        event.inEv = event.data2
        
        event.outEv = event.inEv - 0x40
        # 0-63 are right turns; 65-127 is a left turn
        delta = event.outEv / 64
        return clamp(delta * self.__scaling + value, 0.0, 1.0)

    def getChannelFromEvent(self, event: FlMidiMsg) -> int:
        assert isMidiMsgStandard(event)
        return event.status & 0xF
