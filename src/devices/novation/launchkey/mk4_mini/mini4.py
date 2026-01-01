"""
devices > novation > launchkey > mk2 > launchkey

Device definitions for Launchkey Mk2 controllers

Authors:
* Maddy Guthridge [hello@maddyguthridge.com, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""

from typing import Optional

import device
from fl_classes import FlMidiMsg

from common.extension_manager import ExtensionManager
from control_surfaces import (
    StandardModWheel,
    StandardPitchWheel,
    SustainPedal,
)
from control_surfaces.event_patterns import BasicPattern
from control_surfaces.matchers import BasicControlMatcher, NoteMatcher
from devices.device import Device
from devices.novation.launchkey.incontrol import (
    InControl,
    InControlMatcher,
)
from devices.novation.launchkey.incontrol.controls import (
    LkEncoderSet,
)

from .shift import getShiftControls

DEVICE_ID = "Novation.Launchkey.Mk4.Mini"


class LaunchkeyMiniMk4(Device):
    """
    Novation Launchkey Mk4 Mini
    """

    def __init__(self) -> None:
        matcher = BasicControlMatcher()
        # InControl manager
        self._incontrol = InControl(matcher)
        matcher.addSubMatcher(InControlMatcher(self._incontrol))

        # Notes
        matcher.addSubMatcher(NoteMatcher())

        matcher.addSubMatcher(LkEncoderSet())
        # matcher.addControl(LkMk3PlayButton())
        matcher.addControl(StandardPitchWheel.create())
        matcher.addControl(StandardModWheel.create())
        matcher.addControl(SustainPedal.create())

        # Shift controls
        matcher.addSubMatcher(getShiftControls())
        super().__init__(matcher)

    def initialize(self) -> None:
        self._incontrol.enable()

    def deinitialize(self) -> None:
        self._incontrol.enable()

    @classmethod
    def getDrumPadSize(cls) -> tuple[int, int]:
        return 2, 8

    def getDeviceNumber(self) -> int:
        if (
            'MIDIIN2' in device.getName()
            or 'DAW' in device.getName()
        ):
            return 2
        else:
            return 1
        
    @classmethod
    def matchDeviceName(self, arg) -> bool:
        if('Launchkey Mini MK4' in arg):
            return True
        else:
            return False

    @classmethod
    def create(
        cls,
        event: Optional[FlMidiMsg] = None,
        id: Optional[str] = None,
    ) -> 'Device':
        return cls()

    def getId(self) -> str:
        return DEVICE_ID

    @classmethod
    def getSupportedIds(cls) -> tuple[str, ...]:
        return (DEVICE_ID,)

    @classmethod
    def getUniversalEnquiryResponsePattern(cls):
        return BasicPattern([
                0xF0,  # Sysex start
                0x7E,  # Device response
                ...,  # OS Device ID
                0x06,  # Separator
                0x02,  # Separator
                0x00,  # Manufacturer
                0x20,  # Manufacturer
                0x29,  # Manufacturer
                0x41,  # Family code
                0x01,
                0x00,
                ...,  # MIDI in 1 or 2
                0x01,
                0x01,
                0x0B,
                0x06,
                0xF7,
            ]) 
        

# Register devices
ExtensionManager.devices.register(LaunchkeyMiniMk4)
