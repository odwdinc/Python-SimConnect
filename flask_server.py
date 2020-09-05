from flask import Flask, jsonify
from SimConnect import *
from time import sleep

app = Flask(__name__)

### SIMCONNECTION RELATED STARTUPS

# create simconnection
sm = SimConnect()

# create Request
myRequest = sm.newRequest(time=2000)  # set auto data collection time @ 2s

# add required definitions output data name, definition from SDK
myRequest.add('Altitude', (b'Plane Altitude', b'feet'))
myRequest.add('Latitude', (b'Plane Latitude', b'degrees'))
myRequest.add('Longitude', (b'Plane Longitude', b'degrees'))
myRequest.add('Kohlsman', (b'Kohlsman setting hg', b'inHg'))


AIRSPEEDRequest = sm.newRequest()
AIRSPEEDRequest.add('AIRSPEED_TRUE', (b'AIRSPEED TRUE', b'Knots'))
AIRSPEEDRequest.add('AIRSPEED_INDICATE', (b'AIRSPEED INDICATED', b'Knots'))
AIRSPEEDRequest.add('AIRSPEED_TRUE CALIBRATE', (b'AIRSPEED TRUE CALIBRATE', b'Degrees'))
AIRSPEEDRequest.add('AIRSPEED_BARBER POLE', (b'AIRSPEED BARBER POLE', b'Knots'))
AIRSPEEDRequest.add('AIRSPEED_MACH', (b'AIRSPEED MACH', b'Mach'))

COMPASSRequest = sm.newRequest()
COMPASSRequest.add('WISKEY_COMPASS_INDICATION_DEGREES', (b'WISKEY COMPASS INDICATION DEGREES', b'Degrees'))
COMPASSRequest.add('PARTIAL_PANEL_COMPASS', (b'PARTIAL PANEL COMPASS', b'Enum'))  # Gauge fail flag (0 = ok, 1 = fail, 2 = blank)
COMPASSRequest.add('ADF_CARD', (b'ADF CARD', b'Degrees'))  # ADF compass rose setting
COMPASSRequest.add('MAGNETIC_COMPASS', (b'MAGNETIC COMPASS', b'Degrees'))  # Compass reading
COMPASSRequest.add('INDUCTOR_COMPASS_PERCENT_DEVIATION', (b'INDUCTOR COMPASS PERCENT DEVIATION', b'Percent over 100'))  # Inductor compass deviation reading
COMPASSRequest.add('INDUCTOR_COMPASS_HEADING_REF', (b'INDUCTOR COMPASS HEADING REF', b'Radians'))  # Inductor compass heading


VERTICALSPEEDRequest = sm.newRequest()
VERTICALSPEEDRequest.add('VELOCITY_BODY_Y', (b'VELOCITY BODY Y', b'Feet per second'))  # True vertical speed, relative to aircraft axis
VERTICALSPEEDRequest.add('RELATIVE_WIND_VELOCITY_BODY_Y', (b'RELATIVE WIND VELOCITY BODY Y', b'Feet per second'))  # Vertical speed relative to wind
VERTICALSPEEDRequest.add('VERTICAL_SPEED', (b'VERTICAL SPEED', b'Feet per second'))  # Vertical speed indication
VERTICALSPEEDRequest.add('GPS_WP_VERTICAL_SPEED', (b'GPS WP VERTICAL SPEED', b'Meters per second'))  # Vertical speed to waypoint

FUELLEVELRequest = sm.newRequest()
FUELLEVELRequest.add('FUEL_TANK_CENTER_LEVEL', (b'FUEL TANK CENTER LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
FUELLEVELRequest.add('FUEL_TANK_CENTER2_LEVEL', (b'FUEL TANK CENTER2 LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
FUELLEVELRequest.add('FUEL_TANK_CENTER3_LEVEL', (b'FUEL TANK CENTER3 LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
FUELLEVELRequest.add('FUEL_TANK_LEFT_MAIN_LEVEL', (b'FUEL TANK LEFT MAIN LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
FUELLEVELRequest.add('FUEL_TANK_LEFT_AUX_LEVEL', (b'FUEL TANK LEFT AUX LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
FUELLEVELRequest.add('FUEL_TANK_LEFT_TIP_LEVEL', (b'FUEL TANK LEFT TIP LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
FUELLEVELRequest.add('FUEL_TANK_RIGHT_MAIN_LEVEL', (b'FUEL TANK RIGHT MAIN LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
FUELLEVELRequest.add('FUEL_TANK_RIGHT_AUX_LEVEL', (b'FUEL TANK RIGHT AUX LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
FUELLEVELRequest.add('FUEL_TANK_RIGHT_TIP_LEVEL', (b'FUEL TANK RIGHT TIP LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
FUELLEVELRequest.add('FUEL_TANK_EXTERNAL1_LEVEL', (b'FUEL TANK EXTERNAL1 LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
FUELLEVELRequest.add('FUEL_TANK_EXTERNAL2_LEVEL', (b'FUEL TANK EXTERNAL2 LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
FUELLEVELRequest.add('FUEL_TANK_CENTER_CAPACITY', (b'FUEL TANK CENTER CAPACITY', b'Gallons'))  # Maximum capacity in volume
FUELLEVELRequest.add('FUEL_TANK_CENTER2_CAPACITY', (b'FUEL TANK CENTER2 CAPACITY', b'Gallons'))  # Maximum capacity in volume
FUELLEVELRequest.add('FUEL_TANK_CENTER3_CAPACITY', (b'FUEL TANK CENTER3 CAPACITY', b'Gallons'))  # Maximum capacity in volume
FUELLEVELRequest.add('FUEL_TANK_LEFT_MAIN_CAPACITY', (b'FUEL TANK LEFT MAIN CAPACITY', b'Gallons'))  # Maximum capacity in volume
FUELLEVELRequest.add('FUEL_TANK_LEFT_AUX_CAPACITY', (b'FUEL TANK LEFT AUX CAPACITY', b'Gallons'))  # Maximum capacity in volume
FUELLEVELRequest.add('FUEL_TANK_LEFT_TIP_CAPACITY', (b'FUEL TANK LEFT TIP CAPACITY', b'Gallons'))  # Maximum capacity in volume
FUELLEVELRequest.add('FUEL_TANK_RIGHT_MAIN_CAPACITY', (b'FUEL TANK RIGHT MAIN CAPACITY', b'Gallons'))  # Maximum capacity in volume
FUELLEVELRequest.add('FUEL_TANK_RIGHT_AUX_CAPACITY', (b'FUEL TANK RIGHT AUX CAPACITY', b'Gallons'))  # Maximum capacity in volume
FUELLEVELRequest.add('FUEL_TANK_RIGHT_TIP_CAPACITY', (b'FUEL TANK RIGHT TIP CAPACITY', b'Gallons'))  # Maximum capacity in volume
FUELLEVELRequest.add('FUEL_TANK_EXTERNAL1_CAPACITY', (b'FUEL TANK EXTERNAL1 CAPACITY', b'Gallons'))  # Maximum capacity in volume
FUELLEVELRequest.add('FUEL_TANK_EXTERNAL2_CAPACITY', (b'FUEL TANK EXTERNAL2 CAPACITY', b'Gallons'))  # Maximum capacity in volume
FUELLEVELRequest.add('FUEL_LEFT_CAPACITY', (b'FUEL LEFT CAPACITY', b'Gallons'))  # Maximum capacity in volume
FUELLEVELRequest.add('FUEL_RIGHT_CAPACITY', (b'FUEL RIGHT CAPACITY', b'Gallons'))  # Maximum capacity in volume
FUELLEVELRequest.add('FUEL_TANK_CENTER_QUANTITY', (b'FUEL TANK CENTER QUANTITY', b'Gallons'))  # Current quantity in volume
FUELLEVELRequest.add('FUEL_TANK_CENTER2_QUANTITY', (b'FUEL TANK CENTER2 QUANTITY', b'Gallons'))  # Current quantity in volume
FUELLEVELRequest.add('FUEL_TANK_CENTER3_QUANTITY', (b'FUEL TANK CENTER3 QUANTITY', b'Gallons'))  # Current quantity in volume
FUELLEVELRequest.add('FUEL_TANK_LEFT_MAIN_QUANTITY', (b'FUEL TANK LEFT MAIN QUANTITY', b'Gallons'))  # Current quantity in volume
FUELLEVELRequest.add('FUEL_TANK_LEFT_AUX_QUANTITY', (b'FUEL TANK LEFT AUX QUANTITY', b'Gallons'))  # Current quantity in volume
FUELLEVELRequest.add('FUEL_TANK_LEFT_TIP_QUANTITY', (b'FUEL TANK LEFT TIP QUANTITY', b'Gallons'))  # Current quantity in volume
FUELLEVELRequest.add('FUEL_TANK_RIGHT_MAIN_QUANTITY', (b'FUEL TANK RIGHT MAIN QUANTITY', b'Gallons'))  # Current quantity in volume
FUELLEVELRequest.add('FUEL_TANK_RIGHT_AUX_QUANTITY', (b'FUEL TANK RIGHT AUX QUANTITY', b'Gallons'))  # Current quantity in volume
FUELLEVELRequest.add('FUEL_TANK_RIGHT_TIP_QUANTITY', (b'FUEL TANK RIGHT TIP QUANTITY', b'Gallons'))  # Current quantity in volume
FUELLEVELRequest.add('FUEL_TANK_EXTERNAL1_QUANTITY', (b'FUEL TANK EXTERNAL1 QUANTITY', b'Gallons'))  # Current quantity in volume
FUELLEVELRequest.add('FUEL_TANK_EXTERNAL2_QUANTITY', (b'FUEL TANK EXTERNAL2 QUANTITY', b'Gallons'))  # Current quantity in volume
FUELLEVELRequest.add('FUEL_LEFT_QUANTITY', (b'FUEL LEFT QUANTITY', b'Gallons'))  # Current quantity in volume
FUELLEVELRequest.add('FUEL_RIGHT_QUANTITY', (b'FUEL RIGHT QUANTITY', b'Gallons'))  # Current quantity in volume
FUELLEVELRequest.add('FUEL_TOTAL_QUANTITY', (b'FUEL TOTAL QUANTITY', b'Gallons'))  # Current quantity in volume
FUELLEVELRequest.add('FUEL_WEIGHT_PER_GALLON', (b'FUEL WEIGHT PER GALLON', b'Pounds'))  # Fuel weight per gallon
FUELLEVELRequest.add('FUEL_TOTAL_CAPACITY', (b'FUEL TOTAL CAPACITY', b'Gallons'))  # Total capacity of the aircraft
FUELLEVELRequest.add('FUEL_SELECTED_QUANTITY_PERCENT', (b'FUEL SELECTED QUANTITY PERCENT', b'Percent Over 100'))  # Percent or capacity for selected tank
FUELLEVELRequest.add('FUEL_SELECTED_QUANTITY', (b'FUEL SELECTED QUANTITY', b'Gallons'))  # Quantity of selected tank
FUELLEVELRequest.add('FUEL_TOTAL_QUANTITY_WEIGHT', (b'FUEL TOTAL QUANTITY WEIGHT', b'Pounds'))  # Current total fuel weight of the aircraft
FUELLEVELRequest.add('NUM_FUEL_SELECTORS', (b'NUM FUEL SELECTORS', b'Number'))  # Number of selectors on the aircraft
FUELLEVELRequest.add('UNLIMITED_FUEL', (b'UNLIMITED FUEL', b'Bool'))  # Unlimited fuel flag
FUELLEVELRequest.add('ESTIMATED_FUEL_FLOW', (b'ESTIMATED FUEL FLOW', b'Pounds per hour'))  # Estimated fuel flow at cruise


FLAPSRequest = sm.newRequest()
FLAPSRequest.add('FLAPS_HANDLE_PERCENT', (b'FLAPS HANDLE PERCENT', b'Percent Over 100'))  # Percent flap handle extended
FLAPSRequest.add('FLAPS_HANDLE_INDEX', (b'FLAPS HANDLE INDEX', b'Number'))  # Index of current flap position
FLAPSRequest.add('FLAPS_NUM_HANDLE_POSITIONS', (b'FLAPS NUM HANDLE POSITIONS', b'Number'))  # Number of flap positions
FLAPSRequest.add('TRAILING_EDGE_FLAPS_LEFT_PERCENT', (b'TRAILING EDGE FLAPS LEFT PERCENT', b'Percent Over 100'))  # Percent left trailing edge flap extended
FLAPSRequest.add('TRAILING_EDGE_FLAPS_RIGHT_PERCENT', (b'TRAILING EDGE FLAPS RIGHT PERCENT', b'Percent Over 100'))  # Percent right trailing edge flap extended
FLAPSRequest.add('TRAILING_EDGE_FLAPS_LEFT_ANGLE', (b'TRAILING EDGE FLAPS LEFT ANGLE', b'Radians'))  # Angle left trailing edge flap extended. Use TRAILING EDGE FLAPS LEFT PERCENT to set a value.
FLAPSRequest.add('TRAILING_EDGE_FLAPS_RIGHT_ANGLE', (b'TRAILING EDGE FLAPS RIGHT ANGLE', b'Radians'))  # Angle right trailing edge flap extended. Use TRAILING EDGE FLAPS RIGHT PERCENT to set a value.
FLAPSRequest.add('LEADING_EDGE_FLAPS_LEFT_PERCENT', (b'LEADING EDGE FLAPS LEFT PERCENT', b'Percent Over 100'))  # Percent left leading edge flap extended
FLAPSRequest.add('LEADING_EDGE_FLAPS_RIGHT_PERCENT', (b'LEADING EDGE FLAPS RIGHT PERCENT', b'Percent Over 100'))  # Percent right leading edge flap extended
FLAPSRequest.add('LEADING_EDGE_FLAPS_LEFT_ANGLE', (b'LEADING EDGE FLAPS LEFT ANGLE', b'Radians'))  # Angle left leading edge flap extended. Use LEADING EDGE FLAPS LEFT PERCENT to set a value.
FLAPSRequest.add('LEADING_EDGE_FLAPS_RIGHT_ANGLE', (b'LEADING EDGE FLAPS RIGHT ANGLE', b'Radians'))  # Angle right leading edge flap extended. Use LEADING EDGE FLAPS RIGHT PERCENT to set a value.
FLAPSRequest.add('FLAPS_AVAILABLE', (b'FLAPS AVAILABLE', b'Bool'))  # True if flaps available
FLAPSRequest.add('FLAP_DAMAGE_BY_SPEED', (b'FLAP DAMAGE BY SPEED', b'Bool'))  # True if flagps are damaged by excessive speed
FLAPSRequest.add('FLAP_SPEED_EXCEEDED', (b'FLAP SPEED EXCEEDED', b'Bool'))  # True if safe speed limit for flaps exceeded

THROTTLERequest = sm.newRequest()
THROTTLERequest.add('AUTOPILOT_THROTTLE_ARM', (b'AUTOPILOT THROTTLE ARM', b'Bool'))  # Autothrottle armed
THROTTLERequest.add('AUTOPILOT_TAKEOFF_POWER_ACTIVE', (b'AUTOPILOT TAKEOFF POWER ACTIVE', b'Bool'))  # Takeoff / Go Around power mode active
THROTTLERequest.add('AUTOTHROTTLE_ACTIVE', (b'AUTOTHROTTLE ACTIVE', b'Bool'))  # Auto-throttle active
THROTTLERequest.add('FULL_THROTTLE_THRUST_TO_WEIGHT_RATIO', (b'FULL THROTTLE THRUST TO WEIGHT RATIO', b'Number'))  # Full throttle thrust to weight ratio
THROTTLERequest.add('THROTTLE_LOWER_LIMIT', (b'THROTTLE LOWER LIMIT', b'Percent'))  # Percent throttle defining lower limit (negative for reverse thrust equipped airplanes)
THROTTLERequest.add('GENERAL_ENG_THROTTLE_LEVER_POSITION:index', (b'GENERAL ENG THROTTLE LEVER POSITION:index', b'Percent'))  # Percent of max throttle position
THROTTLERequest.add('AUTOPILOT_THROTTLE_ARM', (b'AUTOPILOT THROTTLE ARM', b'Bool'))  # Autothrottle armed
THROTTLERequest.add('AUTOTHROTTLE_ACTIVE', (b'AUTOTHROTTLE ACTIVE', b'Bool'))  # Auto-throttle active
THROTTLERequest.add('FULL_THROTTLE_THRUST_TO_WEIGHT_RATIO', (b'FULL THROTTLE THRUST TO WEIGHT RATIO', b'Number'))  # Full throttle thrust to weight ratio


GEARRequest = sm.newRequest()
GEARRequest.add('IS_GEAR_RETRACTABLE', (b'IS GEAR RETRACTABLE', b'Bool'))  # True if gear can be retracted
GEARRequest.add('IS_GEAR_SKIS', (b'IS GEAR SKIS', b'Bool'))  # True if landing gear is skis
GEARRequest.add('IS_GEAR_FLOATS', (b'IS GEAR FLOATS', b'Bool'))  # True if landing gear is floats
GEARRequest.add('IS_GEAR_SKIDS', (b'IS GEAR SKIDS', b'Bool'))  # True if landing gear is skids
GEARRequest.add('IS_GEAR_WHEELS', (b'IS GEAR WHEELS', b'Bool'))  # True if landing gear is wheels
GEARRequest.add('GEAR_HANDLE_POSITION', (b'GEAR HANDLE POSITION', b'Bool'))  # True if gear handle is applied
GEARRequest.add('GEAR_HYDRAULIC_PRESSURE', (b'GEAR HYDRAULIC PRESSURE', b'Pound force per square foot (psf)'))  # Gear hydraulic pressure
GEARRequest.add('TAILWHEEL_LOCK_ON', (b'TAILWHEEL LOCK ON', b'Bool'))  # True if tailwheel lock applied
GEARRequest.add('GEAR_CENTER_POSITION', (b'GEAR CENTER POSITION', b'Percent Over 100'))  # Percent center gear extended
GEARRequest.add('GEAR_LEFT_POSITION', (b'GEAR LEFT POSITION', b'Percent Over 100'))  # Percent left gear extended
GEARRequest.add('GEAR_RIGHT_POSITION', (b'GEAR RIGHT POSITION', b'Percent Over 100'))  # Percent right gear extended
GEARRequest.add('GEAR_TAIL_POSITION', (b'GEAR TAIL POSITION', b'Percent Over 100'))  # Percent tail gear extended
GEARRequest.add('GEAR_AUX_POSITION', (b'GEAR AUX POSITION', b'Percent Over 100'))  # Percent auxiliary gear extended
GEARRequest.add('GEAR_TOTAL_PCT_EXTENDED', (b'GEAR TOTAL PCT EXTENDED', b'Percentage'))  # Percent total gear extended
GEARRequest.add('AUTO_BRAKE_SWITCH_CB', (b'AUTO BRAKE SWITCH CB', b'Number'))  # Auto brake switch position
GEARRequest.add('WATER_RUDDER_HANDLE_POSITION', (b'WATER RUDDER HANDLE POSITION', b'Percent Over 100'))  # Position of the water rudder handle (0 handle retracted, 100 rudder handle applied)
GEARRequest.add('WATER_LEFT_RUDDER_EXTENDED', (b'WATER LEFT RUDDER EXTENDED', b'Percentage'))  # Percent extended
GEARRequest.add('WATER_RIGHT_RUDDER_EXTENDED', (b'WATER RIGHT RUDDER EXTENDED', b'Percentage'))  # Percent extended
GEARRequest.add('GEAR_CENTER_STEER_ANGLE', (b'GEAR CENTER STEER ANGLE', b'Percent Over 100'))  # Center wheel angle, negative to the left, positive to the right.
GEARRequest.add('GEAR_LEFT_STEER_ANGLE', (b'GEAR LEFT STEER ANGLE', b'Percent Over 100'))  # Left wheel angle, negative to the left, positive to the right.
GEARRequest.add('GEAR_RIGHT_STEER_ANGLE', (b'GEAR RIGHT STEER ANGLE', b'Percent Over 100'))  # Right wheel angle, negative to the left, positive to the right.
GEARRequest.add('GEAR_AUX_STEER_ANGLE', (b'GEAR AUX STEER ANGLE', b'Percent Over 100'))  # Aux wheel angle, negative to the left, positive to the right. The aux wheel is the fourth set of gear, sometimes used on helicopters.
GEARRequest.add('WATER_LEFT_RUDDER_STEER_ANGLE', (b'WATER LEFT RUDDER STEER ANGLE', b'Percent Over 100'))  # Water left rudder angle, negative to the left, positive to the right.
GEARRequest.add('WATER_RIGHT_RUDDER_STEER_ANGLE', (b'WATER RIGHT RUDDER STEER ANGLE', b'Percent Over 100'))  # Water right rudder angle, negative to the left, positive to the right.
GEARRequest.add('GEAR_CENTER_STEER_ANGLE_PCT', (b'GEAR CENTER STEER ANGLE PCT', b'Percent Over 100'))  # Center steer angle as a percentage
GEARRequest.add('GEAR_LEFT_STEER_ANGLE_PCT', (b'GEAR LEFT STEER ANGLE PCT', b'Percent Over 100'))  # Left steer angle as a percentage
GEARRequest.add('GEAR_RIGHT_STEER_ANGLE_PCT', (b'GEAR RIGHT STEER ANGLE PCT', b'Percent Over 100'))  # Right steer angle as a percentage
GEARRequest.add('GEAR_AUX_STEER_ANGLE_PCT', (b'GEAR AUX STEER ANGLE PCT', b'Percent Over 100'))  # Aux steer angle as a percentage
GEARRequest.add('WATER_LEFT_RUDDER_STEER_ANGLE_PCT', (b'WATER LEFT RUDDER STEER ANGLE PCT', b'Percent Over 100'))  # Water left rudder angle as a percentage
GEARRequest.add('WATER_RIGHT_RUDDER_STEER_ANGLE_PCT', (b'WATER RIGHT RUDDER STEER ANGLE PCT', b'Percent Over 100'))  # Water right rudder as a percentage
GEARRequest.add('CENTER_WHEEL_RPM', (b'CENTER WHEEL RPM', b'Rpm'))  # Center landing gear rpm
GEARRequest.add('LEFT_WHEEL_RPM', (b'LEFT WHEEL RPM', b'Rpm'))  # Left landing gear rpm
GEARRequest.add('RIGHT_WHEEL_RPM', (b'RIGHT WHEEL RPM', b'Rpm'))  # Right landing gear rpm
GEARRequest.add('AUX_WHEEL_RPM', (b'AUX WHEEL RPM', b'Rpm'))  # Rpm of fourth set of gear wheels.
GEARRequest.add('CENTER_WHEEL_ROTATION_ANGLE', (b'CENTER WHEEL ROTATION ANGLE', b'Radians'))  # Center wheel rotation angle
GEARRequest.add('LEFT_WHEEL_ROTATION_ANGLE', (b'LEFT WHEEL ROTATION ANGLE', b'Radians'))  # Left wheel rotation angle
GEARRequest.add('RIGHT_WHEEL_ROTATION_ANGLE', (b'RIGHT WHEEL ROTATION ANGLE', b'Radians'))  # Right wheel rotation angle
GEARRequest.add('AUX_WHEEL_ROTATION_ANGLE', (b'AUX WHEEL ROTATION ANGLE', b'Radians'))  # Aux wheel rotation angle
GEARRequest.add('GEAR_EMERGENCY_HANDLE_POSITION', (b'GEAR EMERGENCY HANDLE POSITION', b'Bool'))  # True if gear emergency handle applied
GEARRequest.add('ANTISKID_BRAKES_ACTIVE', (b'ANTISKID BRAKES ACTIVE', b'Bool'))  # True if antiskid brakes active
GEARRequest.add('RETRACT_FLOAT_SWITCH', (b'RETRACT FLOAT SWITCH', b'Bool'))  # True if retract float switch on
GEARRequest.add('RETRACT_LEFT_FLOAT_EXTENDED', (b'RETRACT LEFT FLOAT EXTENDED', b'Percent (0 is fully retracted, 100 is fully extended)'))  # If aircraft has retractable floats.
GEARRequest.add('RETRACT_RIGHT_FLOAT_EXTENDED', (b'RETRACT RIGHT FLOAT EXTENDED', b'Percent (0 is fully retracted, 100 is fully extended)'))  # If aircraft has retractable floats.
GEARRequest.add('STEER_INPUT_CONTROL', (b'STEER INPUT CONTROL', b'Percent over 100'))  # Position of steering tiller
GEARRequest.add('GEAR_DAMAGE_BY_SPEED', (b'GEAR DAMAGE BY SPEED', b'Bool'))  # True if gear has been damaged by excessive speed
GEARRequest.add('GEAR_SPEED_EXCEEDED', (b'GEAR SPEED EXCEEDED', b'Bool'))  # True if safe speed limit for gear exceeded
GEARRequest.add('NOSEWHEEL_LOCK_ON', (b'NOSEWHEEL LOCK ON', b'Bool'))  # True if the nosewheel lock is engaged.

TRIMRequest = sm.newRequest()
TRIMRequest.add('ROTOR_LATERAL_TRIM_PCT', (b'ROTOR LATERAL TRIM PCT', b'Percent Over 100'))  # Trim percent
TRIMRequest.add('ELEVATOR_TRIM_POSITION', (b'ELEVATOR TRIM POSITION', b'Radians'))  # Elevator trim deflection
TRIMRequest.add('ELEVATOR_TRIM_INDICATOR', (b'ELEVATOR TRIM INDICATOR', b'Position (-16K to 0) -16K = full down'))  # Percent elevator trim (for indication)
TRIMRequest.add('ELEVATOR_TRIM_PCT', (b'ELEVATOR TRIM PCT', b'Percent Over 100'))  # Percent elevator trim
TRIMRequest.add('AILERON_TRIM', (b'AILERON TRIM', b'Radians'))  # Angle deflection
TRIMRequest.add('AILERON_TRIM_PCT', (b'AILERON TRIM PCT', b'Float. Percent over 100'))  # The trim position of the ailerons. Zero is fully retracted.
TRIMRequest.add('RUDDER_TRIM_PCT', (b'RUDDER TRIM PCT', b'Float. Percent over 100'))  # The trim position of the rudder. Zero is no trim.
TRIMRequest.add('RUDDER_TRIM', (b'RUDDER TRIM', b'Radians'))  # Angle deflection

AUTOPILOTRequest = sm.newRequest()
AUTOPILOTRequest.add('AUTOPILOT_MASTER', (b'AUTOPILOT MASTER', b'Bool'))
AUTOPILOTRequest.add('AUTOPILOT_AVAILABLE', (b'AUTOPILOT AVAILABLE', b'Bool'))
AUTOPILOTRequest.add('AUTOPILOT_NAV_SELECTED', (b'AUTOPILOT NAV SELECTED', b'Number'))
AUTOPILOTRequest.add('AUTOPILOT_WING_LEVELER', (b'AUTOPILOT WING LEVELER', b'Bool'))
AUTOPILOTRequest.add('AUTOPILOT_NAV1_LOCK', (b'AUTOPILOT NAV1 LOCK', b'Bool'))
AUTOPILOTRequest.add('AUTOPILOT_HEADING_LOCK', (b'AUTOPILOT HEADING LOCK', b'Bool'))
AUTOPILOTRequest.add('AUTOPILOT_HEADING_LOCK_DIR', (b'AUTOPILOT HEADING LOCK DIR', b'Degrees'))
AUTOPILOTRequest.add('AUTOPILOT_ALTITUDE_LOCK', (b'AUTOPILOT ALTITUDE LOCK', b'Bool'))
AUTOPILOTRequest.add('AUTOPILOT_ALTITUDE_LOCK_VAR', (b'AUTOPILOT ALTITUDE LOCK VAR', b'Feet'))
AUTOPILOTRequest.add('AUTOPILOT_ATTITUDE_HOLD', (b'AUTOPILOT ATTITUDE HOLD', b'Bool'))
AUTOPILOTRequest.add('AUTOPILOT_GLIDESLOPE_HOLD', (b'AUTOPILOT GLIDESLOPE HOLD', b'Bool'))
AUTOPILOTRequest.add('AUTOPILOT_PITCH_HOLD_REF', (b'AUTOPILOT PITCH HOLD REF', b'Radians'))
AUTOPILOTRequest.add('AUTOPILOT_APPROACH_HOLD', (b'AUTOPILOT APPROACH HOLD', b'Bool'))
AUTOPILOTRequest.add('AUTOPILOT_BACKCOURSE_HOLD', (b'AUTOPILOT BACKCOURSE HOLD', b'Bool'))
AUTOPILOTRequest.add('AUTOPILOT_VERTICAL_HOLD_VAR', (b'AUTOPILOT VERTICAL HOLD VAR', b'Feet/minute'))
AUTOPILOTRequest.add('AUTOPILOT_PITCH_HOLD', (b'AUTOPILOT PITCH HOLD', b'Bool'))
AUTOPILOTRequest.add('AUTOPILOT_FLIGHT_DIRECTOR_ACTIVE', (b'AUTOPILOT FLIGHT DIRECTOR ACTIVE', b'Bool'))
AUTOPILOTRequest.add('AUTOPILOT_FLIGHT_DIRECTOR_PITCH', (b'AUTOPILOT FLIGHT DIRECTOR PITCH', b'Radians'))
AUTOPILOTRequest.add('AUTOPILOT_FLIGHT_DIRECTOR_BANK', (b'AUTOPILOT FLIGHT DIRECTOR BANK', b'Radians'))
AUTOPILOTRequest.add('AUTOPILOT_AIRSPEED_HOLD', (b'AUTOPILOT AIRSPEED HOLD', b'Bool'))
AUTOPILOTRequest.add('AUTOPILOT_AIRSPEED_HOLD_VAR', (b'AUTOPILOT AIRSPEED HOLD VAR', b'Knots'))
AUTOPILOTRequest.add('AUTOPILOT_MACH_HOLD', (b'AUTOPILOT MACH HOLD', b'Bool'))
AUTOPILOTRequest.add('AUTOPILOT_MACH_HOLD_VAR', (b'AUTOPILOT MACH HOLD VAR', b'Number'))
AUTOPILOTRequest.add('AUTOPILOT_YAW_DAMPER', (b'AUTOPILOT YAW DAMPER', b'Bool'))
AUTOPILOTRequest.add('AUTOPILOT_RPM_HOLD_VAR', (b'AUTOPILOT RPM HOLD VAR', b'Number'))
AUTOPILOTRequest.add('AUTOPILOT_THROTTLE_ARM', (b'AUTOPILOT THROTTLE ARM', b'Bool'))
AUTOPILOTRequest.add('AUTOPILOT_TAKEOFF_POWER ACTIVE', (b'AUTOPILOT TAKEOFF POWER ACTIVE', b'Bool'))
AUTOPILOTRequest.add('AUTOTHROTTLE_ACTIVE', (b'AUTOTHROTTLE ACTIVE', b'Bool'))
AUTOPILOTRequest.add('AUTOPILOT_VERTICAL_HOLD', (b'AUTOPILOT VERTICAL HOLD', b'Bool'))
AUTOPILOTRequest.add('AUTOPILOT_RPM_HOLD', (b'AUTOPILOT RPM HOLD', b'Bool'))
AUTOPILOTRequest.add('AUTOPILOT_MAX_BANK', (b'AUTOPILOT MAX BANK', b'Radians'))
AUTOPILOTRequest.add('FLY_BY_WIRE_ELAC_SWITCH', (b'FLY BY WIRE ELAC SWITCH', b'Bool'))
AUTOPILOTRequest.add('FLY_BY_WIRE_FAC_SWITCH', (b'FLY BY WIRE FAC SWITCH', b'Bool'))
AUTOPILOTRequest.add('FLY_BY_WIRE_SEC_SWITCH', (b'FLY BY WIRE SEC SWITCH', b'Bool'))
AUTOPILOTRequest.add('FLY_BY_WIRE_ELAC_FAILED', (b'FLY BY WIRE ELAC FAILED', b'Bool'))
AUTOPILOTRequest.add('FLY_BY_WIRE_FAC_FAILED', (b'FLY BY WIRE FAC FAILED', b'Bool'))
AUTOPILOTRequest.add('FLY_BY_WIRE_SEC_FAILED', (b'FLY BY WIRE SEC FAILED', b'Bool'))



@app.route('/json/')
@app.route('/json/all')
def json_add_data():

    attempts = 0
    data = None

    while data is None and attempts < 20:
        sm.RequestData(myRequest)
        sm.Run()
        data = sm.GetData(myRequest, True)
        if data is None:
            sleep(0.5)
        attempts = attempts + 1

    if data is None:
        data_dictionary = {
            "Status": "failed to access simulator despite repeated attempts"
        }
    else:
        data_dictionary = {
            "Status": "success",
        }
        data_dictionary.update(data)
        return jsonify(data_dictionary)


app.run(host='0.0.0.0', port=5000, debug=True)