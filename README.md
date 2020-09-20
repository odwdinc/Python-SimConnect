[![PyPI version](https://badge.fury.io/py/SimConnect.svg)](https://badge.fury.io/py/SimConnect)
# Python-SimConnect

Python interface for Microsoft Flight Simulator 2020 (MSFS2020) using SimConnect

This library allows Python scripts to read and set variables within MSFS2020 and trigger events within the simulation.

It also includes, as an example, "Cockpit Companion", a flask mini http server which runs locally. It provides a web UI with a moving map and simulation variables. It also provides simulation data in JSON format in response to REST API requests.

Full documentation for this example can be found at [https://msfs2020.cc](https://msfs2020.cc) and it is included in a standalone repo here on Github as [MSFS2020-cockpit-companion](https://github.com/hankhank10/MSFS2020-cockpit-companion).

## Python interface example

````
from SimConnect import *

# Create SimConnect link
sm = SimConnect()
# Note the default _time is 2000 as to refreshed at 2s
aq = AircraftRequests(sm, _time=2000)
# Use _time=ms where ms is the millsec to refresh data to cash.
# setting ms to 0 will disable data cashing and allwas pull new data form sim.
# There is still a timeout of 4 trys with a 10ms delay between checks. 
# If no data is recived in 40ms the value will be set to -999999
# Each Requests can be fine tuned by seting the time pram.
# To find and set time out of cashed data to 200ms

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
````

## HTTP interface example

Run `glass_server.py` using Python 3.

#### `http://localhost:5000`
Method: GET

Variables: None

Output: Web interface with moving map and aircraft information

#### `http://localhost:5000/dataset/<dataset_name>`
Method: GET

Arguments to pass:

|Argument|Location|Description|
|---|---|---|
|dataset_name|in path|can be navigation, airspeed compass, vertical_speed, fuel, flaps, throttle, gear, trim, autopilot, cabin|

Description: Returns set of variables from simulator in JSON format


#### `http://localhost:5000/datapoint/<datapoint_name>/get`
Method: GET

Arguments to pass:

|Argument|Location|Description|
|---|---|---|
|datapoint_name|in path|any variable name from MS SimConnect documentation|

Description: Returns individual variable from simulator in JSON format


#### `http://localhost:5000/datapoint/<datapoint_name>/set`
Method: POST

Arguments to pass:

|Argument|Location|Description|
|---|---|---|
|datapoint_name|in path|any variable name from MS SimConnect documentation|
|index (optional)|form or json|the relevant index if required (eg engine number) - if not passed defaults to None|
|value_to_use (optional)|value to set variable to - if not passed defaults to 0|

Description: Sets datapoint in the simulator


#### `http://localhost:5000/event/<event_name>/trigger`
Method: POST

Arguments to pass:

|Argument|Location|Description|
|---|---|---|
|event_name|in path|any event name from MS SimConnect documentation|
|value_to_use (optional)|value to pass to the event|

Description: Triggers an event in the simulator

## Events and Variables

Below are links to the Microsoft documentation 

[Event IDs](https://docs.microsoft.com/en-us/previous-versions/microsoft-esp/cc526980(v=msdn.10))

[Simulation Variables](https://docs.microsoft.com/en-us/previous-versions/microsoft-esp/cc526981(v=msdn.10))
