# LabInstruments
PyVISA wrappers for some of my lab instruments: Rigol DL3021, Agilent DSO-X 3024

**Note:** I use a USB connection to all of those instruments and use pyvisa-py as a backend driver on Linux. Getting the connection to work is the sole responsibility of [PyVISA](https://pyvisa.readthedocs.io/en/latest/)

**Note:** This project does not aim to be complete for any instrument, but I just add whatever function I want to try out, or need to use for some project. If you need to use other functions *please submit a pull request* or an issue if you have no idea of how to implement it. Refer to the *programming manual* of your instrument for details on the commands available.

## Installation

On Debian/Ubuntu:

```sh
sudo apt -y install python3-dev python3-pip python3-usb
sudo pip3 install pyvisa pyvisa-py
```

Now you can clone *LabInstruments*:
```sh
git clone https://github.com/ulikoehler/LabInstruments.git
```

You also need to find the PyVISA ID of your instrument:

```
python3 LabInstruments/IdentifyInstruments.py
```

If you've setup your hardware & PyVISA installation correctly (see *Installation* above for PyVISA & ensure that your instrument is plugged in and turned on), you will see information like

```
Trying to open resource:  USB0::6833::3601::DL3A204100212::0::INSTR
        It's a RIGOL TECHNOLOGIES DL3021 with serial DL3A204100212
```

The PyVISA ID in this example is `USB0::6833::3601::DL3A204100212::0::INSTR`.

If it's telling you `No PyVISA resources found`, try to re-run it as `root` using `sudo`! If that works and you are using an instrument connected via USB or via USB adapter, refer to [How to fix ALL USB permission issues on Linux once and for all](https://techoverflow.net/2019/08/09/how-to-fix-all-usb-permission-issues-on-linux-once-and-for-all/).

## Usage example

This example connects to a Rigol DL3021 and configures it correctly.

Be sure to insert your specific PyVISA ID in the example!

Place this script in the directory where the `LabInstruments` directory is located.

```
#!/usr/bin/env python3
import pyvisa
from LabInstruments.DL3000 import DL3000

rm = pyvisa.ResourceManager()
inst = DL3021(rm.open_resource('USB0::6833::3601::DL3A204100212::0::INSTR'))
# Reset to factory settings (always do this to ensure a 100% consistent state)
inst.reset()

inst.set_mode("CURRENT") # CC
inst.set_cc_current(0.850) #A
inst.enable() # Switch ON
# Read voltage
print("{} V".format(inst.voltage()))
inst.disable() # Switch OFF
```

I recommend you add `LabInstruments` to your project as a `git submodule`:

```sh
git submodule init
git submodule add https://github.com/ulikoehler/LabInstruments.git LabInstruments
```

## Troubleshooting

PyVISA doesn't find your device? Refer to [How to fix PyVISA not finding any USB instruments
](https://techoverflow.net/2019/08/08/how-to-fix-pyvisa-not-finding-any-usb-instruments/)

Got a `Found a device whose serial number cannot be read. The partial VISA resource name is ...` error? Refer to [How to fix PyVISA ‘Found a device whose serial number cannot be read. The partial VISA resource name is: USB0::[…]::[…]::???::0::INSTR’](https://techoverflow.net/2019/08/09/how-to-fix-pyvisa-found-a-device-whose-serial-number-cannot-be-read-the-partial-visa-resource-name-is-usb0-0instr/)
