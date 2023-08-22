#!/usr/bin/env python3
import pyvisa
rm = pyvisa.ResourceManager()

resources = rm.list_resources()

if not resources:
    print("No PyVISA resources found")

# Try to open resources and let them identify themselves
for resource in resources:
    print("\nTrying to open resource: ", resource)
    try:
        res = rm.open_resource(resource)
        idn_parts = res.query("*IDN?").split(",")
        identifier = " ".join(idn_parts[:2]) # MFR & Model
        serial = idn_parts[2]
        print("\tIt's a {} with serial {}".format(identifier, serial))
    except Exception as ex:
        print("\t Error: {}".format(ex))
