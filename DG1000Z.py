#!/usr/bin/env python3
from typing import Literal
__all__ = ["DL3000"]

class DG1000Z(object):
    """
    Rigol DG1000Z (e.g. DG1022Z) function generator command wrapper.
    """
    def __init__(self, inst):
        """
        Initialize the DG1000Z wrapper with a specific PyVISA resource.
        This class does NOT open the resource, you have to open it for yourself!
        
        Official programming manual:
        https://www.batronix.com/pdf/Rigol/ProgrammingGuide/DG1000Z_ProgrammingGuide_EN.pdf
        
        Example:
        ```
        import pyvisa
        from DG1000 import DG1000

        rm = pyvisa.ResourceManager()
        inst = rm.open_resource('TCPIP0::10.9.8.40::INSTR')
        dg1022 = DG1000(inst)
        """
        self.inst = inst
        
    @staticmethod
    def _float_or_string(s):
        try:
            return float(s)
        except ValueError:
            return s
        
        
    def set_channel_enabled(self, channel, enabled=True):
        """
        Enable the given channel
        """
        self.inst.write(f"OUTPUT{channel} {'ON' if enabled else 'OFF'}")
        
    def query_channel_enabled(self, channel):
        """
        Query if the given channel is enabled
        """
        return self.inst.query(f"OUTPUT{channel}?").strip() == "ON"
    
    def set_channel_waveform(self, channel, waveform: Literal['SIN','SQU','RAMP','PULSE','NOISE','DC','USER']):
        """
        Set the given channel to the given waveform.
        Note that there are (some) more specific functions that set
        the waveform including the parameters.
        """
        self.inst.write(f"SOURCE{channel}:APPLY:{waveform}")
        
    def query_waveform(self, channel=1):
        """
        Query the given channel's waveform.
        
        Returns a list where the first element is a string (the waveform mode)
        and the others are floats (the parameters).
        Floats that cannot be parsed are returned as strings.
        
        Example return value: ['PULSE', 6.0, 2.0, 1.0, 0.0]
        """
        ret = self.inst.query(f"SOURCE{channel}:APPLY?").strip().strip("\"")
        splitted = ret.split(",")
        return [
            DG1000Z._float_or_string(v) for v in splitted
        ]
        
    def set_pulse_width(self, channel, width="5us"):
        """
        Set the given channel's pulse width.
        """
        self.inst.write(f":SOURCE{channel}:FUNC:PULSE:WIDTH {width}")
        
    def set_pulse_period(self, channel, period="100ms"):
        """
        Set the given channel's pulse period.
        """
        self.inst.write(f":SOURCE{channel}:FUNC:PULSE:PERIOD {period}")
        
    def set_pulse_frequency(self, channel, frequency="10Hz"):
        """
        Set the given channel's pulse frequency.
        """
        self.inst.write(f":SOURCE{channel}:FUNC:PULSE:FREQ {frequency}")
        
    def set_low_voltage_level(self, channel, voltage="0.0V"):
        """
        Set the given channel's low voltage level.
        """
        self.inst.write(f":SOURCE{channel}:VOLT:LOW {voltage}")
        
    def set_high_voltage_level(self, channel, voltage="1.0V"):
        """
        Set the given channel's low voltage level.
        """
        self.inst.write(f":SOURCE{channel}:VOLT:LOW {voltage}")
        
    def set_voltage_levels(self, channel, low="0.0V", high="1.0V"):
        """
        Set the given channel's low and high voltage levels.
        """
        self.inst.write(f":SOURCE{channel}:VOLT:LOW {low}")
        self.inst.write(f":SOURCE{channel}:VOLT:HIGH {high}")
        