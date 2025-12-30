"""
devices > novation > launchkey > incontrol > controls

Definitions for controls shared between Novation Launchkey devices

Authors:
* Maddy Guthridge [hello@maddyguthridge.com, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""

__all__ = [
    'ColorInControlSurface',
    'GrayscaleInControlSurface',
    'LkMk2DirectionNext',
    'LkMk2DirectionPrevious',
    'LkFastForwardButton',
    'LkMk2LoopButton',
    'LkMk3LoopButton',
    'LkMk2StopButton',
    'LkMk3StopButton',
    'LkMk2PlayButton',
    'LkMk3PlayButton',
    'LkMk2RecordButton',
    'LkMk3RecordButton',
    'LkRecordButton',
    'LkRewindButton',
    'LkMk2DrumPad',
    'LkMk3DrumPad',
    'LkDrumPadMatcher',
    'LkMk2Fader',
    'LkMk2MasterFader',
    'LkMk2FaderButton',
    'LkMk2MasterFaderButton',
    'LkMk2FaderSet',
    'LkMk3Fader',
    'LkMk3MasterFader',
    'LkMk3FaderButton',
    'LkMk3FaderSet',
    'LkKnob',
    'LkKnobSet',
    'LkEncoder',
    'LkEncoderSet',
    'LkMk2MetronomeButton',
    'LkMk3MetronomeButton',
    'LkMk2ControlSwitchButton',
    'LkMk3ControlSwitchButton',
    'LkMk3CaptureMidiButton',
    'LkQuantizeButton',
    'LkUndoRedoButton',
    'Mk3DirectionLeft',
    'Mk3DirectionRight',
    'MiniMk3DirectionUp',
    'MiniMk3DirectionDown',
    'Mk3DirectionUp',
    'Mk3DirectionDown',
    'Mk3DirectionUpSilenced',
    'Mk3DirectionDownSilenced',
    'StopSoloMuteButton',
    'LkMk3DrumPadMute',
    'LkMk3DrumPadSolo',
    'LkMk3DrumPadActivity',
    'LkMk3MiniDrumPadActivity',
    'LkPauseActive',
    'LkDeviceSelect',
]

from .activity import LkDeviceSelect, LkPauseActive
from .control_switch import (
    LkMk2ControlSwitchButton,
    LkMk3ControlSwitchButton,
)
from .drum_pad import (
    LkDrumPadMatcher,
    LkMk2DrumPad,
    LkMk3DrumPad,
    LkMk3DrumPadActivity,
    LkMk3DrumPadMute,
    LkMk3DrumPadSolo,
    LkMk3MiniDrumPadActivity,
)
from .faders import (
    LkMk2Fader,
    LkMk2FaderButton,
    LkMk2FaderSet,
    LkMk2MasterFader,
    LkMk2MasterFaderButton,
    LkMk3Fader,
    LkMk3FaderButton,
    LkMk3FaderSet,
    LkMk3MasterFader,
)
from .incontrol_surface import ColorInControlSurface, GrayscaleInControlSurface
from .knob import (
    LkKnob,
    LkKnobSet,
)
from .encoder import (
    LkEncoder,
    LkEncoderSet,
)
from .metronome import (
    LkMk2MetronomeButton,
    LkMk3MetronomeButton,
)
from .mutes import (
    StopSoloMuteButton,
)
from .navigation import (
    LkMk2DirectionNext,
    LkMk2DirectionPrevious,
    MiniMk3DirectionDown,
    MiniMk3DirectionUp,
    Mk3DirectionDown,
    Mk3DirectionDownSilenced,
    Mk3DirectionLeft,
    Mk3DirectionRight,
    Mk3DirectionUp,
    Mk3DirectionUpSilenced,
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
from .transport import (
    LkFastForwardButton,
    LkMk2LoopButton,
    LkMk2PlayButton,
    LkMk2RecordButton,
    LkMk2StopButton,
    LkMk3CaptureMidiButton,
    LkMk3LoopButton,
    LkMk3PlayButton,
    LkMk3RecordButton,
    LkMk3StopButton,
    LkQuantizeButton,
    LkRewindButton,
    LkUndoRedoButton,
)
