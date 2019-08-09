#!/usr/bin/env python3
import numpy as np
import struct

__all__ = ["DSOX3000"]

class DSOX3000(object):
    """
    Rigol DL3000 command wrapper.
    """
    def __init__(self, inst):
        """
        Initialize the DL3000 wrapper with a specific PyVISA resource.
        This class does NOT open the resource, you have to open it for yourself!
        """
        self.inst = inst
        self.inst.timeout = 5000

    def enable_channel(self, chan):
        """
        Enable the given channel
        """
        self.inst.write(":VIEW CHAN{}".format(chan))
    
    def disable_channel(self, chan):
        """
        Enable the given channel
        """
        self.inst.write(":BLANK CHAN{}".format(chan))

    def autoscale(self, chan):
        """
        Autoscale a specific channel
        """
        self.inst.write(":AUT CHAN{}".format(chan))

    def trigger_mode(self, mode):
        """
        Enable the given trigger mode:
        "EDGE", "GLIT", "PATT", "TV", "DELAY", "EBURST", "OR", "RUNT", "SHOLD", "TRANSITION", "SBUS1", "SBUS2"
        """
        self.inst.write(":TRIG:MODE {}".format(mode))

    def trigger_coupling(self, mode):
        """
        Enable the given edge trigger coupling:
        "AC" | "DC" | "LFReject"
        """
        self.inst.write(":TRIG:COUP {}".format(mode))

    def trigger_level(self, level):
        """
        Set the trigger level in Volts
        """
        self.inst.write(":TRIG:LEVEL {}".format(level))

    def trigger_source(self, src):
        """
        Set the trigger source:
        "CHAN<n>" | "EXTERNAL" | "LINE" | "WGEN"
        """
        self.inst.write(":TRIG:SOURCE {}".format(src))

    def trigger_source_channel(self, ch):
        """
        Set the trigger source (numeric channel)
        """
        self.trigger_source("CHAN{}".format(ch))

    def trigger_slope(self, slope):
        """
        Set the edge trigger slope:
        "POSITIVE" | "NEGATIVE" | "EITHER" | "ALTERNATE
        """
        self.inst.write(":TRIG:SLOPE {}".format(slope))

    def single(self):
        """
        Activate single capture mode
        """
        self.inst.write(":SINGLE")

    def run(self):
        """
        Activate run capture mode
        """
        self.inst.write(":RUN")

    def stop(self):
        """
        Stop capture mode
        """
        self.inst.write(":STOP")

    def timebase_normal(self):
        """
        Activate normal timebase mode
        """
        self.inst.write(":TIMEBASE:MODE MAIN")

    def timebase_roll(self):
        """
        Activate normal timebase mode
        """
        self.inst.write(":TIMEBASE:MODE ROLL")

    def timebase_trigger_position(self, position):
        """
        Set the middle of the timebase relative to the trigger position
        position must be a value in seconds.
        Positive values means the trigger is BEFORE the middle of the screen!
        """
        self.inst.write(":TIMEBASE:POSITION {}".format(position))

    def timebase_scale(self, scale):
        """
        Set the horizontal timescale per division in SECONDS
        """
        self.inst.write(":TIMEBASE:SCALE {}".format(scale))

    def screenshot_png(self):
        """
        Create a PNG screenshot
        """
        return self.inst.query_binary_values(":DISP:DATA? PNG", datatype='s', delay=1)[0]

    def waveform_acquire(self, src, mode="RAW"):
        """
        Acquire waveform data and store in memory so it
        src: "CHAN<n>" | "FUNC" | "MATH" | "SBUS1" | "SBUS2"
        mode: "NORMAL" | "MAXIMUM" | "RAW"
        """
        self.inst.write(":WAVEFORM:FORMAT WORD") # binary WORD transfer
        self.inst.write(":WAVEFORM:SOURCE {}".format(src))
        self.inst.write(":WAVEFORM:POINTS:MODE {}".format(mode))
        self.inst.write(":WAVEFORM:POINTS 8000000".format()) # binary WORD transfer
        self.inst.write(":DIGITIZE {}".format(src))

    def waveform_data_raw(self):
        """
        Retrieve acquired waveform data
        Call waveform_acquire() before this!!
        """
        preamble = self.inst.query(":WAVEFORM:PREAMBLE?")
        fmt, typ, pnts, count, xinc, xorigin, xreference, yincrement, yorigin, yreference = preamble.strip().split(",")
        # Parse preamble
        # NOTE: fmt is always WORD, type no care
        pnts = int(pnts)
        count = int(count)
        xinc = float(xinc)
        xorigin = float(xorigin)
        xreference = int(xreference)
        yincrement = float(yincrement)
        yorigin = float(yorigin)
        yreference = int(yreference)
        # Request actual data
        data = self.inst.query_binary_values(":WAVEFORM:DATA?", datatype='h', container=np.ndarray)
        # TODO postprocess data with preamble information
        return data

    def reset(self):
        self.inst.write("*RST")
