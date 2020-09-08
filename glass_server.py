from flask import Flask, jsonify, render_template, request
from SimConnect import *
from time import sleep

app = Flask(__name__)

# SIMCONNECTION RELATED STARTUPS

# create simconnection
sm = SimConnect()

# create Request
request_ui = sm.new_request_holder()
request_ui.add('ALTITUDE', (b'PLANE ALTITUDE', b'feet'))
request_ui.add('LATITUDE', (b'PLANE LATITUDE', b'degrees'))
request_ui.add('LONGITUDE', (b'PLANE LONGITUDE', b'degrees'))
request_ui.add('AIRSPEED_INDICATE', (b'AIRSPEED INDICATED', b'Knots'))
request_ui.add('MAGNETIC_COMPASS', (b'MAGNETIC COMPASS', b'Degrees'))  # Compass reading
request_ui.add('VERTICAL_SPEED', (b'VERTICAL SPEED', b'feet/minute'))  # Vertical speed indication
request_ui.add('FLAPS_HANDLE_PERCENT', (b'FLAPS HANDLE PERCENT', b'Percent Over 100'))  # Percent flap handle extended
request_ui.add('FUEL_TOTAL_QUANTITY', (b'FUEL TOTAL QUANTITY', b'Gallons'))  # Current quantity in volume
request_ui.add('FUEL_TOTAL_CAPACITY', (b'FUEL TOTAL CAPACITY', b'Gallons'))  # Total capacity of the aircraft
request_ui.add('GEAR_HANDLE_POSITION', (b'GEAR HANDLE POSITION', b'Bool'))  # True if gear handle is applied
request_ui.add('AUTOPILOT_MASTER', (b'AUTOPILOT MASTER', b'Bool'))
request_ui.add('AUTOPILOT_NAV_SELECTED', (b'AUTOPILOT NAV SELECTED', b'Number'))
request_ui.add('AUTOPILOT_WING_LEVELER', (b'AUTOPILOT WING LEVELER', b'Bool'))
request_ui.add('AUTOPILOT_HEADING_LOCK', (b'AUTOPILOT HEADING LOCK', b'Bool'))
request_ui.add('AUTOPILOT_HEADING_LOCK_DIR', (b'AUTOPILOT HEADING LOCK DIR', b'Degrees'))
request_ui.add('AUTOPILOT_ALTITUDE_LOCK', (b'AUTOPILOT ALTITUDE LOCK', b'Bool'))
request_ui.add('AUTOPILOT_ALTITUDE_LOCK_VAR', (b'AUTOPILOT ALTITUDE LOCK VAR', b'Feet'))
request_ui.add('AUTOPILOT_ATTITUDE_HOLD', (b'AUTOPILOT ATTITUDE HOLD', b'Bool'))
request_ui.add('AUTOPILOT_GLIDESLOPE_HOLD', (b'AUTOPILOT GLIDESLOPE HOLD', b'Bool'))
request_ui.add('AUTOPILOT_PITCH_HOLD_REF', (b'AUTOPILOT PITCH HOLD REF', b'Radians'))
request_ui.add('AUTOPILOT_APPROACH_HOLD', (b'AUTOPILOT APPROACH HOLD', b'Bool'))
request_ui.add('AUTOPILOT_BACKCOURSE_HOLD', (b'AUTOPILOT BACKCOURSE HOLD', b'Bool'))
request_ui.add('AUTOPILOT_VERTICAL_HOLD', (b'AUTOPILOT VERTICAL HOLD', b'Bool'))
request_ui.add('AUTOPILOT_VERTICAL_HOLD_VAR', (b'AUTOPILOT VERTICAL HOLD VAR', b'Feet/minute'))
request_ui.add('AUTOPILOT_PITCH_HOLD', (b'AUTOPILOT PITCH HOLD', b'Bool'))
request_ui.add('AUTOPILOT_FLIGHT_DIRECTOR_ACTIVE', (b'AUTOPILOT FLIGHT DIRECTOR ACTIVE', b'Bool'))
request_ui.add('AUTOPILOT_AIRSPEED_HOLD', (b'AUTOPILOT AIRSPEED HOLD', b'Bool'))
request_ui.add('AUTOPILOT_AIRSPEED_HOLD_VAR', (b'AUTOPILOT AIRSPEED HOLD VAR', b'Knots'))

request_location = sm.new_request_holder()
request_location.add('ALTITUDE', (b'PLANE ALTITUDE', b'feet'))
request_location.add('LATITUDE', (b'PLANE LATITUDE', b'degrees'))
request_location.add('LONGITUDE', (b'PLANE LONGITUDE', b'degrees'))
request_location.add('KOHLSMAN', (b'KOHLSMAN SETTING HG', b'inHg'))

request_airspeed = sm.new_request_holder()
request_airspeed.add('AIRSPEED_TRUE', (b'AIRSPEED TRUE', b'Knots'))
request_airspeed.add('AIRSPEED_INDICATE', (b'AIRSPEED INDICATED', b'Knots'))
request_airspeed.add('AIRSPEED_TRUE CALIBRATE', (b'AIRSPEED TRUE CALIBRATE', b'Degrees'))
request_airspeed.add('AIRSPEED_BARBER POLE', (b'AIRSPEED BARBER POLE', b'Knots'))
request_airspeed.add('AIRSPEED_MACH', (b'AIRSPEED MACH', b'Mach'))

request_compass = sm.new_request_holder()
request_compass.add('WISKEY_COMPASS_INDICATION_DEGREES', (b'WISKEY COMPASS INDICATION DEGREES', b'Degrees'))
request_compass.add('PARTIAL_PANEL_COMPASS', (b'PARTIAL PANEL COMPASS', b'Enum'))  # Gauge fail flag (0 = ok, 1 = fail, 2 = blank)
request_compass.add('ADF_CARD', (b'ADF CARD', b'Degrees'))  # ADF compass rose setting
request_compass.add('MAGNETIC_COMPASS', (b'MAGNETIC COMPASS', b'Degrees'))  # Compass reading
request_compass.add('INDUCTOR_COMPASS_PERCENT_DEVIATION', (b'INDUCTOR COMPASS PERCENT DEVIATION', b'Percent over 100'))  # Inductor compass deviation reading
request_compass.add('INDUCTOR_COMPASS_HEADING_REF', (b'INDUCTOR COMPASS HEADING REF', b'Radians'))  # Inductor compass heading

request_vertical_speed = sm.new_request_holder()
request_vertical_speed.add('VELOCITY_BODY_Y', (b'VELOCITY BODY Y', b'Feet per second'))  # True vertical speed, relative to aircraft axis
request_vertical_speed.add('RELATIVE_WIND_VELOCITY_BODY_Y', (b'RELATIVE WIND VELOCITY BODY Y', b'Feet per second'))  # Vertical speed relative to wind
request_vertical_speed.add('VERTICAL_SPEED', (b'VERTICAL SPEED', b'Feet per second'))  # Vertical speed indication
request_vertical_speed.add('GPS_WP_VERTICAL_SPEED', (b'GPS WP VERTICAL SPEED', b'Meters per second'))  # Vertical speed to waypoint

request_fuel = sm.new_request_holder()
request_fuel.add('FUEL_TANK_CENTER_LEVEL', (b'FUEL TANK CENTER LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
request_fuel.add('FUEL_TANK_CENTER2_LEVEL', (b'FUEL TANK CENTER2 LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
request_fuel.add('FUEL_TANK_CENTER3_LEVEL', (b'FUEL TANK CENTER3 LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
request_fuel.add('FUEL_TANK_LEFT_MAIN_LEVEL', (b'FUEL TANK LEFT MAIN LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
request_fuel.add('FUEL_TANK_LEFT_AUX_LEVEL', (b'FUEL TANK LEFT AUX LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
request_fuel.add('FUEL_TANK_LEFT_TIP_LEVEL', (b'FUEL TANK LEFT TIP LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
request_fuel.add('FUEL_TANK_RIGHT_MAIN_LEVEL', (b'FUEL TANK RIGHT MAIN LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
request_fuel.add('FUEL_TANK_RIGHT_AUX_LEVEL', (b'FUEL TANK RIGHT AUX LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
request_fuel.add('FUEL_TANK_RIGHT_TIP_LEVEL', (b'FUEL TANK RIGHT TIP LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
request_fuel.add('FUEL_TANK_EXTERNAL1_LEVEL', (b'FUEL TANK EXTERNAL1 LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
request_fuel.add('FUEL_TANK_EXTERNAL2_LEVEL', (b'FUEL TANK EXTERNAL2 LEVEL', b'Percent Over 100'))  # Percent of maximum capacity
request_fuel.add('FUEL_TANK_CENTER_CAPACITY', (b'FUEL TANK CENTER CAPACITY', b'Gallons'))  # Maximum capacity in volume
request_fuel.add('FUEL_TANK_CENTER2_CAPACITY', (b'FUEL TANK CENTER2 CAPACITY', b'Gallons'))  # Maximum capacity in volume
request_fuel.add('FUEL_TANK_CENTER3_CAPACITY', (b'FUEL TANK CENTER3 CAPACITY', b'Gallons'))  # Maximum capacity in volume
request_fuel.add('FUEL_TANK_LEFT_MAIN_CAPACITY', (b'FUEL TANK LEFT MAIN CAPACITY', b'Gallons'))  # Maximum capacity in volume
request_fuel.add('FUEL_TANK_LEFT_AUX_CAPACITY', (b'FUEL TANK LEFT AUX CAPACITY', b'Gallons'))  # Maximum capacity in volume
request_fuel.add('FUEL_TANK_LEFT_TIP_CAPACITY', (b'FUEL TANK LEFT TIP CAPACITY', b'Gallons'))  # Maximum capacity in volume
request_fuel.add('FUEL_TANK_RIGHT_MAIN_CAPACITY', (b'FUEL TANK RIGHT MAIN CAPACITY', b'Gallons'))  # Maximum capacity in volume
request_fuel.add('FUEL_TANK_RIGHT_AUX_CAPACITY', (b'FUEL TANK RIGHT AUX CAPACITY', b'Gallons'))  # Maximum capacity in volume
request_fuel.add('FUEL_TANK_RIGHT_TIP_CAPACITY', (b'FUEL TANK RIGHT TIP CAPACITY', b'Gallons'))  # Maximum capacity in volume
request_fuel.add('FUEL_TANK_EXTERNAL1_CAPACITY', (b'FUEL TANK EXTERNAL1 CAPACITY', b'Gallons'))  # Maximum capacity in volume
request_fuel.add('FUEL_TANK_EXTERNAL2_CAPACITY', (b'FUEL TANK EXTERNAL2 CAPACITY', b'Gallons'))  # Maximum capacity in volume
request_fuel.add('FUEL_LEFT_CAPACITY', (b'FUEL LEFT CAPACITY', b'Gallons'))  # Maximum capacity in volume
request_fuel.add('FUEL_RIGHT_CAPACITY', (b'FUEL RIGHT CAPACITY', b'Gallons'))  # Maximum capacity in volume
request_fuel.add('FUEL_TANK_CENTER_QUANTITY', (b'FUEL TANK CENTER QUANTITY', b'Gallons'))  # Current quantity in volume
request_fuel.add('FUEL_TANK_CENTER2_QUANTITY', (b'FUEL TANK CENTER2 QUANTITY', b'Gallons'))  # Current quantity in volume
request_fuel.add('FUEL_TANK_CENTER3_QUANTITY', (b'FUEL TANK CENTER3 QUANTITY', b'Gallons'))  # Current quantity in volume
request_fuel.add('FUEL_TANK_LEFT_MAIN_QUANTITY', (b'FUEL TANK LEFT MAIN QUANTITY', b'Gallons'))  # Current quantity in volume
request_fuel.add('FUEL_TANK_LEFT_AUX_QUANTITY', (b'FUEL TANK LEFT AUX QUANTITY', b'Gallons'))  # Current quantity in volume
request_fuel.add('FUEL_TANK_LEFT_TIP_QUANTITY', (b'FUEL TANK LEFT TIP QUANTITY', b'Gallons'))  # Current quantity in volume
request_fuel.add('FUEL_TANK_RIGHT_MAIN_QUANTITY', (b'FUEL TANK RIGHT MAIN QUANTITY', b'Gallons'))  # Current quantity in volume
request_fuel.add('FUEL_TANK_RIGHT_AUX_QUANTITY', (b'FUEL TANK RIGHT AUX QUANTITY', b'Gallons'))  # Current quantity in volume
request_fuel.add('FUEL_TANK_RIGHT_TIP_QUANTITY', (b'FUEL TANK RIGHT TIP QUANTITY', b'Gallons'))  # Current quantity in volume
request_fuel.add('FUEL_TANK_EXTERNAL1_QUANTITY', (b'FUEL TANK EXTERNAL1 QUANTITY', b'Gallons'))  # Current quantity in volume
request_fuel.add('FUEL_TANK_EXTERNAL2_QUANTITY', (b'FUEL TANK EXTERNAL2 QUANTITY', b'Gallons'))  # Current quantity in volume
request_fuel.add('FUEL_LEFT_QUANTITY', (b'FUEL LEFT QUANTITY', b'Gallons'))  # Current quantity in volume
request_fuel.add('FUEL_RIGHT_QUANTITY', (b'FUEL RIGHT QUANTITY', b'Gallons'))  # Current quantity in volume
request_fuel.add('FUEL_TOTAL_QUANTITY', (b'FUEL TOTAL QUANTITY', b'Gallons'))  # Current quantity in volume
request_fuel.add('FUEL_WEIGHT_PER_GALLON', (b'FUEL WEIGHT PER GALLON', b'Pounds'))  # Fuel weight per gallon
request_fuel.add('FUEL_TOTAL_CAPACITY', (b'FUEL TOTAL CAPACITY', b'Gallons'))  # Total capacity of the aircraft
request_fuel.add('FUEL_SELECTED_QUANTITY_PERCENT', (b'FUEL SELECTED QUANTITY PERCENT', b'Percent Over 100'))  # Percent or capacity for selected tank
request_fuel.add('FUEL_SELECTED_QUANTITY', (b'FUEL SELECTED QUANTITY', b'Gallons'))  # Quantity of selected tank
request_fuel.add('FUEL_TOTAL_QUANTITY_WEIGHT', (b'FUEL TOTAL QUANTITY WEIGHT', b'Pounds'))  # Current total fuel weight of the aircraft
request_fuel.add('NUM_FUEL_SELECTORS', (b'NUM FUEL SELECTORS', b'Number'))  # Number of selectors on the aircraft
request_fuel.add('UNLIMITED_FUEL', (b'UNLIMITED FUEL', b'Bool'))  # Unlimited fuel flag
request_fuel.add('ESTIMATED_FUEL_FLOW', (b'ESTIMATED FUEL FLOW', b'Pounds per hour'))  # Estimated fuel flow at cruise

request_flaps = sm.new_request_holder()
request_flaps.add('FLAPS_HANDLE_PERCENT', (b'FLAPS HANDLE PERCENT', b'Percent Over 100'))  # Percent flap handle extended
request_flaps.add('FLAPS_HANDLE_INDEX', (b'FLAPS HANDLE INDEX', b'Number'))  # Index of current flap position
request_flaps.add('FLAPS_NUM_HANDLE_POSITIONS', (b'FLAPS NUM HANDLE POSITIONS', b'Number'))  # Number of flap positions
request_flaps.add('TRAILING_EDGE_FLAPS_LEFT_PERCENT', (b'TRAILING EDGE FLAPS LEFT PERCENT', b'Percent Over 100'))  # Percent left trailing edge flap extended
request_flaps.add('TRAILING_EDGE_FLAPS_RIGHT_PERCENT', (b'TRAILING EDGE FLAPS RIGHT PERCENT', b'Percent Over 100'))  # Percent right trailing edge flap extended
request_flaps.add('TRAILING_EDGE_FLAPS_LEFT_ANGLE', (b'TRAILING EDGE FLAPS LEFT ANGLE', b'Radians'))  # Angle left trailing edge flap extended. Use TRAILING EDGE FLAPS LEFT PERCENT to set a value.
request_flaps.add('TRAILING_EDGE_FLAPS_RIGHT_ANGLE', (b'TRAILING EDGE FLAPS RIGHT ANGLE', b'Radians'))  # Angle right trailing edge flap extended. Use TRAILING EDGE FLAPS RIGHT PERCENT to set a value.
request_flaps.add('LEADING_EDGE_FLAPS_LEFT_PERCENT', (b'LEADING EDGE FLAPS LEFT PERCENT', b'Percent Over 100'))  # Percent left leading edge flap extended
request_flaps.add('LEADING_EDGE_FLAPS_RIGHT_PERCENT', (b'LEADING EDGE FLAPS RIGHT PERCENT', b'Percent Over 100'))  # Percent right leading edge flap extended
request_flaps.add('LEADING_EDGE_FLAPS_LEFT_ANGLE', (b'LEADING EDGE FLAPS LEFT ANGLE', b'Radians'))  # Angle left leading edge flap extended. Use LEADING EDGE FLAPS LEFT PERCENT to set a value.
request_flaps.add('LEADING_EDGE_FLAPS_RIGHT_ANGLE', (b'LEADING EDGE FLAPS RIGHT ANGLE', b'Radians'))  # Angle right leading edge flap extended. Use LEADING EDGE FLAPS RIGHT PERCENT to set a value.
request_flaps.add('FLAPS_AVAILABLE', (b'FLAPS AVAILABLE', b'Bool'))  # True if flaps available
request_flaps.add('FLAP_DAMAGE_BY_SPEED', (b'FLAP DAMAGE BY SPEED', b'Bool'))  # True if flagps are damaged by excessive speed
request_flaps.add('FLAP_SPEED_EXCEEDED', (b'FLAP SPEED EXCEEDED', b'Bool'))  # True if safe speed limit for flaps exceeded

request_throttle = sm.new_request_holder()
request_throttle.add('AUTOPILOT_THROTTLE_ARM', (b'AUTOPILOT THROTTLE ARM', b'Bool'))  # Autothrottle armed
request_throttle.add('AUTOPILOT_TAKEOFF_POWER_ACTIVE', (b'AUTOPILOT TAKEOFF POWER ACTIVE', b'Bool'))  # Takeoff / Go Around power mode active
request_throttle.add('AUTOTHROTTLE_ACTIVE', (b'AUTOTHROTTLE ACTIVE', b'Bool'))  # Auto-throttle active
request_throttle.add('FULL_THROTTLE_THRUST_TO_WEIGHT_RATIO', (b'FULL THROTTLE THRUST TO WEIGHT RATIO', b'Number'))  # Full throttle thrust to weight ratio
request_throttle.add('THROTTLE_LOWER_LIMIT', (b'THROTTLE LOWER LIMIT', b'Percent'))  # Percent throttle defining lower limit (negative for reverse thrust equipped airplanes)
request_throttle.add('GENERAL_ENG_THROTTLE_LEVER_POSITION:index', (b'GENERAL ENG THROTTLE LEVER POSITION:index', b'Percent'))  # Percent of max throttle position
request_throttle.add('AUTOPILOT_THROTTLE_ARM', (b'AUTOPILOT THROTTLE ARM', b'Bool'))  # Autothrottle armed
request_throttle.add('AUTOTHROTTLE_ACTIVE', (b'AUTOTHROTTLE ACTIVE', b'Bool'))  # Auto-throttle active
request_throttle.add('FULL_THROTTLE_THRUST_TO_WEIGHT_RATIO', (b'FULL THROTTLE THRUST TO WEIGHT RATIO', b'Number'))  # Full throttle thrust to weight ratio

request_gear = sm.new_request_holder()
request_gear.add('IS_GEAR_RETRACTABLE', (b'IS GEAR RETRACTABLE', b'Bool'))  # True if gear can be retracted
request_gear.add('IS_GEAR_SKIS', (b'IS GEAR SKIS', b'Bool'))  # True if landing gear is skis
request_gear.add('IS_GEAR_FLOATS', (b'IS GEAR FLOATS', b'Bool'))  # True if landing gear is floats
request_gear.add('IS_GEAR_SKIDS', (b'IS GEAR SKIDS', b'Bool'))  # True if landing gear is skids
request_gear.add('IS_GEAR_WHEELS', (b'IS GEAR WHEELS', b'Bool'))  # True if landing gear is wheels
request_gear.add('GEAR_HANDLE_POSITION', (b'GEAR HANDLE POSITION', b'Bool'))  # True if gear handle is applied
request_gear.add('GEAR_HYDRAULIC_PRESSURE', (b'GEAR HYDRAULIC PRESSURE', b'Pound force per square foot (psf)'))  # Gear hydraulic pressure
request_gear.add('TAILWHEEL_LOCK_ON', (b'TAILWHEEL LOCK ON', b'Bool'))  # True if tailwheel lock applied
request_gear.add('GEAR_CENTER_POSITION', (b'GEAR CENTER POSITION', b'Percent Over 100'))  # Percent center gear extended
request_gear.add('GEAR_LEFT_POSITION', (b'GEAR LEFT POSITION', b'Percent Over 100'))  # Percent left gear extended
request_gear.add('GEAR_RIGHT_POSITION', (b'GEAR RIGHT POSITION', b'Percent Over 100'))  # Percent right gear extended
request_gear.add('GEAR_TAIL_POSITION', (b'GEAR TAIL POSITION', b'Percent Over 100'))  # Percent tail gear extended
request_gear.add('GEAR_AUX_POSITION', (b'GEAR AUX POSITION', b'Percent Over 100'))  # Percent auxiliary gear extended
request_gear.add('GEAR_TOTAL_PCT_EXTENDED', (b'GEAR TOTAL PCT EXTENDED', b'Percentage'))  # Percent total gear extended
request_gear.add('AUTO_BRAKE_SWITCH_CB', (b'AUTO BRAKE SWITCH CB', b'Number'))  # Auto brake switch position
request_gear.add('WATER_RUDDER_HANDLE_POSITION', (b'WATER RUDDER HANDLE POSITION', b'Percent Over 100'))  # Position of the water rudder handle (0 handle retracted, 100 rudder handle applied)
request_gear.add('WATER_LEFT_RUDDER_EXTENDED', (b'WATER LEFT RUDDER EXTENDED', b'Percentage'))  # Percent extended
request_gear.add('WATER_RIGHT_RUDDER_EXTENDED', (b'WATER RIGHT RUDDER EXTENDED', b'Percentage'))  # Percent extended
request_gear.add('GEAR_CENTER_STEER_ANGLE', (b'GEAR CENTER STEER ANGLE', b'Percent Over 100'))  # Center wheel angle, negative to the left, positive to the right.
request_gear.add('GEAR_LEFT_STEER_ANGLE', (b'GEAR LEFT STEER ANGLE', b'Percent Over 100'))  # Left wheel angle, negative to the left, positive to the right.
request_gear.add('GEAR_RIGHT_STEER_ANGLE', (b'GEAR RIGHT STEER ANGLE', b'Percent Over 100'))  # Right wheel angle, negative to the left, positive to the right.
request_gear.add('GEAR_AUX_STEER_ANGLE', (b'GEAR AUX STEER ANGLE', b'Percent Over 100'))  # Aux wheel angle, negative to the left, positive to the right. The aux wheel is the fourth set of gear, sometimes used on helicopters.
request_gear.add('WATER_LEFT_RUDDER_STEER_ANGLE', (b'WATER LEFT RUDDER STEER ANGLE', b'Percent Over 100'))  # Water left rudder angle, negative to the left, positive to the right.
request_gear.add('WATER_RIGHT_RUDDER_STEER_ANGLE', (b'WATER RIGHT RUDDER STEER ANGLE', b'Percent Over 100'))  # Water right rudder angle, negative to the left, positive to the right.
request_gear.add('GEAR_CENTER_STEER_ANGLE_PCT', (b'GEAR CENTER STEER ANGLE PCT', b'Percent Over 100'))  # Center steer angle as a percentage
request_gear.add('GEAR_LEFT_STEER_ANGLE_PCT', (b'GEAR LEFT STEER ANGLE PCT', b'Percent Over 100'))  # Left steer angle as a percentage
request_gear.add('GEAR_RIGHT_STEER_ANGLE_PCT', (b'GEAR RIGHT STEER ANGLE PCT', b'Percent Over 100'))  # Right steer angle as a percentage
request_gear.add('GEAR_AUX_STEER_ANGLE_PCT', (b'GEAR AUX STEER ANGLE PCT', b'Percent Over 100'))  # Aux steer angle as a percentage
request_gear.add('WATER_LEFT_RUDDER_STEER_ANGLE_PCT', (b'WATER LEFT RUDDER STEER ANGLE PCT', b'Percent Over 100'))  # Water left rudder angle as a percentage
request_gear.add('WATER_RIGHT_RUDDER_STEER_ANGLE_PCT', (b'WATER RIGHT RUDDER STEER ANGLE PCT', b'Percent Over 100'))  # Water right rudder as a percentage
request_gear.add('CENTER_WHEEL_RPM', (b'CENTER WHEEL RPM', b'Rpm'))  # Center landing gear rpm
request_gear.add('LEFT_WHEEL_RPM', (b'LEFT WHEEL RPM', b'Rpm'))  # Left landing gear rpm
request_gear.add('RIGHT_WHEEL_RPM', (b'RIGHT WHEEL RPM', b'Rpm'))  # Right landing gear rpm
request_gear.add('AUX_WHEEL_RPM', (b'AUX WHEEL RPM', b'Rpm'))  # Rpm of fourth set of gear wheels.
request_gear.add('CENTER_WHEEL_ROTATION_ANGLE', (b'CENTER WHEEL ROTATION ANGLE', b'Radians'))  # Center wheel rotation angle
request_gear.add('LEFT_WHEEL_ROTATION_ANGLE', (b'LEFT WHEEL ROTATION ANGLE', b'Radians'))  # Left wheel rotation angle
request_gear.add('RIGHT_WHEEL_ROTATION_ANGLE', (b'RIGHT WHEEL ROTATION ANGLE', b'Radians'))  # Right wheel rotation angle
request_gear.add('AUX_WHEEL_ROTATION_ANGLE', (b'AUX WHEEL ROTATION ANGLE', b'Radians'))  # Aux wheel rotation angle
request_gear.add('GEAR_EMERGENCY_HANDLE_POSITION', (b'GEAR EMERGENCY HANDLE POSITION', b'Bool'))  # True if gear emergency handle applied
request_gear.add('ANTISKID_BRAKES_ACTIVE', (b'ANTISKID BRAKES ACTIVE', b'Bool'))  # True if antiskid brakes active
request_gear.add('RETRACT_FLOAT_SWITCH', (b'RETRACT FLOAT SWITCH', b'Bool'))  # True if retract float switch on
request_gear.add('RETRACT_LEFT_FLOAT_EXTENDED', (b'RETRACT LEFT FLOAT EXTENDED', b'Percent (0 is fully retracted, 100 is fully extended)'))  # If aircraft has retractable floats.
request_gear.add('RETRACT_RIGHT_FLOAT_EXTENDED', (b'RETRACT RIGHT FLOAT EXTENDED', b'Percent (0 is fully retracted, 100 is fully extended)'))  # If aircraft has retractable floats.
request_gear.add('STEER_INPUT_CONTROL', (b'STEER INPUT CONTROL', b'Percent over 100'))  # Position of steering tiller
request_gear.add('GEAR_DAMAGE_BY_SPEED', (b'GEAR DAMAGE BY SPEED', b'Bool'))  # True if gear has been damaged by excessive speed
request_gear.add('GEAR_SPEED_EXCEEDED', (b'GEAR SPEED EXCEEDED', b'Bool'))  # True if safe speed limit for gear exceeded
request_gear.add('NOSEWHEEL_LOCK_ON', (b'NOSEWHEEL LOCK ON', b'Bool'))  # True if the nosewheel lock is engaged.

request_trim = sm.new_request_holder()
request_trim.add('ROTOR_LATERAL_TRIM_PCT', (b'ROTOR LATERAL TRIM PCT', b'Percent Over 100'))  # Trim percent
request_trim.add('ELEVATOR_TRIM_POSITION', (b'ELEVATOR TRIM POSITION', b'Radians'))  # Elevator trim deflection
request_trim.add('ELEVATOR_TRIM_INDICATOR', (b'ELEVATOR TRIM INDICATOR', b'Position (-16K to 0) -16K = full down'))  # Percent elevator trim (for indication)
request_trim.add('ELEVATOR_TRIM_PCT', (b'ELEVATOR TRIM PCT', b'Percent Over 100'))  # Percent elevator trim
request_trim.add('AILERON_TRIM', (b'AILERON TRIM', b'Radians'))  # Angle deflection
request_trim.add('AILERON_TRIM_PCT', (b'AILERON TRIM PCT', b'Float. Percent over 100'))  # The trim position of the ailerons. Zero is fully retracted.
request_trim.add('RUDDER_TRIM_PCT', (b'RUDDER TRIM PCT', b'Float. Percent over 100'))  # The trim position of the rudder. Zero is no trim.
request_trim.add('RUDDER_TRIM', (b'RUDDER TRIM', b'Radians'))  # Angle deflection

request_autopilot = sm.new_request_holder()
request_autopilot.add('AUTOPILOT_MASTER', (b'AUTOPILOT MASTER', b'Bool'))
request_autopilot.add('AUTOPILOT_AVAILABLE', (b'AUTOPILOT AVAILABLE', b'Bool'))
request_autopilot.add('AUTOPILOT_NAV_SELECTED', (b'AUTOPILOT NAV SELECTED', b'Number'))
request_autopilot.add('AUTOPILOT_WING_LEVELER', (b'AUTOPILOT WING LEVELER', b'Bool'))
request_autopilot.add('AUTOPILOT_NAV1_LOCK', (b'AUTOPILOT NAV1 LOCK', b'Bool'))
request_autopilot.add('AUTOPILOT_HEADING_LOCK', (b'AUTOPILOT HEADING LOCK', b'Bool'))
request_autopilot.add('AUTOPILOT_HEADING_LOCK_DIR', (b'AUTOPILOT HEADING LOCK DIR', b'Degrees'))
request_autopilot.add('AUTOPILOT_ALTITUDE_LOCK', (b'AUTOPILOT ALTITUDE LOCK', b'Bool'))
request_autopilot.add('AUTOPILOT_ALTITUDE_LOCK_VAR', (b'AUTOPILOT ALTITUDE LOCK VAR', b'Feet'))
request_autopilot.add('AUTOPILOT_ATTITUDE_HOLD', (b'AUTOPILOT ATTITUDE HOLD', b'Bool'))
request_autopilot.add('AUTOPILOT_GLIDESLOPE_HOLD', (b'AUTOPILOT GLIDESLOPE HOLD', b'Bool'))
request_autopilot.add('AUTOPILOT_PITCH_HOLD_REF', (b'AUTOPILOT PITCH HOLD REF', b'Radians'))
request_autopilot.add('AUTOPILOT_APPROACH_HOLD', (b'AUTOPILOT APPROACH HOLD', b'Bool'))
request_autopilot.add('AUTOPILOT_BACKCOURSE_HOLD', (b'AUTOPILOT BACKCOURSE HOLD', b'Bool'))
request_autopilot.add('AUTOPILOT_VERTICAL_HOLD_VAR', (b'AUTOPILOT VERTICAL HOLD VAR', b'Feet/minute'))
request_autopilot.add('AUTOPILOT_PITCH_HOLD', (b'AUTOPILOT PITCH HOLD', b'Bool'))
request_autopilot.add('AUTOPILOT_FLIGHT_DIRECTOR_ACTIVE', (b'AUTOPILOT FLIGHT DIRECTOR ACTIVE', b'Bool'))
request_autopilot.add('AUTOPILOT_FLIGHT_DIRECTOR_PITCH', (b'AUTOPILOT FLIGHT DIRECTOR PITCH', b'Radians'))
request_autopilot.add('AUTOPILOT_FLIGHT_DIRECTOR_BANK', (b'AUTOPILOT FLIGHT DIRECTOR BANK', b'Radians'))
request_autopilot.add('AUTOPILOT_AIRSPEED_HOLD', (b'AUTOPILOT AIRSPEED HOLD', b'Bool'))
request_autopilot.add('AUTOPILOT_AIRSPEED_HOLD_VAR', (b'AUTOPILOT AIRSPEED HOLD VAR', b'Knots'))
request_autopilot.add('AUTOPILOT_MACH_HOLD', (b'AUTOPILOT MACH HOLD', b'Bool'))
request_autopilot.add('AUTOPILOT_MACH_HOLD_VAR', (b'AUTOPILOT MACH HOLD VAR', b'Number'))
request_autopilot.add('AUTOPILOT_YAW_DAMPER', (b'AUTOPILOT YAW DAMPER', b'Bool'))
request_autopilot.add('AUTOPILOT_RPM_HOLD_VAR', (b'AUTOPILOT RPM HOLD VAR', b'Number'))
request_autopilot.add('AUTOPILOT_THROTTLE_ARM', (b'AUTOPILOT THROTTLE ARM', b'Bool'))
request_autopilot.add('AUTOPILOT_TAKEOFF_POWER ACTIVE', (b'AUTOPILOT TAKEOFF POWER ACTIVE', b'Bool'))
request_autopilot.add('AUTOTHROTTLE_ACTIVE', (b'AUTOTHROTTLE ACTIVE', b'Bool'))
request_autopilot.add('AUTOPILOT_VERTICAL_HOLD', (b'AUTOPILOT VERTICAL HOLD', b'Bool'))
request_autopilot.add('AUTOPILOT_RPM_HOLD', (b'AUTOPILOT RPM HOLD', b'Bool'))
request_autopilot.add('AUTOPILOT_MAX_BANK', (b'AUTOPILOT MAX BANK', b'Radians'))
request_autopilot.add('FLY_BY_WIRE_ELAC_SWITCH', (b'FLY BY WIRE ELAC SWITCH', b'Bool'))
request_autopilot.add('FLY_BY_WIRE_FAC_SWITCH', (b'FLY BY WIRE FAC SWITCH', b'Bool'))
request_autopilot.add('FLY_BY_WIRE_SEC_SWITCH', (b'FLY BY WIRE SEC SWITCH', b'Bool'))
request_autopilot.add('FLY_BY_WIRE_ELAC_FAILED', (b'FLY BY WIRE ELAC FAILED', b'Bool'))
request_autopilot.add('FLY_BY_WIRE_FAC_FAILED', (b'FLY BY WIRE FAC FAILED', b'Bool'))
request_autopilot.add('FLY_BY_WIRE_SEC_FAILED', (b'FLY BY WIRE SEC FAILED', b'Bool'))


def thousandify(x):
    return f"{x:,}"


@app.route('/')
def glass():
    return render_template("glass.html")


def get_dataset(data_type):
    if data_type == "navigation": request_to_action = request_location
    if data_type == "airspeed": request_to_action = request_airspeed
    if data_type == "compass": request_to_action = request_compass
    if data_type == "vertical_speed": request_to_action = request_vertical_speed
    if data_type == "fuel": request_to_action = request_fuel
    if data_type == "flaps": request_to_action = request_flaps
    if data_type == "throttle": request_to_action = request_throttle
    if data_type == "gear": request_to_action = request_gear
    if data_type == "trim": request_to_action = request_trim
    if data_type == "autopilot": request_to_action = request_autopilot
    if data_type == "ui": request_to_action = request_ui

    return request_to_action


@app.route('/ui')
def output_ui_variables():
    data_dictionary = get_dataset("ui")

    ui_friendly_dictionary = {}
    ui_friendly_dictionary["STATUS"] = "success"

    fuel_percentage = (data_dictionary.get("FUEL_TOTAL_QUANTITY") / data_dictionary.get("FUEL_TOTAL_CAPACITY")) * 100
    ui_friendly_dictionary["FUEL_PERCENTAGE"] = round(fuel_percentage)
    ui_friendly_dictionary["AIRSPEED_INDICATE"] = round(data_dictionary.get("AIRSPEED_INDICATE"))
    ui_friendly_dictionary["ALTITUDE"] = thousandify(round(data_dictionary.get("ALTITUDE")))
    ui_friendly_dictionary["FLAPS_HANDLE_PERCENT"] = round(data_dictionary.get("FLAPS_HANDLE_PERCENT")*100)

    if data_dictionary.get("GEAR_HANDLE_POSITION") == 1:
        ui_friendly_dictionary["GEAR_HANDLE_POSITION"] = "DOWN"
    else:
        ui_friendly_dictionary["GEAR_HANDLE_POSITION"] = "UP"

    ui_friendly_dictionary["LATITUDE"] = data_dictionary.get("LATITUDE")
    ui_friendly_dictionary["LONGITUDE"] = data_dictionary.get("LONGITUDE")

    ui_friendly_dictionary["MAGNETIC_COMPASS"] = round(data_dictionary.get("MAGNETIC_COMPASS"))
    ui_friendly_dictionary["VERTICAL_SPEED"] = round(data_dictionary.get("VERTICAL_SPEED"))

    ui_friendly_dictionary["AUTOPILOT_MASTER"] = data_dictionary.get("AUTOPILOT_MASTER")
    ui_friendly_dictionary["AUTOPILOT_NAV_SELECTED"] = data_dictionary.get("AUTOPILOT_NAV_SELECTED")
    ui_friendly_dictionary["AUTOPILOT_WING_LEVELER"] = data_dictionary.get("AUTOPILOT_WING_LEVELER")
    ui_friendly_dictionary["AUTOPILOT_HEADING_LOCK"] = data_dictionary.get("AUTOPILOT_HEADING_LOCK")
    ui_friendly_dictionary["AUTOPILOT_HEADING_LOCK_DIR"] = round(data_dictionary.get("AUTOPILOT_HEADING_LOCK_DIR"))
    ui_friendly_dictionary["AUTOPILOT_ALTITUDE_LOCK"] = data_dictionary.get("AUTOPILOT_ALTITUDE_LOCK")
    ui_friendly_dictionary["AUTOPILOT_ALTITUDE_LOCK_VAR"] = thousandify(round(data_dictionary.get("AUTOPILOT_ALTITUDE_LOCK_VAR")))
    ui_friendly_dictionary["AUTOPILOT_ATTITUDE_HOLD"] = data_dictionary.get("AUTOPILOT_ATTITUDE_HOLD")
    ui_friendly_dictionary["AUTOPILOT_GLIDESLOPE_HOLD"] = data_dictionary.get("AUTOPILOT_GLIDESLOPE_HOLD")
    ui_friendly_dictionary["AUTOPILOT_APPROACH_HOLD"] = data_dictionary.get("AUTOPILOT_APPROACH_HOLD")
    ui_friendly_dictionary["AUTOPILOT_BACKCOURSE_HOLD"] = data_dictionary.get("AUTOPILOT_BACKCOURSE_HOLD")
    ui_friendly_dictionary["AUTOPILOT_VERTICAL_HOLD"] = data_dictionary.get("AUTOPILOT_VERTICAL_HOLD")
    ui_friendly_dictionary["AUTOPILOT_VERTICAL_HOLD_VAR"] = data_dictionary.get("AUTOPILOT_VERTICAL_HOLD_VAR")
    ui_friendly_dictionary["AUTOPILOT_PITCH_HOLD"] = data_dictionary.get("AUTOPILOT_PITCH_HOLD")
    ui_friendly_dictionary["AUTOPILOT_PITCH_HOLD_REF"] = data_dictionary.get("AUTOPILOT_PITCH_HOLD_REF")
    ui_friendly_dictionary["AUTOPILOT_FLIGHT_DIRECTOR_ACTIVE"] = data_dictionary.get("AUTOPILOT_FLIGHT_DIRECTOR_ACTIVE")
    ui_friendly_dictionary["AUTOPILOT_AIRSPEED_HOLD"] = data_dictionary.get("AUTOPILOT_AIRSPEED_HOLD")
    ui_friendly_dictionary["AUTOPILOT_AIRSPEED_HOLD_VAR"] = round(data_dictionary.get("AUTOPILOT_AIRSPEED_HOLD_VAR"))

    return jsonify(ui_friendly_dictionary)


@app.route('/dataset/<dataset_name>/', methods=["GET"])
def output_detailed_json_data(dataset_name):

    data_dictionary = get_dataset(dataset_name)
    return jsonify(data_dictionary.json())


# NOT WORKING
@app.route('/datapoint/<datapoint_name>/get')
def get_datapoint_endpoint(datapoint_name):
    sm = SimConnect()

    request_set = sm.new_request_holder()
    request_set.add('thr', (b'GENERAL ENG THROTTLE LEVER POSITION:1', b'Percent'))

    print(request_ui.get("thr"))

    return


@app.route('/datapoint/<datapoint_name>/set', methods=["POST"])
def set_datapoint_endpoint(datapoint_name):

    value_to_use = request.form.get('value_to_use')

    if value_to_use is None:
        print(datapoint_name + ": " + "No value passed")
    else:
        print(datapoint_name + ": " + value_to_use)

    status = "success"
    return jsonify(status)


@app.route('/event/<event_name>/trigger', methods=["POST"])
def trigger_event(event_name):

    value_to_use = request.form.get('value_to_use')

    event_name_bytes = bytes(event_name, encoding='utf-8')

    sm = SimConnect()
    EVENT_TO_TRIGGER = Event(event_name_bytes, sm)

    if value_to_use is None:
        EVENT_TO_TRIGGER()
    else:
        pass

    sm.exit()

    status = "success"
    return jsonify(status)


app.run(host='0.0.0.0', port=5000, debug=True)