[![PyPI version](https://badge.fury.io/py/SimConnect.svg)](https://badge.fury.io/py/SimConnect)
# Python-SimConnect

Python interface for Microsoft Flight Simulator 2020 (MSFS2020) using SimConnect

This library allows Python scripts to read and set variables within MSFS2020 and trigger events within the simulation.

It also includes, as an example, "Cockpit Companion", a flask mini http server which runs locally. It provides a web UI with a moving map and simulation variables. It also provides simulation data in JSON format in response to REST API requests.

Full documentation for this example can be found at [https://msfs2020.cc](https://msfs2020.cc) and it is included in a standalone repo here on Github as [MSFS2020-cockpit-companion](https://github.com/hankhank10/MSFS2020-cockpit-companion).


## Mobiflight Simconnect events:

Yes this supports the new [SimConnect commands that DocMoebiuz](https://forums.flightsimulator.com/t/full-g1000-control-now-with-mobiflight/348509) of [MobiFlight](https://www.mobiflight.com/en/index.html) developed.
A full list of [commands and install instructions](https://pastebin.com/fMdB7at2)

At this time MobiFlight SimConnect commands are not include in the AircraftEvents class and as so the AircraftEvents.find() and AircraftEvents.get() will not work. You will need to pass the Event ID to a new Event class as the Example below shows.


```py
from SimConnect import *
# Create SimConnect link
sm = SimConnect()
# Creat a function to call the MobiFlight AS1000_MFD_SOFTKEYS_3 event.
Sk3 = Event(b'MobiFlight.AS1000_MFD_SOFTKEYS_3', sm)
# Call the Event.
Sk3()
sm.exit()
quit()
```

## Python interface example

```py
from SimConnect import *

# Create SimConnect link
sm = SimConnect()
# Note the default _time is 2000 to be refreshed every 2 seconds
aq = AircraftRequests(sm, _time=2000)
# Use _time=ms where ms is the time in milliseconds to cache the data.
# Setting ms to 0 will disable data caching and always pull new data from the sim.
# There is still a timeout of 4 tries with a 10ms delay between checks.
# If no data is received in 40ms the value will be set to None
# Each request can be fine tuned by setting the time param.

# To find and set timeout of cached data to 200ms:
altitude = aq.find("PLANE_ALTITUDE")
altitude.time = 200

# Get the aircraft's current altitude
altitude = aq.get("PLANE_ALTITUDE")
altitude = altitude + 1000

# Set the aircraft's current altitude
aq.set("PLANE_ALTITUDE", altitude)

ae = AircraftEvents(sm)
# Trigger a simple event
event_to_trigger = ae.find("AP_MASTER")  # Toggles autopilot on or off
event_to_trigger()

# Trigger an event while passing a variable
target_altitude = 15000
event_to_trigger = ae.find("AP_ALT_VAR_SET_ENGLISH")  # Sets AP autopilot hold level
event_to_trigger(target_altitude)
sm.exit()
quit()
```

## Running SimConnect on a separate system.

#### Note: At this time SimConnect can only run on Windows hosts.

Create a file called SimConnect.cfg in the same folder as your script.
#### Sample SimConnect.cfg:
```ini
; Example SimConnect client configurations
[SimConnect]
Protocol=IPv4
Address=<ip of server>
Port=500
```
To enable the host running the sim to share over network,

add \<Address\>0.0.0.0\</Address\>

under the \<Port\>500\</Port\> in SimConnect.xml

SimConnect.xml can be located at
#### `%AppData%\Microsoft Flight Simulator\SimConnect.xml`

#### Sample SimConnect.xml:
```xml
<?xml version="1.0" encoding="Windows-1252"?>

<SimBase.Document Type="SimConnect" version="1,0">
    <Descr>SimConnect Server Configuration</Descr>
    <Filename>SimConnect.xml</Filename>
    <SimConnect.Comm>
        <Descr>Static IP4 port</Descr>
        <Protocol>IPv4</Protocol>
        <Scope>local</Scope>
        <Port>500</Port>
        <Address>0.0.0.0</Address>
        <MaxClients>64</MaxClients>
        <MaxRecvSize>41088</MaxRecvSize>
    </SimConnect.Comm>
...
```
## Notes:

Python 64-bit is needed. You may see this Error if running 32-bit python:

```OSError: [WinError 193] %1 is not a valid Win32 application```

Per mracko on COM_RADIO_SET:

    MSFS uses the European COM frequency spacing of 8.33kHz for all default aircraft.
    This means that in practice, you increment the frequency by 0.005 MHz and
    skip x.x20, x.x45, x.x70, and x.x95 MHz frequencies.
    Have a look here http://g3asr.co.uk/calculators/833kHz.htm


## Events and Variables

Below are links to the Microsoft documentation

[Function](https://docs.microsoft.com/en-us/previous-versions/microsoft-esp/cc526983(v=msdn.10))

[Event IDs](https://docs.microsoft.com/en-us/previous-versions/microsoft-esp/cc526980(v=msdn.10))

[Simulation Variables](https://docs.flightsimulator.com/html/Programming_Tools/SimVars/Simulation_Variables.htm)
