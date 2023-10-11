#!/usr/bin/env python3

__all__ = ["DM3058"]

class DM3058(object):
    """
    Rigol DM3058 or DM3058E command wrapper.
    """
    def __init__(self, inst):
        """
        Initialize the DM3058 wrapper with a specific PyVISA resource.
        This class does NOT open the resource, you have to open it for yourself!
        """
        self.inst = inst

    def read_voltage(self) -> float:
        """
        Read the current voltage measurement in volts        
        """
        volts_str = self.inst.query(':MEAS:VOLT:DC?')
        volts = float(volts_str.strip())
        return volts
    
    def set_speed(self, speed="M"):
        """
        Set the measurement speed.
        Valid values are:
        - "S" (slow)
        - "M" (medium)
        - "F" (fast)
        """
        self.inst.write(f':RATE:VOLTAGE:DC {speed}')
    
    def mode_dc_voltage(self):
        """
        Set the measurement mode to DC voltage.
        """
        self.inst.write(':FUNC:VOLTAGE:DC')
    
    