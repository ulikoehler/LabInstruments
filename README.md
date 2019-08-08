# LabInstruments
PyVISA wrappers for some of my lab instruments: Rigol DL3021, Agilent DSO-X 3024

**Note:** I use a USB connection to all of those instruments and use pyvisa-py as a backend driver on Linux. Getting the connection to work is the sole responsibility of [PyVISA](https://pyvisa.readthedocs.io/en/latest/)

**Note:** This project does not aim to be complete for any instrument, but I just add whatever function I want to try out, or need to use for some project. If you need to use other functions *please submit a pull request* or an issue if you have no idea of how to do it

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

## Usage example

```

```

## Troubleshooting

PyVISA doesn't find your device? Refer to [How to fix PyVISA not finding any USB instruments
](https://techoverflow.net/2019/08/08/how-to-fix-pyvisa-not-finding-any-usb-instruments/)

Got a `Found a device whose serial number cannot be read. The partial VISA resource name is ...` error? Refer to [How to fix PyVISA ‘Found a device whose serial number cannot be read. The partial VISA resource name is: USB0::[…]::[…]::???::0::INSTR’](https://techoverflow.net/2019/08/09/how-to-fix-pyvisa-found-a-device-whose-serial-number-cannot-be-read-the-partial-visa-resource-name-is-usb0-0instr/)
