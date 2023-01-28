[![PyPI version](https://badge.fury.io/py/SimConnect.svg)](https://badge.fury.io/py/SimConnect)
# Python-SimConnect

Python interface for Microsoft Flight Simulator 2020 (MSFS2020) using SimConnect

This library allows Python scripts to read and set variables within MSFS2020 and trigger events within the simulation.

## Setup and use

This is a fork of the official https://github.com/odwdinc/Python-SimConnect repository, as such if you want to use this fork in your project, install this using:

```
python -m pip install git+https://github.com/pomax/python-simconnect@master#egg=simconnect
```

This fork offers two ways to make calls using SimConnect:

1. the "convenient wrapper" way, and
2. the more low level "direct simconnect instance" way.

### The convenient way

Use the `SimConnection` wrapper object:

```python
from SimConnect import SimConnection


connection = SimConnection()
connection.connect()

running, paused, on_ground = connection.get_all(
    'SIM_RUNNING',
    'SIM_PAUSED',
    'SIM_ON_GROUND',
)

if running >= 3 and not paused:
    plane = connection.get('TITLE')
    print(f'User is flying the {plane}.')

    if on_ground:
        print(f'The plan is on the runway: resetting all trim.')
        connection.set('ELEVATOR_TRIM_POSITION', 0)
        connection.set('AILERON_TRIM_PCT', 0)
        connection.set('RUDDER_TRIM_PCT', 0)

    else:
        speed, alt, heading = connection.get_all(
            'AIRSPEED_TRUE',
            'INDICATED_ALTITUDE',
            'PLANE_HEADING_DEGREES_MAGNETIC',
        )
        print(f'Going {speed}kts at {alt}\' heading {heading} degrees.')


        print('Enabling autopilot and setting alt hold to 1500 feet')
        ap_enabled = connection.get('AUTOPILOT_MASTER')

        if ap_enabled == 0:
            connection.trigger('AP_MASTER')

        connection.trigger('AP_ALT_VAR_SET_ENGLISH', 15000)

connection.disconnect()
```

Note that this object comes with three simvars that are not part of the official SimConnect SDK:

| varname | type | description |
|---|---|-- |
| `SIM_RUNNING` | decimal | int.int format, the integer part is the current game state (see below), and the fractional part is an integer representing the current camera state |
| `SIM_PAUSED` | boolean | true if the user is in game, but paused into the menu system |
| `FLIGHT_RESET` | boolean | true if the user reset their flight after crashing. This value will always be `false` after reading |

The `SIM_RUNNING` state values are as follows:

| value | description |
|---|---|
| 0 | User is on a game state transition screen |
| 1 | User is navigating the menu system |
| 2 | User is in-game, but navigating the menu system |
| 3 | User is in-game |

For the camera values, see [the documentation for the `CAMERA_STATE` variable](https://docs.flightsimulator.com/html/Programming_Tools/SimVars/Camera_Variables.htm#CAMERA_STATE)

#### Adding event handling

If your code needs to handle events, you can extend the `SimConnection` object and implement the following functions:

```python
import SimConnection from SimConnect


class MySimConnection(SimConnection):
    def handle_id_event(self, event_id):
        super(event_id)
        # then your code here

    def handle_simobject_event(self, event):
        # your code here

    def handle_exception_event(self, exception, definition):
        # your code here
```

### Directly using the SimConnect object

For more direct control, you can also use the underlying SimConnect code:

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

## Mobiflight Simconnect events:

This supports the [SimConnect commands that DocMoebiuz](https://forums.flightsimulator.com/t/full-g1000-control-now-with-mobiflight/348509) of [MobiFlight](https://www.mobiflight.com/en/index.html) developed.

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

## Notes

### you need 64 bit Python

Python 64-bit is required. You may see the followed error when running 32-bit python:

```OSError: [WinError 193] %1 is not a valid Win32 application```

### US vs. EU radio frequency

Per mracko on COM_RADIO_SET:

> MSFS uses the European COM frequency spacing of 8.33kHz for all default aircraft. This means that in practice, you increment the frequency by 0.005 MHz and skip x.x20, x.x45, x.x70, and x.x95 MHz frequencies. Have a look here http://g3asr.co.uk/calculators/833kHz.htm


## MSFS SDK Documentation

Below are links to the Microsoft documentation:

- [SimConnect SDK Documentation](https://docs.flightsimulator.com/html/Introduction/Introduction.htm)
- [Event IDs](https://docs.flightsimulator.com/html/Programming_Tools/Event_IDs/Event_IDs.htm)
- [Simulation Variables](https://docs.flightsimulator.com/html/Programming_Tools/SimVars/Simulation_Variables.htm)
