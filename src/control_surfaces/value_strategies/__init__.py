"""
control_surfaces > value_strategies

Contains definitions for value strategies, as well as the IValueStrategy
interface.

Authors:
* Maddy Guthridge [hello@maddyguthridge.com, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""

__all__ = [
    'IValueStrategy',
    'NoteStrategy',
    'Data2Strategy',
    'Data1Strategy',
    'TwosComplimentDeltaStrategy',
    'ButtonData2Strategy',
    'ButtonSinglePressStrategy',
    'ForwardedStrategy',
    'ForwardedUnionStrategy',
    'NullStrategy',
    'AkaiJoystickFullStrategy',
    'Lk4RelativeStrategy',
]

from .akai_joystick_full_strategy import AkaiJoystickFullStrategy
from .button_data2_strategy import ButtonData2Strategy
from .button_single_press_strategy import ButtonSinglePressStrategy
from .data_strategy import Data1Strategy, Data2Strategy
from .forwarded_strategy import ForwardedStrategy, ForwardedUnionStrategy
from .note_strategy import NoteStrategy
from .null_strategy import NullStrategy
from .twos_compliment_delta import TwosComplimentDeltaStrategy
from .value_strategy import IValueStrategy
from .lk4_relative_strategy import Lk4RelativeStrategy
