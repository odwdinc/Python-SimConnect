
class AircraftRequests():
	# NOTE AUTOGEN form SDK
	# Any AircraftRequests that has :index
	# need futher work and will return None
	# if Request.defined is false there was
	# errors with the Request definition.
	# Request.description hold a small dec of the Request

	def getall(self):
		for requ in list(self.__dict__):
			holder = getattr(self, requ)
			print(requ)
			for rq in holder.dic:
				(val, dec) = holder.get(rq, True)
				if val is None:
					continue
				print("\t%s: %f\n\t\t%s" % (rq, val, dec))

	def __init__(self, sm):
		self.Environment = sm.new_request_holder()
		self.Environment.add(
			'AMBIENT_DENSITY',
			(b'AMBIENT DENSITY', b'Slugs per cubic feet'),
			_dec='Ambient density'
		)
		self.Environment.add(
			'AMBIENT_TEMPERATURE',
			(b'AMBIENT TEMPERATURE', b'Celsius'),
			_dec='Ambient temperature'
		)
		self.Environment.add(
			'AMBIENT_PRESSURE',
			(b'AMBIENT PRESSURE', b'Inches of mercury, inHg'),
			_dec='Ambient pressure'
		)
		self.Environment.add(
			'AMBIENT_WIND_VELOCITY',
			(b'AMBIENT WIND VELOCITY', b'Knots'),
			_dec='Wind velocity'
		)
		self.Environment.add(
			'AMBIENT_WIND_DIRECTION',
			(b'AMBIENT WIND DIRECTION', b'Degrees'),
			_dec='Wind direction'
		)
		self.Environment.add(
			'AMBIENT_WIND_X',
			(b'AMBIENT WIND X', b'Meters per second'),
			_dec='Wind component in East/West direction.'
		)
		self.Environment.add(
			'AMBIENT_WIND_Y',
			(b'AMBIENT WIND Y', b'Meters per second'),
			_dec='Wind component in vertical direction.'
		)
		self.Environment.add(
			'AMBIENT_WIND_Z',
			(b'AMBIENT WIND Z', b'Meters per second'),
			_dec='Wind component in North/South direction.'
		)
		self.Environment.add(
			'STRUCT_AMBIENT_WIND',
			(b'STRUCT AMBIENT WIND', b'Feet_per_second'),
			_dec='''
			X (latitude),
			Y (vertical) and Z (longitude)
			components of the wind.'''
		)
		self.Environment.add(
			'AIRCRAFT_WIND_X',
			(b'AIRCRAFT WIND X', b'Knots'),
			_dec='Wind component in aircraft lateral axis'
		)
		self.Environment.add(
			'AIRCRAFT_WIND_Y',
			(b'AIRCRAFT WIND Y', b'Knots'),
			_dec='Wind component in aircraft vertical axis'
		)
		self.Environment.add(
			'AIRCRAFT_WIND_Z',
			(b'AIRCRAFT WIND Z', b'Knots'),
			_dec='Wind component in aircraft longitudinal axis'
		)
		self.Environment.add(
			'BAROMETER_PRESSURE',
			(b'BAROMETER PRESSURE', b'Millibars'),
			_dec='Barometric pressure'
		)
		self.Environment.add(
			'SEA_LEVEL_PRESSURE',
			(b'SEA LEVEL PRESSURE', b'Millibars'),
			_dec='Barometric pressure at sea level'
		)
		self.Environment.add(
			'TOTAL_AIR_TEMPERATURE',
			(b'TOTAL AIR TEMPERATURE', b'Celsius'),
			_dec='''
				Total air temperature is the air temperature
				at the front of the aircraft where the ram
				pressure from the speed of the aircraft
				is taken into account.'''
		)
		self.Environment.add(
			'WINDSHIELD_RAIN_EFFECT_AVAILABLE',
			(b'WINDSHIELD RAIN EFFECT AVAILABLE', b'Bool'),
			_dec='Is visual effect available on this aircraft'
		)
		self.Environment.add(
			'AMBIENT_IN_CLOUD',
			(b'AMBIENT IN CLOUD', b'Bool'),
			_dec='True if the aircraft is in a cloud.'
		)
		self.Environment.add(
			'AMBIENT_VISIBILITY',
			(b'AMBIENT VISIBILITY', b'Meters'),
			_dec='Ambient visibility'
		)
		self.Environment.add(
			'STANDARD_ATM_TEMPERATURE',
			(b'STANDARD ATM TEMPERATURE', b'Rankine'),
			_dec='Outside temperature on the standard ATM scale'
		)

		self.Engine = sm.new_request_holder()
		self.Engine.add(
			'NUMBER_OF_ENGINES',
			(b'NUMBER OF ENGINES', b'Number'),
			_dec='Number of engines (minimum 0, maximum 4)'
		)
		self.Engine.add(
			'THROTTLE_LOWER_LIMIT',
			(b'THROTTLE LOWER LIMIT', b'Percent'),
			_dec='''
				Percent throttle defining lower limit
				(negative for reverse thrust equipped airplanes)'''
		)
		self.Engine.add(
			'MASTER_IGNITION_SWITCH',
			(b'MASTER IGNITION SWITCH', b'Bool'),
			_dec='''
				Aircraft master ignition switch
				(grounds all engines magnetos)'''
		)
		self.Engine.add(
			'GENERAL_ENG_COMBUSTION:index',
			(b'GENERAL ENG COMBUSTION:index', b'Bool'),
			_dec='Combustion flag'
		)
		self.Engine.add(
			'GENERAL_ENG_MASTER_ALTERNATOR:index',
			(b'GENERAL ENG MASTER ALTERNATOR:index', b'Bool'),
			_dec='Alternator (generator) switch'
		)
		self.Engine.add(
			'GENERAL_ENG_FUEL_PUMP_SWITCH:index',
			(b'GENERAL ENG FUEL PUMP SWITCH:index', b'Bool'),
			_dec='Fuel pump switch'
		)
		self.Engine.add(
			'GENERAL_ENG_FUEL_PUMP_ON:index',
			(b'GENERAL ENG FUEL PUMP ON:index', b'Bool'),
			_dec='Fuel pump on/off'
		)
		self.Engine.add(
			'GENERAL_ENG_RPM:index',
			(b'GENERAL ENG RPM:index', b'Rpm'),
			_dec='Engine rpm'
		)
		self.Engine.add(
			'GENERAL_ENG_PCT_MAX_RPM:index',
			(b'GENERAL ENG PCT MAX RPM:index', b'Percent'),
			_dec='Percent of max rated rpm'
		)
		self.Engine.add(
			'GENERAL_ENG_MAX_REACHED_RPM:index',
			(b'GENERAL ENG MAX REACHED RPM:index', b'Rpm'),
			_dec='Maximum attained rpm'
		)
		self.Engine.add(
			'GENERAL_ENG_THROTTLE_LEVER_POSITION:index',
			(b'GENERAL ENG THROTTLE LEVER POSITION:index', b'Percent'),
			_dec='Percent of max throttle position'
		)
		self.Engine.add(
			'GENERAL_ENG_MIXTURE_LEVER_POSITION:index',
			(b'GENERAL ENG MIXTURE LEVER POSITION:index', b'Percent'),
			_dec='Percent of max mixture lever position'
		)
		self.Engine.add(
			'GENERAL_ENG_PROPELLER_LEVER_POSITION:index',
			(b'GENERAL ENG PROPELLER LEVER POSITION:index', b'Percent'),
			_dec='Percent of max prop lever position'
		)
		self.Engine.add(
			'GENERAL_ENG_STARTER:index',
			(b'GENERAL ENG STARTER:index', b'Bool'),
			_dec='Engine starter on/off'
		)
		self.Engine.add(
			'GENERAL_ENG_EXHAUST_GAS_TEMPERATURE:index',
			(b'GENERAL ENG EXHAUST GAS TEMPERATURE:index', b'Rankine'),
			_dec='Engine exhaust gas temperature.'
		)
		self.Engine.add(
			'GENERAL_ENG_OIL_PRESSURE:index',
			(b'GENERAL ENG OIL PRESSURE:index', b'Psf'),
			_dec='Engine oil pressure'
		)
		self.Engine.add(
			'GENERAL_ENG_OIL_LEAKED_PERCENT:index',
			(b'GENERAL ENG OIL LEAKED PERCENT:index', b'Percent'),
			_dec='Percent of max oil capacity leaked'
		)
		self.Engine.add(
			'GENERAL_ENG_COMBUSTION_SOUND_PERCENT:index',
			(b'GENERAL ENG COMBUSTION SOUND PERCENT:index', b'Percent'),
			_dec='Percent of maximum engine sound'
		)
		self.Engine.add(
			'GENERAL_ENG_DAMAGE_PERCENT:index',
			(b'GENERAL ENG DAMAGE PERCENT:index', b'Percent'),
			_dec='Percent of total engine damage'
		)
		self.Engine.add(
			'GENERAL_ENG_OIL_TEMPERATURE:index',
			(b'GENERAL ENG OIL TEMPERATURE:index', b'Rankine'),
			_dec='Engine oil temperature'
		)
		self.Engine.add(
			'GENERAL_ENG_FAILED:index',
			(b'GENERAL ENG FAILED:index', b'Bool'),
			_dec='Fail flag'
		)
		self.Engine.add(
			'GENERAL_ENG_GENERATOR_SWITCH:index',
			(b'GENERAL ENG GENERATOR SWITCH:index', b'Bool'),
			_dec='Alternator (generator) switch'
		)
		self.Engine.add(
			'GENERAL_ENG_GENERATOR_ACTIVE:index',
			(b'GENERAL ENG GENERATOR ACTIVE:index', b'Bool'),
			_dec='Alternator (generator) on/off'
		)
		self.Engine.add(
			'GENERAL_ENG_ANTI_ICE_POSITION:index',
			(b'GENERAL ENG ANTI ICE POSITION:index', b'Bool'),
			_dec='Engine anti-ice switch'
		)
		self.Engine.add(
			'GENERAL_ENG_FUEL_VALVE:index',
			(b'GENERAL ENG FUEL VALVE:index', b'Bool'),
			_dec='Fuel valve state'
		)
		self.Engine.add(
			'GENERAL_ENG_FUEL_PRESSURE:index',
			(b'GENERAL ENG FUEL PRESSURE:index', b'Psi'),
			_dec='Engine fuel pressure'
		)
		self.Engine.add(
			'GENERAL_ENG_ELAPSED_TIME:index',
			(b'GENERAL ENG ELAPSED TIME:index', b'Hours'),
			_dec='Total engine elapsed time'
		)
		self.Engine.add(
			'RECIP_ENG_COWL_FLAP_POSITION:index',
			(b'RECIP ENG COWL FLAP POSITION:index', b'Percent'),
			_dec='Percent cowl flap opened'
		)
		self.Engine.add(
			'RECIP_ENG_PRIMER:index',
			(b'RECIP ENG PRIMER:index', b'Bool'),
			_dec='Engine primer position'
		)
		self.Engine.add(
			'RECIP_ENG_MANIFOLD_PRESSURE:index',
			(b'RECIP ENG MANIFOLD PRESSURE:index', b'Psi'),
			_dec='Engine manifold pressure'
		)
		self.Engine.add(
			'RECIP_ENG_ALTERNATE_AIR_POSITION:index',
			(b'RECIP ENG ALTERNATE AIR POSITION:index', b'Position'),
			_dec='Alternate air control'
		)
		self.Engine.add(
			'RECIP_ENG_COOLANT_RESERVOIR_PERCENT:index',
			(b'RECIP ENG COOLANT RESERVOIR PERCENT:index', b'Percent'),
			_dec='Percent coolant available'
		)
		self.Engine.add(
			'RECIP_ENG_LEFT_MAGNETO:index',
			(b'RECIP ENG LEFT MAGNETO:index', b'Bool'),
			_dec='Left magneto state'
		)
		self.Engine.add(
			'RECIP_ENG_RIGHT_MAGNETO:index',
			(b'RECIP ENG RIGHT MAGNETO:index', b'Bool'),
			_dec='Right magneto state'
		)
		self.Engine.add(
			'RECIP_ENG_BRAKE_POWER:index',
			(b'RECIP ENG BRAKE POWER:index', b'Foot pounds per second'),
			_dec='Brake power produced by engine'
		)
		self.Engine.add(
			'RECIP_ENG_STARTER_TORQUE:index',
			(b'RECIP ENG STARTER TORQUE:index', b'Foot pound'),
			_dec='Torque produced by engine'
		)
		self.Engine.add(
			'RECIP_ENG_TURBOCHARGER_FAILED:index',
			(b'RECIP ENG TURBOCHARGER FAILED:index', b'Bool'),
			_dec='Turbo failed state'
		)
		self.Engine.add(
			'RECIP_ENG_EMERGENCY_BOOST_ACTIVE:index',
			(b'RECIP ENG EMERGENCY BOOST ACTIVE:index', b'Bool'),
			_dec='War emergency power active'
		)
		self.Engine.add(
			'RECIP_ENG_EMERGENCY_BOOST_ELAPSED_TIME:index',
			(b'RECIP ENG EMERGENCY BOOST ELAPSED TIME:index', b'Hours'),
			_dec='Elapsed time war emergency power active'
		)
		self.Engine.add(
			'RECIP_ENG_WASTEGATE_POSITION:index',
			(b'RECIP ENG WASTEGATE POSITION:index', b'Percent'),
			_dec='Percent turbo wastegate closed'
		)
		self.Engine.add(
			'RECIP_ENG_TURBINE_INLET_TEMPERATURE:index',
			(b'RECIP ENG TURBINE INLET TEMPERATURE:index', b'Celsius'),
			_dec='Engine turbine inlet temperature'
		)
		self.Engine.add(
			'RECIP_ENG_CYLINDER_HEAD_TEMPERATURE:index',
			(b'RECIP ENG CYLINDER HEAD TEMPERATURE:index', b'Celsius'),
			_dec='Engine cylinder head temperature'
		)
		self.Engine.add(
			'RECIP_ENG_RADIATOR_TEMPERATURE:index',
			(b'RECIP ENG RADIATOR TEMPERATURE:index', b'Celsius'),
			_dec='Engine radiator temperature'
		)
		self.Engine.add(
			'RECIP_ENG_FUEL_AVAILABLE:index',
			(b'RECIP ENG FUEL AVAILABLE:index', b'Bool'),
			_dec='True if fuel is available'
		)
		self.Engine.add(
			'RECIP_ENG_FUEL_FLOW:index',
			(b'RECIP ENG FUEL FLOW:index', b'Pounds per hour'),
			_dec='Engine fuel flow'
		)
		self.Engine.add(
			'RECIP_ENG_FUEL_TANK_SELECTOR:index',
			(b'RECIP ENG FUEL TANK SELECTOR:index', b'Enum'),
			_dec='Fuel tank selected for engine. See fuel tank list.'
		)
		self.Engine.add(
			'RECIP_ENG_FUEL_NUMBER_TANKS_USED:index',
			(b'RECIP ENG FUEL NUMBER TANKS USED:index', b'Number'),
			_dec='Number of tanks currently being used'
		)
		self.Engine.add(
			'RECIP_CARBURETOR_TEMPERATURE:index',
			(b'RECIP CARBURETOR TEMPERATURE:index', b'Celsius'),
			_dec='Carburetor temperature'
		)
		self.Engine.add(
			'RECIP_MIXTURE_RATIO:index',
			(b'RECIP MIXTURE RATIO:index', b'Ratio'),
			_dec='Fuel / Air mixture ratio'
		)
		self.Engine.add(
			'TURB_ENG_N1:index',
			(b'TURB ENG N1:index', b'Percent'),
			_dec='Turbine engine N1'
		)
		self.Engine.add(
			'TURB_ENG_N2:index',
			(b'TURB ENG N2:index', b'Percent'),
			_dec='Turbine engine N2'
		)
		self.Engine.add(
			'TURB_ENG_CORRECTED_N1:index',
			(b'TURB ENG CORRECTED N1:index', b'Percent'),
			_dec='Turbine engine corrected N1'
		)
		self.Engine.add(
			'TURB_ENG_CORRECTED_N2:index',
			(b'TURB ENG CORRECTED N2:index', b'Percent'),
			_dec='Turbine engine corrected N2'
		)
		self.Engine.add(
			'TURB_ENG_CORRECTED_FF:index',
			(b'TURB ENG CORRECTED FF:index', b'Pounds per hour'),
			_dec='Corrected fuel flow'
		)
		self.Engine.add(
			'TURB_ENG_MAX_TORQUE_PERCENT:index',
			(b'TURB ENG MAX TORQUE PERCENT:index', b'Percent'),
			_dec='Percent of max rated torque'
		)
		self.Engine.add(
			'TURB_ENG_PRESSURE_RATIO:index',
			(b'TURB ENG PRESSURE RATIO:index', b'Ratio'),
			_dec='Engine pressure ratio'
		)
		self.Engine.add(
			'TURB_ENG_ITT:index',
			(b'TURB ENG ITT:index', b'Rankine'),
			_dec='Engine ITT'
		)
		self.Engine.add(
			'TURB_ENG_AFTERBURNER:index',
			(b'TURB ENG AFTERBURNER:index', b'Bool'),
			_dec='Afterburner state'
		)
		self.Engine.add(
			'TURB_ENG_JET_THRUST:index',
			(b'TURB ENG JET THRUST:index', b'Pounds'),
			_dec='Engine jet thrust'
		)
		self.Engine.add(
			'TURB_ENG_BLEED_AIR:index',
			(b'TURB ENG BLEED AIR:index', b'Psi'),
			_dec='Bleed air pressure'
		)
		self.Engine.add(
			'TURB_ENG_TANK_SELECTOR:index',
			(b'TURB ENG TANK SELECTOR:index', b'Enum'),
			_dec='Fuel tank selected for engine. See fuel tank list.'
		)
		self.Engine.add(
			'TURB_ENG_NUM_TANKS_USED:index',
			(b'TURB ENG NUM TANKS USED:index', b'Number'),
			_dec='Number of tanks currently being used'
		)
		self.Engine.add(
			'TURB_ENG_FUEL_FLOW_PPH:index',
			(b'TURB ENG FUEL FLOW PPH:index', b'Pounds per hour'),
			_dec='Engine fuel flow'
		)
		self.Engine.add(
			'TURB_ENG_FUEL_AVAILABLE:index',
			(b'TURB ENG FUEL AVAILABLE:index', b'Bool'),
			_dec='True if fuel is available'
		)
		self.Engine.add(
			'TURB_ENG_REVERSE_NOZZLE_PERCENT:index',
			(b'TURB ENG REVERSE NOZZLE PERCENT:index', b'Percent'),
			_dec='Percent thrust reverser nozzles deployed'
		)
		self.Engine.add(
			'TURB_ENG_VIBRATION:index',
			(b'TURB ENG VIBRATION:index', b'Number'),
			_dec='Engine vibration value'
		)
		self.Engine.add(
			'ENG_FAILED:index',
			(b'ENG FAILED:index', b'Number'),
			_dec='Failure flag'
		)
		self.Engine.add(
			'ENG_RPM_ANIMATION_PERCENT:index',
			(b'ENG RPM ANIMATION PERCENT:index', b'Percent'),
			_dec='Percent max rated rpm used for visual animation'
		)
		self.Engine.add(
			'ENG_ON_FIRE:index',
			(b'ENG ON FIRE:index', b'Bool'),
			_dec='On fire state'
		)
		self.Engine.add(
			'ENG_FUEL_FLOW_BUG_POSITION:index',
			(b'ENG FUEL FLOW BUG POSITION:index', b'Pounds per hour'),
			_dec='Fuel flow reference'
		)
		self.Engine.add(
			'PROP_RPM:index',
			(b'PROP RPM:index', b'Rpm'),
			_dec='Propeller rpm'
		)
		self.Engine.add(
			'PROP_MAX_RPM_PERCENT:index',
			(b'PROP MAX RPM PERCENT:index', b'Percent'),
			_dec='Percent of max rated rpm'
		)
		self.Engine.add(
			'PROP_THRUST:index',
			(b'PROP THRUST:index', b'Pounds'),
			_dec='Propeller thrust'
		)
		self.Engine.add(
			'PROP_BETA:index',
			(b'PROP BETA:index', b'Radians'),
			_dec='Prop blade pitch angle'
		)
		self.Engine.add(
			'PROP_FEATHERING_INHIBIT:index',
			(b'PROP FEATHERING INHIBIT:index', b'Bool'),
			_dec='Feathering inhibit flag'
		)
		self.Engine.add(
			'PROP_FEATHERED:index',
			(b'PROP FEATHERED:index', b'Bool'),
			_dec='Feathered state'
		)
		self.Engine.add(
			'PROP_SYNC_DELTA_LEVER:index',
			(b'PROP SYNC DELTA LEVER:index', b'Position'),
			_dec='Corrected prop correction input on slaved engine'
		)
		self.Engine.add(
			'PROP_AUTO_FEATHER_ARMED:index',
			(b'PROP AUTO FEATHER ARMED:index', b'Bool'),
			_dec='Auto-feather armed state'
		)
		self.Engine.add(
			'PROP_FEATHER_SWITCH:index',
			(b'PROP FEATHER SWITCH:index', b'Bool'),
			_dec='Prop feather switch'
		)
		self.Engine.add(
			'PANEL_AUTO_FEATHER_SWITCH:index',
			(b'PANEL AUTO FEATHER SWITCH:index', b'Bool'),
			_dec='Auto-feather arming switch'
		)
		self.Engine.add(
			'PROP_SYNC_ACTIVE:index',
			(b'PROP SYNC ACTIVE:index', b'Bool'),
			_dec='True if prop sync is active'
		)
		self.Engine.add(
			'PROP_DEICE_SWITCH:index',
			(b'PROP DEICE SWITCH:index', b'Bool'),
			_dec='True if prop deice switch on'
		)
		self.Engine.add(
			'ENG_COMBUSTION',
			(b'ENG COMBUSTION', b'Bool'),
			_dec='True if the engine is running'
		)
		self.Engine.add(
			'ENG_N1_RPM:index',
			(b'ENG N1 RPM:index', b'Rpm (0 to 16384 = 0 to 100%)'),
			_dec='Engine N1 rpm'
		)
		self.Engine.add(
			'ENG_N2_RPM:index',
			(b'ENG N2 RPM:index', b'Rpm(0 to 16384 = 0 to 100%)'),
			_dec='Engine N2 rpm'
		)
		self.Engine.add(
			'ENG_FUEL_FLOW_GPH:index',
			(b'ENG FUEL FLOW GPH:index', b'Gallons per hour'),
			_dec='Engine fuel flow'
		)
		self.Engine.add(
			'ENG_FUEL_FLOW_PPH:index',
			(b'ENG FUEL FLOW PPH:index', b'Pounds per hour'),
			_dec='Engine fuel flow'
		)
		self.Engine.add(
			'ENG_TORQUE:index',
			(b'ENG TORQUE:index', b'Foot pounds'),
			_dec='Torque'
		)
		self.Engine.add(
			'ENG_ANTI_ICE:index',
			(b'ENG ANTI ICE:index', b'Bool'),
			_dec='Anti-ice switch'
		)
		self.Engine.add(
			'ENG_PRESSURE_RATIO:index',
			(b'ENG PRESSURE RATIO:index', b'Ratio (0-16384)'),
			_dec='Engine pressure ratio'
		)
		self.Engine.add(
			'ENG_EXHAUST_GAS_TEMPERATURE:index',
			(b'ENG EXHAUST GAS TEMPERATURE:index', b'Rankine'),
			_dec='Exhaust gas temperature'
		)
		self.Engine.add(
			'ENG_EXHAUST_GAS_TEMPERATURE_GES:index',
			(b'ENG EXHAUST GAS TEMPERATURE GES:index', b'Percent over 100'),
			_dec='Governed engine setting'
		)
		self.Engine.add(
			'ENG_CYLINDER_HEAD_TEMPERATURE:index',
			(b'ENG CYLINDER HEAD TEMPERATURE:index', b'Rankine'),
			_dec='Engine cylinder head temperature'
		)
		self.Engine.add(
			'ENG_OIL_TEMPERATURE:index',
			(b'ENG OIL TEMPERATURE:index', b'Rankine'),
			_dec='Engine oil temperature'
		)
		self.Engine.add(
			'ENG_OIL_PRESSURE:index',
			(b'ENG OIL PRESSURE:index', b'Pounds per square foot'),
			_dec='Engine oil pressure'
		)
		self.Engine.add(
			'ENG_OIL_QUANTITY:index',
			(b'ENG OIL QUANTITY:index', b'Percent over 100'),
			_dec='Engine oil quantitiy as a percentage of full capacity'
		)
		self.Engine.add(
			'ENG_HYDRAULIC_PRESSURE:index',
			(b'ENG HYDRAULIC PRESSURE:index', b'Pounds per square foot'),
			_dec='Engine hydraulic pressure'
		)
		self.Engine.add(
			'ENG_HYDRAULIC_QUANTITY:index',
			(b'ENG HYDRAULIC QUANTITY:index', b'Percent over 100'),
			_dec='Engine hydraulic fluid quantity, as a percentage of total capacity'
		)
		self.Engine.add(
			'ENG_MANIFOLD_PRESSURE:index',
			(b'ENG MANIFOLD PRESSURE:index', b'inHG.'),
			_dec='Engine manifold pressure.'
		)
		self.Engine.add(
			'ENG_VIBRATION:index',
			(b'ENG VIBRATION:index', b'Number'),
			_dec='Engine vibration'
		)
		self.Engine.add(
			'ENG_RPM_SCALER:index',
			(b'ENG RPM SCALER:index', b'Scalar'),
			_dec='Obsolete'
		)
		self.Engine.add(
			'ENG_MAX_RPM',
			(b'ENG MAX RPM', b'Rpm'),
			_dec='Maximum rpm'
		)
		self.Engine.add(
			'GENERAL_ENG_STARTER_ACTIVE',
			(b'GENERAL ENG STARTER ACTIVE', b'Bool'),
			_dec='True if engine starter is active'
		)
		self.Engine.add(
			'GENERAL_ENG_FUEL_USED_SINCE_START',
			(b'GENERAL ENG FUEL USED SINCE START', b'Pounds'),
			_dec='Fuel used since the engines were last started'
		)
		self.Engine.add(
			'TURB_ENG_PRIMARY_NOZZLE_PERCENT:index',
			(b'TURB ENG PRIMARY NOZZLE PERCENT:index', b'Percent over 100'),
			_dec='Percent thrust of primary nozzle'
		)
		self.Engine.add(
			'TURB_ENG_IGNITION_SWITCH',
			(b'TURB ENG IGNITION SWITCH', b'Bool'),
			_dec='True if the turbine engine ignition switch is on'
		)
		self.Engine.add(
			'TURB_ENG_MASTER_STARTER_SWITCH',
			(b'TURB ENG MASTER STARTER SWITCH', b'Bool'),
			_dec='True if the turbine engine master starter switch is on'
		)
		self.Engine.add(
			'TURB_ENG_AFTERBURNER_STAGE_ACTIVE',
			(b'TURB ENG AFTERBURNER STAGE ACTIVE', b'Number'),
			_dec='The stage of the afterburner, or 0 if the afterburner is not active.'
		)
		self.Engine.add(
			'TURB_ENG_AFTERBURNER_PCT_ACTIVE',
			(b'TURB ENG AFTERBURNER PCT ACTIVE', b'Percent_over_100'),
			_dec='The percentage that the afterburner is running at.'
		)

		self.Fuel = sm.new_request_holder()
		self.Fuel.add(
			'FUEL_TANK_CENTER_LEVEL',
			(b'FUEL TANK CENTER LEVEL', b'Percent Over 100'),
			_dec='Percent of maximum capacity'
		)
		self.Fuel.add(
			'FUEL_TANK_CENTER2_LEVEL',
			(b'FUEL TANK CENTER2 LEVEL', b'Percent Over 100'),
			_dec='Percent of maximum capacity'
		)
		self.Fuel.add(
			'FUEL_TANK_CENTER3_LEVEL',
			(b'FUEL TANK CENTER3 LEVEL', b'Percent Over 100'),
			_dec='Percent of maximum capacity'
		)
		self.Fuel.add(
			'FUEL_TANK_LEFT_MAIN_LEVEL',
			(b'FUEL TANK LEFT MAIN LEVEL', b'Percent Over 100'),
			_dec='Percent of maximum capacity'
		)
		self.Fuel.add(
			'FUEL_TANK_LEFT_AUX_LEVEL',
			(b'FUEL TANK LEFT AUX LEVEL', b'Percent Over 100'),
			_dec='Percent of maximum capacity'
		)
		self.Fuel.add(
			'FUEL_TANK_LEFT_TIP_LEVEL',
			(b'FUEL TANK LEFT TIP LEVEL', b'Percent Over 100'),
			_dec='Percent of maximum capacity'
		)
		self.Fuel.add(
			'FUEL_TANK_RIGHT_MAIN_LEVEL',
			(b'FUEL TANK RIGHT MAIN LEVEL', b'Percent Over 100'),
			_dec='Percent of maximum capacity'
		)
		self.Fuel.add(
			'FUEL_TANK_RIGHT_AUX_LEVEL',
			(b'FUEL TANK RIGHT AUX LEVEL', b'Percent Over 100'),
			_dec='Percent of maximum capacity'
		)
		self.Fuel.add(
			'FUEL_TANK_RIGHT_TIP_LEVEL',
			(b'FUEL TANK RIGHT TIP LEVEL', b'Percent Over 100'),
			_dec='Percent of maximum capacity'
		)
		self.Fuel.add(
			'FUEL_TANK_EXTERNAL1_LEVEL',
			(b'FUEL TANK EXTERNAL1 LEVEL', b'Percent Over 100'),
			_dec='Percent of maximum capacity'
		)
		self.Fuel.add(
			'FUEL_TANK_EXTERNAL2_LEVEL',
			(b'FUEL TANK EXTERNAL2 LEVEL', b'Percent Over 100'),
			_dec='Percent of maximum capacity'
		)
		self.Fuel.add(
			'FUEL_TANK_CENTER_CAPACITY',
			(b'FUEL TANK CENTER CAPACITY', b'Gallons'),
			_dec='Maximum capacity in volume'
		)
		self.Fuel.add(
			'FUEL_TANK_CENTER2_CAPACITY',
			(b'FUEL TANK CENTER2 CAPACITY', b'Gallons'),
			_dec='Maximum capacity in volume'
		)
		self.Fuel.add(
			'FUEL_TANK_CENTER3_CAPACITY',
			(b'FUEL TANK CENTER3 CAPACITY', b'Gallons'),
			_dec='Maximum capacity in volume'
		)
		self.Fuel.add(
			'FUEL_TANK_LEFT_MAIN_CAPACITY',
			(b'FUEL TANK LEFT MAIN CAPACITY', b'Gallons'),
			_dec='Maximum capacity in volume'
		)
		self.Fuel.add(
			'FUEL_TANK_LEFT_AUX_CAPACITY',
			(b'FUEL TANK LEFT AUX CAPACITY', b'Gallons'),
			_dec='Maximum capacity in volume'
		)
		self.Fuel.add(
			'FUEL_TANK_LEFT_TIP_CAPACITY',
			(b'FUEL TANK LEFT TIP CAPACITY', b'Gallons'),
			_dec='Maximum capacity in volume'
		)
		self.Fuel.add(
			'FUEL_TANK_RIGHT_MAIN_CAPACITY',
			(b'FUEL TANK RIGHT MAIN CAPACITY', b'Gallons'),
			_dec='Maximum capacity in volume'
		)
		self.Fuel.add(
			'FUEL_TANK_RIGHT_AUX_CAPACITY',
			(b'FUEL TANK RIGHT AUX CAPACITY', b'Gallons'),
			_dec='Maximum capacity in volume'
		)
		self.Fuel.add(
			'FUEL_TANK_RIGHT_TIP_CAPACITY',
			(b'FUEL TANK RIGHT TIP CAPACITY', b'Gallons'),
			_dec='Maximum capacity in volume'
		)
		self.Fuel.add(
			'FUEL_TANK_EXTERNAL1_CAPACITY',
			(b'FUEL TANK EXTERNAL1 CAPACITY', b'Gallons'),
			_dec='Maximum capacity in volume'
		)
		self.Fuel.add(
			'FUEL_TANK_EXTERNAL2_CAPACITY',
			(b'FUEL TANK EXTERNAL2 CAPACITY', b'Gallons'),
			_dec='Maximum capacity in volume'
		)
		self.Fuel.add(
			'FUEL_LEFT_CAPACITY',
			(b'FUEL LEFT CAPACITY', b'Gallons'),
			_dec='Maximum capacity in volume'
		)
		self.Fuel.add(
			'FUEL_RIGHT_CAPACITY',
			(b'FUEL RIGHT CAPACITY', b'Gallons'),
			_dec='Maximum capacity in volume'
		)
		self.Fuel.add(
			'FUEL_TANK_CENTER_QUANTITY',
			(b'FUEL TANK CENTER QUANTITY', b'Gallons'),
			_dec='Current quantity in volume'
		)
		self.Fuel.add(
			'FUEL_TANK_CENTER2_QUANTITY',
			(b'FUEL TANK CENTER2 QUANTITY', b'Gallons'),
			_dec='Current quantity in volume'
		)
		self.Fuel.add(
			'FUEL_TANK_CENTER3_QUANTITY',
			(b'FUEL TANK CENTER3 QUANTITY', b'Gallons'),
			_dec='Current quantity in volume'
		)
		self.Fuel.add(
			'FUEL_TANK_LEFT_MAIN_QUANTITY',
			(b'FUEL TANK LEFT MAIN QUANTITY', b'Gallons'),
			_dec='Current quantity in volume'
		)
		self.Fuel.add(
			'FUEL_TANK_LEFT_AUX_QUANTITY',
			(b'FUEL TANK LEFT AUX QUANTITY', b'Gallons'),
			_dec='Current quantity in volume'
		)
		self.Fuel.add(
			'FUEL_TANK_LEFT_TIP_QUANTITY',
			(b'FUEL TANK LEFT TIP QUANTITY', b'Gallons'),
			_dec='Current quantity in volume'
		)
		self.Fuel.add(
			'FUEL_TANK_RIGHT_MAIN_QUANTITY',
			(b'FUEL TANK RIGHT MAIN QUANTITY', b'Gallons'),
			_dec='Current quantity in volume'
		)
		self.Fuel.add(
			'FUEL_TANK_RIGHT_AUX_QUANTITY',
			(b'FUEL TANK RIGHT AUX QUANTITY', b'Gallons'),
			_dec='Current quantity in volume'
		)
		self.Fuel.add(
			'FUEL_TANK_RIGHT_TIP_QUANTITY',
			(b'FUEL TANK RIGHT TIP QUANTITY', b'Gallons'),
			_dec='Current quantity in volume'
		)
		self.Fuel.add(
			'FUEL_TANK_EXTERNAL1_QUANTITY',
			(b'FUEL TANK EXTERNAL1 QUANTITY', b'Gallons'),
			_dec='Current quantity in volume'
		)
		self.Fuel.add(
			'FUEL_TANK_EXTERNAL2_QUANTITY',
			(b'FUEL TANK EXTERNAL2 QUANTITY', b'Gallons'),
			_dec='Current quantity in volume'
		)
		self.Fuel.add(
			'FUEL_LEFT_QUANTITY',
			(b'FUEL LEFT QUANTITY', b'Gallons'),
			_dec='Current quantity in volume'
		)
		self.Fuel.add(
			'FUEL_RIGHT_QUANTITY',
			(b'FUEL RIGHT QUANTITY', b'Gallons'),
			_dec='Current quantity in volume'
		)
		self.Fuel.add(
			'FUEL_TOTAL_QUANTITY',
			(b'FUEL TOTAL QUANTITY', b'Gallons'),
			_dec='Current quantity in volume'
		)
		self.Fuel.add(
			'FUEL_WEIGHT_PER_GALLON',
			(b'FUEL WEIGHT PER GALLON', b'Pounds'),
			_dec='Fuel weight per gallon'
		)
		self.Fuel.add(
			'FUEL_TANK_SELECTOR:index',
			(b'FUEL TANK SELECTOR:index', b'Enum'),
			_dec='Which tank is selected. See fuel tank list.'
		)
		self.Fuel.add(
			'FUEL_TOTAL_CAPACITY',
			(b'FUEL TOTAL CAPACITY', b'Gallons'),
			_dec='Total capacity of the aircraft'
		)
		self.Fuel.add(
			'FUEL_SELECTED_QUANTITY_PERCENT',
			(b'FUEL SELECTED QUANTITY PERCENT', b'Percent Over 100'),
			_dec='Percent or capacity for selected tank'
		)
		self.Fuel.add(
			'FUEL_SELECTED_QUANTITY',
			(b'FUEL SELECTED QUANTITY', b'Gallons'),
			_dec='Quantity of selected tank'
		)
		self.Fuel.add(
			'FUEL_TOTAL_QUANTITY_WEIGHT',
			(b'FUEL TOTAL QUANTITY WEIGHT', b'Pounds'),
			_dec='Current total fuel weight of the aircraft'
		)
		self.Fuel.add(
			'NUM_FUEL_SELECTORS',
			(b'NUM FUEL SELECTORS', b'Number'),
			_dec='Number of selectors on the aircraft'
		)
		self.Fuel.add(
			'UNLIMITED_FUEL',
			(b'UNLIMITED FUEL', b'Bool'),
			_dec='Unlimited fuel flag'
		)
		self.Fuel.add(
			'ESTIMATED_FUEL_FLOW',
			(b'ESTIMATED FUEL FLOW', b'Pounds per hour'),
			_dec='Estimated fuel flow at cruise'
		)

		self.Lights = sm.new_request_holder()
		self.Lights.add(
			'LIGHT_STROBE',
			(b'LIGHT STROBE', b'Bool'),
			_dec='Light switch state'
		)
		self.Lights.add(
			'LIGHT_PANEL',
			(b'LIGHT PANEL', b'Bool'),
			_dec='Light switch state'
		)
		self.Lights.add(
			'LIGHT_LANDING',
			(b'LIGHT LANDING', b'Bool'),
			_dec='Light switch state'
		)
		self.Lights.add(
			'LIGHT_TAXI',
			(b'LIGHT TAXI', b'Bool'),
			_dec='Light switch state'
		)
		self.Lights.add(
			'LIGHT_BEACON',
			(b'LIGHT BEACON', b'Bool'),
			_dec='Light switch state'
		)
		self.Lights.add(
			'LIGHT_NAV',
			(b'LIGHT NAV', b'Bool'),
			_dec='Light switch state'
		)
		self.Lights.add(
			'LIGHT_LOGO',
			(b'LIGHT LOGO', b'Bool'),
			_dec='Light switch state'
		)
		self.Lights.add(
			'LIGHT_WING',
			(b'LIGHT WING', b'Bool'),
			_dec='Light switch state'
		)
		self.Lights.add(
			'LIGHT_RECOGNITION',
			(b'LIGHT RECOGNITION', b'Bool'),
			_dec='Light switch state'
		)
		self.Lights.add(
			'LIGHT_CABIN',
			(b'LIGHT CABIN', b'Bool'),
			_dec='Light switch state'
		)
		self.Lights.add(
			'LIGHT_STATES',
			(b'LIGHT STATES', b'Mask'),
			_dec='Same as LIGHT ON STATES'
		)
		self.Lights.add(
			'LANDING_LIGHT_PBH',
			(b'LANDING LIGHT PBH', b'SIMCONNECT_DATA_XYZ structure'),
			_dec='Landing light pitch bank and heading'
		)
		self.Lights.add(
			'LIGHT_TAXI_ON',
			(b'LIGHT TAXI ON', b'Bool'),
			_dec='Return true if the light is on.'
		)
		self.Lights.add(
			'LIGHT_STROBE_ON',
			(b'LIGHT STROBE ON', b'Bool'),
			_dec='Return true if the light is on.'
		)
		self.Lights.add(
			'LIGHT_PANEL_ON',
			(b'LIGHT PANEL ON', b'Bool'),
			_dec='Return true if the light is on.'
		)
		self.Lights.add(
			'LIGHT_RECOGNITION_ON',
			(b'LIGHT RECOGNITION ON', b'Bool'),
			_dec='Return true if the light is on.'
		)
		self.Lights.add(
			'LIGHT_WING_ON',
			(b'LIGHT WING ON', b'Bool'),
			_dec='Return true if the light is on.'
		)
		self.Lights.add(
			'LIGHT_LOGO_ON',
			(b'LIGHT LOGO ON', b'Bool'),
			_dec='Return true if the light is on.'
		)
		self.Lights.add(
			'LIGHT_CABIN_ON',
			(b'LIGHT CABIN ON', b'Bool'),
			_dec='Return true if the light is on.'
		)
		self.Lights.add(
			'LIGHT_HEAD_ON',
			(b'LIGHT HEAD ON', b'Bool'),
			_dec='Return true if the light is on.'
		)
		self.Lights.add(
			'LIGHT_BRAKE_ON',
			(b'LIGHT BRAKE ON', b'Bool'),
			_dec='Return true if the light is on.'
		)
		self.Lights.add(
			'LIGHT_NAV_ON',
			(b'LIGHT NAV ON', b'Bool'),
			_dec='Return true if the light is on.'
		)
		self.Lights.add(
			'LIGHT_BEACON_ON',
			(b'LIGHT BEACON ON', b'Bool'),
			_dec='Return true if the light is on.'
		)
		self.Lights.add(
			'LIGHT_LANDING_ON',
			(b'LIGHT LANDING ON', b'Bool'),
			_dec='Return true if the light is on.'
		)

		self.Position_and_Speed = sm.new_request_holder()
		self.Position_and_Speed.add(
			'GROUND_VELOCITY',
			(b'GROUND VELOCITY', b'Knots'),
			_dec='Speed relative to the earths surface'
		)
		self.Position_and_Speed.add(
			'TOTAL_WORLD_VELOCITY',
			(b'TOTAL WORLD VELOCITY', b'Feet per second'),
			_dec='Speed relative to the earths center'
		)
		self.Position_and_Speed.add(
			'VELOCITY_BODY_Z',
			(b'VELOCITY BODY Z', b'Feet per second'),
			_dec='True longitudinal speed, relative to aircraft axis'
		)
		self.Position_and_Speed.add(
			'VELOCITY_BODY_X',
			(b'VELOCITY BODY X', b'Feet per second'),
			_dec='True lateral speed, relative to aircraft axis'
		)
		self.Position_and_Speed.add(
			'VELOCITY_BODY_Y',
			(b'VELOCITY BODY Y', b'Feet per second'),
			_dec='True vertical speed, relative to aircraft axis'
		)
		self.Position_and_Speed.add(
			'VELOCITY_WORLD_Z',
			(b'VELOCITY WORLD Z', b'Feet per second'),
			_dec='Speed relative to earth, in North/South direction'
		)
		self.Position_and_Speed.add(
			'VELOCITY_WORLD_X',
			(b'VELOCITY WORLD X', b'Feet per second'),
			_dec='Speed relative to earth, in East/West direction'
		)
		self.Position_and_Speed.add(
			'VELOCITY_WORLD_Y',
			(b'VELOCITY WORLD Y', b'Feet per second'),
			_dec='Speed relative to earth, in vertical direction'
		)
		self.Position_and_Speed.add(
			'ACCELERATION_WORLD_X',
			(b'ACCELERATION WORLD X', b'Feet per second squared'),
			_dec='Acceleration relative to earth, in east/west direction'
		)
		self.Position_and_Speed.add(
			'ACCELERATION_WORLD_Y',
			(b'ACCELERATION WORLD Y', b'Feet per second squared'),
			_dec='Acceleration relative to earch, in vertical direction'
		)
		self.Position_and_Speed.add(
			'ACCELERATION_WORLD_Z',
			(b'ACCELERATION WORLD Z', b'Feet per second squared'),
			_dec='Acceleration relative to earth, in north/south direction'
		)
		self.Position_and_Speed.add(
			'ACCELERATION_BODY_X',
			(b'ACCELERATION BODY X', b'Feet per second squared'),
			_dec='Acceleration relative to aircraft axix, in east/west direction'
		)
		self.Position_and_Speed.add(
			'ACCELERATION_BODY_Y',
			(b'ACCELERATION BODY Y', b'Feet per second squared'),
			_dec='Acceleration relative to aircraft axis, in vertical direction'
		)
		self.Position_and_Speed.add(
			'ACCELERATION_BODY_Z',
			(b'ACCELERATION BODY Z', b'Feet per second squared'),
			_dec='Acceleration relative to aircraft axis, in north/south direction'
		)
		self.Position_and_Speed.add(
			'ROTATION_VELOCITY_BODY_X',
			(b'ROTATION VELOCITY BODY X', b'Feet per second'),
			_dec='Rotation relative to aircraft axis'
		)
		self.Position_and_Speed.add(
			'ROTATION_VELOCITY_BODY_Y',
			(b'ROTATION VELOCITY BODY Y', b'Feet per second'),
			_dec='Rotation relative to aircraft axis'
		)
		self.Position_and_Speed.add(
			'ROTATION_VELOCITY_BODY_Z',
			(b'ROTATION VELOCITY BODY Z', b'Feet per second'),
			_dec='Rotation relative to aircraft axis'
		)
		self.Position_and_Speed.add(
			'RELATIVE_WIND_VELOCITY_BODY_X',
			(b'RELATIVE WIND VELOCITY BODY X', b'Feet per second'),
			_dec='Lateral speed relative to wind'
		)
		self.Position_and_Speed.add(
			'RELATIVE_WIND_VELOCITY_BODY_Y',
			(b'RELATIVE WIND VELOCITY BODY Y', b'Feet per second'),
			_dec='Vertical speed relative to wind'
		)
		self.Position_and_Speed.add(
			'RELATIVE_WIND_VELOCITY_BODY_Z',
			(b'RELATIVE WIND VELOCITY BODY Z', b'Feet per second'),
			_dec='Longitudinal speed relative to wind'
		)
		self.Position_and_Speed.add(
			'PLANE_ALT_ABOVE_GROUND',
			(b'PLANE ALT ABOVE GROUND', b'Feet'),
			_dec='Altitude above the surface'
		)
		self.Position_and_Speed.add(
			'PLANE_LATITUDE',
			(b'PLANE LATITUDE', b'Degrees'),
			_dec='Latitude of aircraft, North is positive, South negative'
		)
		self.Position_and_Speed.add(
			'PLANE_LONGITUDE',
			(b'PLANE LONGITUDE', b'Degrees'),
			_dec='Longitude of aircraft, East is positive, West negative'
		)
		self.Position_and_Speed.add(
			'PLANE_ALTITUDE',
			(b'PLANE ALTITUDE', b'Feet'),
			_dec='Altitude of aircraft'
		)
		self.Position_and_Speed.add(
			'PLANE_PITCH_DEGREES',
			(b'PLANE PITCH DEGREES', b'Radians'),
			_dec='Pitch angle, although the name mentions degrees the units used are radians'
		)
		self.Position_and_Speed.add(
			'PLANE_BANK_DEGREES',
			(b'PLANE BANK DEGREES', b'Radians'),
			_dec='Bank angle, although the name mentions degrees the units used are radians'
		)
		self.Position_and_Speed.add(
			'PLANE_HEADING_DEGREES_TRUE',
			(b'PLANE HEADING DEGREES TRUE', b'Radians'),
			_dec='Heading relative to true north, although the name mentions degrees the units used are radians'
		)
		self.Position_and_Speed.add(
			'PLANE_HEADING_DEGREES_MAGNETIC',
			(b'PLANE HEADING DEGREES MAGNETIC', b'Radians'),
			_dec='Heading relative to magnetic north, although the name mentions degrees the units used are radians'
		)
		self.Position_and_Speed.add(
			'MAGVAR',
			(b'MAGVAR', b'Degrees'),
			_dec='Magnetic variation'
		)
		self.Position_and_Speed.add(
			'GROUND_ALTITUDE',
			(b'GROUND ALTITUDE', b'Meters'),
			_dec='Altitude of surface'
		)
		self.Position_and_Speed.add(
			'SIM_ON_GROUND',
			(b'SIM ON GROUND', b'Bool'),
			_dec='On ground flag'
		)
		self.Position_and_Speed.add(
			'INCIDENCE_ALPHA',
			(b'INCIDENCE ALPHA', b'Radians'),
			_dec='Angle of attack'
		)
		self.Position_and_Speed.add(
			'INCIDENCE_BETA',
			(b'INCIDENCE BETA', b'Radians'),
			_dec='Sideslip angle'
		)
		self.Position_and_Speed.add(
			'WING_FLEX_PCT:index',
			(b'WING FLEX PCT:index', b'Percent over 100'),
			_dec='''
				The current wing flex.
				Different values can be set for each wing
				(for example, during banking).
				Set an index of 1 for the left wing,
				and 2 for the right wing.'''
		)
		self.Position_and_Speed.add(
			'STRUCT_LATLONALT',
			(b'STRUCT LATLONALT', b'SIMCONNECT_DATA_LATLONALTstructure'),
			_dec='Returns the latitude, longitude and altitude of the user aircraft.'
		)
		self.Position_and_Speed.add(
			'STRUCT_LATLONALTPBH',
			(b'STRUCT LATLONALTPBH', b'SIMCONNECT_DATA_LATLONALTstructure'),
			_dec='Returns the pitch, bank and heading of the user aircraft.'
		)
		self.Position_and_Speed.add(
			'STRUCT_SURFACE_RELATIVE_VELOCITY',
			(b'STRUCT SURFACE RELATIVE VELOCITY', b'SIMCONNECT_DATA_XYZ structure, feet per second'),
			_dec='The relative surface velocity.'
		)
		self.Position_and_Speed.add(
			'STRUCT_WORLDVELOCITY',
			(b'STRUCT WORLDVELOCITY', b'SIMCONNECT_DATA_XYZ structure, feet per second'),
			_dec='The world velocity.'
		)
		self.Position_and_Speed.add(
			'STRUCT_WORLD_ROTATION_VELOCITY',
			(b'STRUCT WORLD ROTATION VELOCITY', b'SIMCONNECT_DATA_XYZ structure, radians per second'),
			_dec='The world rotation velocity.'
		)
		self.Position_and_Speed.add(
			'STRUCT_BODY_VELOCITY',
			(b'STRUCT BODY VELOCITY', b'SIMCONNECT_DATA_XYZ structure, feet per second'),
			_dec='The object body velocity.'
		)
		self.Position_and_Speed.add(
			'STRUCT_BODY_ROTATION_VELOCITY',
			(b'STRUCT BODY ROTATION VELOCITY', b'SIMCONNECT_DATA_XYZ structure, radians per second'),
			_dec='The body rotation velocity. Individual body rotation values are in the Aircraft Position and Speed section.'
		)
		self.Position_and_Speed.add(
			'STRUCT_WORLD_ACCELERATION',
			(b'STRUCT WORLD ACCELERATION', b'SIMCONNECT_DATA_XYZ structure, feet per second squared'),
			_dec='The world acceleration for each axis. Individual world acceleration values are in the Aircraft Position and Speed section.'
		)
		self.Position_and_Speed.add(
			'STRUCT_ENGINE_POSITION:index',
			(b'STRUCT ENGINE POSITION:index', b'SIMCONNECT_DATA_XYZ structure, feet.'),
			_dec='The engine position relative to the reference datum position for the aircraft.'
		)
		self.Position_and_Speed.add(
			'STRUCT_EYEPOINT_DYNAMIC_ANGLE',
			(b'STRUCT EYEPOINT DYNAMIC ANGLE', b'SIMCONNECT_DATA_XYZ structure, radians'),
			_dec='The angle of the eyepoint view. Zero, zero, zero is straight ahead.'
		)
		self.Position_and_Speed.add(
			'STRUCT_EYEPOINT_DYNAMIC_OFFSET',
			(b'STRUCT EYEPOINT DYNAMIC OFFSET', b'SIMCONNECT_DATA_XYZ structure, feet'),
			_dec='A variable offset away from the EYEPOINT POSITION'
		)
		self.Position_and_Speed.add(
			'EYEPOINT_POSITION',
			(b'EYEPOINT POSITION', b'SIMCONNECT_DATA_XYZ structure, feet'),
			_dec='The eyepoint position relative to the reference datum position for the aircraft.'
		)

		self.Flight_Instrumentation = sm.new_request_holder()
		self.Flight_Instrumentation.add(
			'AIRSPEED_TRUE',
			(b'AIRSPEED TRUE', b'Knots'),
			_dec='True airspeed'
		)
		self.Flight_Instrumentation.add(
			'AIRSPEED_INDICATED',
			(b'AIRSPEED INDICATED', b'Knots'),
			_dec='Indicated airspeed'
		)
		self.Flight_Instrumentation.add(
			'AIRSPEED_TRUE_CALIBRATE',
			(b'AIRSPEED TRUE CALIBRATE', b'Degrees'),
			_dec='Angle of True calibration scale on airspeed indicator'
		)
		self.Flight_Instrumentation.add(
			'AIRSPEED_BARBER_POLE',
			(b'AIRSPEED BARBER POLE', b'Knots'),
			_dec='Redline airspeed (dynamic on some aircraft)'
		)
		self.Flight_Instrumentation.add(
			'AIRSPEED_MACH',
			(b'AIRSPEED MACH', b'Mach'),
			_dec='Current mach'
		)
		self.Flight_Instrumentation.add(
			'VERTICAL_SPEED',
			(b'VERTICAL SPEED', b'feet/minute'),
			_dec='Vertical speed indication'
		)
		self.Flight_Instrumentation.add(
			'MACH_MAX_OPERATE',
			(b'MACH MAX OPERATE', b'Mach'),
			_dec='Maximum design mach'
		)
		self.Flight_Instrumentation.add(
			'STALL_WARNING',
			(b'STALL WARNING', b'Bool'),
			_dec='Stall warning state'
		)
		self.Flight_Instrumentation.add(
			'OVERSPEED_WARNING',
			(b'OVERSPEED WARNING', b'Bool'),
			_dec='Overspeed warning state'
		)
		self.Flight_Instrumentation.add(
			'BARBER_POLE_MACH',
			(b'BARBER POLE MACH', b'Mach'),
			_dec='Mach associated with maximum airspeed'
		)
		self.Flight_Instrumentation.add(
			'INDICATED_ALTITUDE',
			(b'INDICATED ALTITUDE', b'Feet'),
			_dec='Altimeter indication'
		)
		self.Flight_Instrumentation.add(
			'KOHLSMAN_SETTING_MB',
			(b'KOHLSMAN SETTING MB', b'Millibars'),
			_dec='Altimeter setting'
		)
		self.Flight_Instrumentation.add(
			'KOHLSMAN_SETTING_HG',
			(b'KOHLSMAN SETTING HG', b'inHg'),
			_dec='Altimeter setting'
		)
		self.Flight_Instrumentation.add(
			'ATTITUDE_INDICATOR_PITCH_DEGREES',
			(b'ATTITUDE INDICATOR PITCH DEGREES', b'Radians'),
			_dec='AI pitch indication'
		)
		self.Flight_Instrumentation.add(
			'ATTITUDE_INDICATOR_BANK_DEGREES',
			(b'ATTITUDE INDICATOR BANK DEGREES', b'Radians'),
			_dec='AI bank indication'
		)
		self.Flight_Instrumentation.add(
			'ATTITUDE_BARS_POSITION',
			(b'ATTITUDE BARS POSITION', b'Percent Over 100'),
			_dec='AI reference pitch reference bars'
		)
		self.Flight_Instrumentation.add(
			'ATTITUDE_CAGE',
			(b'ATTITUDE CAGE', b'Bool'),
			_dec='AI caged state'
		)
		self.Flight_Instrumentation.add(
			'WISKEY_COMPASS_INDICATION_DEGREES',
			(b'WISKEY COMPASS INDICATION DEGREES', b'Degrees'),
			_dec='Magnetic compass indication'
		)
		self.Flight_Instrumentation.add(
			'PLANE_HEADING_DEGREES_GYRO',
			(b'PLANE HEADING DEGREES GYRO', b'Radians'),
			_dec='Heading indicator (directional gyro) indication'
		)
		self.Flight_Instrumentation.add(
			'HEADING_INDICATOR',
			(b'HEADING INDICATOR', b'Radians'),
			_dec='Heading indicator (directional gyro) indication'
		)
		self.Flight_Instrumentation.add(
			'GYRO_DRIFT_ERROR',
			(b'GYRO DRIFT ERROR', b'Radians'),
			_dec='Angular error of heading indicator'
		)
		self.Flight_Instrumentation.add(
			'DELTA_HEADING_RATE',
			(b'DELTA HEADING RATE', b'Radians per second'),
			_dec='Rate of turn of heading indicator'
		)
		self.Flight_Instrumentation.add(
			'TURN_COORDINATOR_BALL',
			(b'TURN COORDINATOR BALL', b'Position 128 (-127 to 127)'),
			_dec='Turn coordinator ball position'
		)
		self.Flight_Instrumentation.add(
			'ANGLE_OF_ATTACK_INDICATOR',
			(b'ANGLE OF ATTACK INDICATOR', b'Radians'),
			_dec='AoA indication'
		)
		self.Flight_Instrumentation.add(
			'RADIO_HEIGHT',
			(b'RADIO HEIGHT', b'Feet'),
			_dec='Radar altitude'
		)
		self.Flight_Instrumentation.add(
			'PARTIAL_PANEL_ADF',
			(b'PARTIAL PANEL ADF', b'Enum'),
			_dec='Gauge fail flag (0 = ok, 1 = fail, 2 = blank)'
		)
		self.Flight_Instrumentation.add(
			'PARTIAL_PANEL_AIRSPEED',
			(b'PARTIAL PANEL AIRSPEED', b'Enum'),
			_dec='Gauge fail flag (0 = ok, 1 = fail, 2 = blank)'
		)
		self.Flight_Instrumentation.add(
			'PARTIAL_PANEL_ALTIMETER',
			(b'PARTIAL PANEL ALTIMETER', b'Enum'),
			_dec='Gauge fail flag (0 = ok, 1 = fail, 2 = blank)'
		)
		self.Flight_Instrumentation.add(
			'PARTIAL_PANEL_ATTITUDE',
			(b'PARTIAL PANEL ATTITUDE', b'Enum'),
			_dec='Gauge fail flag (0 = ok, 1 = fail, 2 = blank)'
		)
		self.Flight_Instrumentation.add(
			'PARTIAL_PANEL_COMM',
			(b'PARTIAL PANEL COMM', b'Enum'),
			_dec='Gauge fail flag (0 = ok, 1 = fail, 2 = blank)'
		)
		self.Flight_Instrumentation.add(
			'PARTIAL_PANEL_COMPASS',
			(b'PARTIAL PANEL COMPASS', b'Enum'),
			_dec='Gauge fail flag (0 = ok, 1 = fail, 2 = blank)'
		)
		self.Flight_Instrumentation.add(
			'PARTIAL_PANEL_ELECTRICAL',
			(b'PARTIAL PANEL ELECTRICAL', b'Enum'),
			_dec='Gauge fail flag (0 = ok, 1 = fail, 2 = blank)'
		)
		self.Flight_Instrumentation.add(
			'PARTIAL_PANEL_AVIONICS',
			(b'PARTIAL PANEL AVIONICS', b'Enum'),
			_dec='Gauge fail flag (0 = ok, 1 = fail, 2 = blank)'
		)
		self.Flight_Instrumentation.add(
			'PARTIAL_PANEL_ENGINE',
			(b'PARTIAL PANEL ENGINE', b'Enum'),
			_dec='Gauge fail flag (0 = ok, 1 = fail, 2 = blank)'
		)
		self.Flight_Instrumentation.add(
			'PARTIAL_PANEL_FUEL_INDICATOR',
			(b'PARTIAL PANEL FUEL INDICATOR', b'Enum'),
			_dec='Gauge fail flag (0 = ok, 1 = fail, 2 = blank)'
		)
		self.Flight_Instrumentation.add(
			'PARTIAL_PANEL_HEADING',
			(b'PARTIAL PANEL HEADING', b'Enum'),
			_dec='Gauge fail flag (0 = ok, 1 = fail, 2 = blank)'
		)
		self.Flight_Instrumentation.add(
			'PARTIAL_PANEL_VERTICAL_VELOCITY',
			(b'PARTIAL PANEL VERTICAL VELOCITY', b'Enum'),
			_dec='Gauge fail flag (0 = ok, 1 = fail, 2 = blank)'
		)
		self.Flight_Instrumentation.add(
			'PARTIAL_PANEL_TRANSPONDER',
			(b'PARTIAL PANEL TRANSPONDER', b'Enum'),
			_dec='Gauge fail flag (0 = ok, 1 = fail, 2 = blank)'
		)
		self.Flight_Instrumentation.add(
			'PARTIAL_PANEL_NAV',
			(b'PARTIAL PANEL NAV', b'Enum'),
			_dec='Gauge fail flag (0 = ok, 1 = fail, 2 = blank)'
		)
		self.Flight_Instrumentation.add(
			'PARTIAL_PANEL_PITOT',
			(b'PARTIAL PANEL PITOT', b'Enum'),
			_dec='Gauge fail flag (0 = ok, 1 = fail, 2 = blank)'
		)
		self.Flight_Instrumentation.add(
			'PARTIAL_PANEL_TURN_COORDINATOR',
			(b'PARTIAL PANEL TURN COORDINATOR', b'Enum'),
			_dec='Gauge fail flag (0 = ok, 1 = fail, 2 = blank)'
		)
		self.Flight_Instrumentation.add(
			'PARTIAL_PANEL_VACUUM',
			(b'PARTIAL PANEL VACUUM', b'Enum'),
			_dec='Gauge fail flag (0 = ok, 1 = fail, 2 = blank)'
		)
		self.Flight_Instrumentation.add(
			'MAX_G_FORCE',
			(b'MAX G FORCE', b'Gforce'),
			_dec='Maximum G force attained'
		)
		self.Flight_Instrumentation.add(
			'MIN_G_FORCE',
			(b'MIN G FORCE', b'Gforce'),
			_dec='Minimum G force attained'
		)
		self.Flight_Instrumentation.add(
			'SUCTION_PRESSURE',
			(b'SUCTION PRESSURE', b'Inches of Mercury, inHg'),
			_dec='Vacuum system suction pressure'
		)

		self.Avionics = sm.new_request_holder()
		self.Avionics.add(
			'AVIONICS_MASTER_SWITCH',
			(b'AVIONICS MASTER SWITCH', b'Bool'),
			_dec='Avionics switch state'
		)
		self.Avionics.add(
			'NAV_SOUND:index',
			(b'NAV SOUND:index', b'Bool'),
			_dec='Nav audio flag. Index of 1 or 2.'
		)
		self.Avionics.add(
			'DME_SOUND',
			(b'DME SOUND', b'Bool'),
			_dec='DME audio flag'
		)
		self.Avionics.add(
			'ADF_SOUND:index',
			(b'ADF SOUND:index', b'Bool'),
			_dec='ADF audio flag. Index of 0 or 1.'
		)
		self.Avionics.add(
			'MARKER_SOUND',
			(b'MARKER SOUND', b'Bool'),
			_dec='Marker audio flag'
		)
		self.Avionics.add(
			'COM_TRANSMIT:index',
			(b'COM TRANSMIT:index', b'Bool'),
			_dec='Audio panel com transmit state. Index of 1 or 2.'
		)
		self.Avionics.add(
			'COM_RECIEVE_ALL',
			(b'COM RECIEVE ALL', b'Bool'),
			_dec='Flag if all Coms receiving'
		)
		self.Avionics.add(
			'COM_ACTIVE_FREQUENCY:index',
			(b'COM ACTIVE FREQUENCY:index', b'Frequency BCD16'),
			_dec='Com frequency. Index is 1 or 2.'
		)
		self.Avionics.add(
			'COM_STANDBY_FREQUENCY:index',
			(b'COM STANDBY FREQUENCY:index', b'Frequency BCD16'),
			_dec='Com standby frequency. Index is 1 or 2.'
		)
		self.Avionics.add(
			'NAV_AVAILABLE:index',
			(b'NAV AVAILABLE:index', b'Bool'),
			_dec='Flag if Nav equipped on aircraft'
		)
		self.Avionics.add(
			'NAV_ACTIVE_FREQUENCY:index',
			(b'NAV ACTIVE FREQUENCY:index', b'MHz'),
			_dec='Nav active frequency. Index is 1 or 2.'
		)
		self.Avionics.add(
			'NAV_STANDBY_FREQUENCY:index',
			(b'NAV STANDBY FREQUENCY:index', b'MHz'),
			_dec='Nav standby frequency. Index is 1 or 2.'
		)
		self.Avionics.add(
			'NAV_SIGNAL:index',
			(b'NAV SIGNAL:index', b'Number'),
			_dec='Nav signal strength'
		)
		self.Avionics.add(
			'NAV_HAS_NAV:index',
			(b'NAV HAS NAV:index', b'Bool'),
			_dec='Flag if Nav has signal'
		)
		self.Avionics.add(
			'NAV_HAS_LOCALIZER:index',
			(b'NAV HAS LOCALIZER:index', b'Bool'),
			_dec='Flag if tuned station is a localizer'
		)
		self.Avionics.add(
			'NAV_HAS_DME:index',
			(b'NAV HAS DME:index', b'Bool'),
			_dec='Flag if tuned station has a DME'
		)
		self.Avionics.add(
			'NAV_HAS_GLIDE_SLOPE:index',
			(b'NAV HAS GLIDE SLOPE:index', b'Bool'),
			_dec='Flag if tuned station has a glideslope'
		)
		self.Avionics.add(
			'NAV_MAGVAR:index',
			(b'NAV MAGVAR:index', b'Degrees'),
			_dec='Magnetic variation of tuned nav station'
		)
		self.Avionics.add(
			'NAV_RADIAL:index',
			(b'NAV RADIAL:index', b'Degrees'),
			_dec='Radial that aircraft is on'
		)
		self.Avionics.add(
			'NAV_RADIAL_ERROR:index',
			(b'NAV RADIAL ERROR:index', b'Degrees'),
			_dec='Difference between current radial and OBS tuned radial'
		)
		self.Avionics.add(
			'NAV_LOCALIZER:index',
			(b'NAV LOCALIZER:index', b'Degrees'),
			_dec='Localizer course heading'
		)
		self.Avionics.add(
			'NAV_GLIDE_SLOPE_ERROR:index',
			(b'NAV GLIDE SLOPE ERROR:index', b'Degrees'),
			_dec='''
				Difference between current position and glideslope angle.
				Note that this provides 32 bit floating point precision,
				rather than the 8 bit integer precision of NAV GSI.'''
		)
		self.Avionics.add(
			'NAV_CDI:index',
			(b'NAV CDI:index', b'Number'),
			_dec='CDI needle deflection (+/- 127)'
		)
		self.Avionics.add(
			'NAV_GSI:index',
			(b'NAV GSI:index', b'Number'),
			_dec='''
			Glideslope needle deflection (+/- 119).
			Note that this provides only 8 bit precision,
			whereas NAV GLIDE SLOPE ERROR provides
			32 bit floating point precision.'''
		)
		self.Avionics.add(
			'NAV_GS_FLAG:index',
			(b'NAV GS FLAG:index', b'Bool'),
			_dec='Glideslope flag'
		)
		self.Avionics.add(
			'NAV_OBS:index',
			(b'NAV OBS:index', b'Degrees'),
			_dec='OBS setting. Index of 1 or 2.'
		)
		self.Avionics.add(
			'NAV_DME:index',
			(b'NAV DME:index', b'Nautical miles'),
			_dec='DME distance'
		)
		self.Avionics.add(
			'NAV_DMESPEED:index',
			(b'NAV DMESPEED:index', b'Knots'),
			_dec='DME speed'
		)
		self.Avionics.add(
			'ADF_ACTIVE_FREQUENCY:index',
			(b'ADF ACTIVE FREQUENCY:index', b'Frequency ADF BCD32'),
			_dec='ADF frequency. Index of 1 or 2.'
		)
		self.Avionics.add(
			'ADF_STANDBY_FREQUENCY:index',
			(b'ADF STANDBY FREQUENCY:index', b'Hz'),
			_dec='ADF standby frequency'
		)
		self.Avionics.add(
			'ADF_RADIAL:index',
			(b'ADF RADIAL:index', b'Degrees'),
			_dec='Current direction from NDB station'
		)
		self.Avionics.add(
			'ADF_SIGNAL:index',
			(b'ADF SIGNAL:index', b'Number'),
			_dec='Signal strength'
		)
		self.Avionics.add(
			'TRANSPONDER_CODE:index',
			(b'TRANSPONDER CODE:index', b'BCO16'),
			_dec='4-digit code'
		)
		self.Avionics.add(
			'INNER_MARKER',
			(b'INNER MARKER', b'Bool'),
			_dec='Inner marker state'
		)
		self.Avionics.add(
			'MIDDLE_MARKER',
			(b'MIDDLE MARKER', b'Bool'),
			_dec='Middle marker state'
		)
		self.Avionics.add(
			'OUTER_MARKER',
			(b'OUTER MARKER', b'Bool'),
			_dec='Outer marker state'
		)
		self.Avionics.add(
			'NAV_RAW_GLIDE_SLOPE:index',
			(b'NAV RAW GLIDE SLOPE:index', b'Degrees'),
			_dec='Glide slope angle'
		)
		self.Avionics.add(
			'ADF_CARD',
			(b'ADF CARD', b'Degrees'),
			_dec='ADF compass rose setting'
		)
		self.Avionics.add(
			'HSI_CDI_NEEDLE',
			(b'HSI CDI NEEDLE', b'Number'),
			_dec='Needle deflection (+/- 127)'
		)
		self.Avionics.add(
			'HSI_GSI_NEEDLE',
			(b'HSI GSI NEEDLE', b'Number'),
			_dec='Needle deflection (+/- 119)'
		)
		self.Avionics.add(
			'HSI_CDI_NEEDLE_VALID',
			(b'HSI CDI NEEDLE VALID', b'Bool'),
			_dec='Signal valid'
		)
		self.Avionics.add(
			'HSI_GSI_NEEDLE_VALID',
			(b'HSI GSI NEEDLE VALID', b'Bool'),
			_dec='Signal valid'
		)
		self.Avionics.add(
			'HSI_BEARING_VALID',
			(b'HSI BEARING VALID', b'Bool'),
			_dec='This will return true if the HSI BEARING variable contains valid data.'
		)
		self.Avionics.add(
			'HSI_BEARING',
			(b'HSI BEARING', b'Degrees'),
			_dec='''
				If the GPS DRIVES NAV1 variable is true and
				the HSI BEARING VALID variable is true,
				this variable contains the HSI needle bearing.
				If the GPS DRIVES NAV1 variable is false and
				the HSI BEARING VALID variable is true,
				this variable contains the ADF1 frequency.'''
		)
		self.Avionics.add(
			'HSI_HAS_LOCALIZER',
			(b'HSI HAS LOCALIZER', b'Bool'),
			_dec='Station is a localizer'
		)
		self.Avionics.add(
			'HSI_SPEED',
			(b'HSI SPEED', b'Knots'),
			_dec='DME/GPS speed'
		)
		self.Avionics.add(
			'HSI_DISTANCE',
			(b'HSI DISTANCE', b'Nautical miles'),
			_dec='DME/GPS distance'
		)
		self.Avionics.add(
			'GPS_POSITION_LAT',
			(b'GPS POSITION LAT', b'Degrees'),
			_dec='Current GPS latitude'
		)
		self.Avionics.add(
			'GPS_POSITION_LON',
			(b'GPS POSITION LON', b'Degrees'),
			_dec='Current GPS longitude'
		)
		self.Avionics.add(
			'GPS_POSITION_ALT',
			(b'GPS POSITION ALT', b'Meters'),
			_dec='Current GPS altitude'
		)
		self.Avionics.add(
			'GPS_MAGVAR',
			(b'GPS MAGVAR', b'Radians'),
			_dec='Current GPS magnetic variation'
		)
		self.Avionics.add(
			'GPS_IS_ACTIVE_FLIGHT_PLAN',
			(b'GPS IS ACTIVE FLIGHT PLAN', b'Bool'),
			_dec='Flight plan mode active'
		)
		self.Avionics.add(
			'GPS_IS_ACTIVE_WAY_POINT',
			(b'GPS IS ACTIVE WAY POINT', b'Bool'),
			_dec='Waypoint mode active'
		)
		self.Avionics.add(
			'GPS_IS_ARRIVED',
			(b'GPS IS ARRIVED', b'Bool'),
			_dec='Is flight plan destination reached'
		)
		self.Avionics.add(
			'GPS_IS_DIRECTTO_FLIGHTPLAN',
			(b'GPS IS DIRECTTO FLIGHTPLAN', b'Bool'),
			_dec='Is Direct To Waypoint mode active'
		)
		self.Avionics.add(
			'GPS_GROUND_SPEED',
			(b'GPS GROUND SPEED', b'Meters per second'),
			_dec='Current ground speed'
		)
		self.Avionics.add(
			'GPS_GROUND_TRUE_HEADING',
			(b'GPS GROUND TRUE HEADING', b'Radians'),
			_dec='Current true heading'
		)
		self.Avionics.add(
			'GPS_GROUND_MAGNETIC_TRACK',
			(b'GPS GROUND MAGNETIC TRACK', b'Radians'),
			_dec='Current magnetic ground track'
		)
		self.Avionics.add(
			'GPS_GROUND_TRUE_TRACK',
			(b'GPS GROUND TRUE TRACK', b'Radians'),
			_dec='Current true ground track'
		)
		self.Avionics.add(
			'GPS_WP_DISTANCE',
			(b'GPS WP DISTANCE', b'Meters'),
			_dec='Distance to waypoint'
		)
		self.Avionics.add(
			'GPS_WP_BEARING',
			(b'GPS WP BEARING', b'Radians'),
			_dec='Magnetic bearing to waypoint'
		)
		self.Avionics.add(
			'GPS_WP_TRUE_BEARING',
			(b'GPS WP TRUE BEARING', b'Radians'),
			_dec='True bearing to waypoint'
		)
		self.Avionics.add(
			'GPS_WP_CROSS_TRK',
			(b'GPS WP CROSS TRK', b'Meters'),
			_dec='Cross track distance'
		)
		self.Avionics.add(
			'GPS_WP_DESIRED_TRACK',
			(b'GPS WP DESIRED TRACK', b'Radians'),
			_dec='Desired track to waypoint'
		)
		self.Avionics.add(
			'GPS_WP_TRUE_REQ_HDG',
			(b'GPS WP TRUE REQ HDG', b'Radians'),
			_dec='Required true heading to waypoint'
		)
		self.Avionics.add(
			'GPS_WP_VERTICAL_SPEED',
			(b'GPS WP VERTICAL SPEED', b'Meters per second'),
			_dec='Vertical speed to waypoint'
		)
		self.Avionics.add(
			'GPS_WP_TRACK_ANGLE_ERROR',
			(b'GPS WP TRACK ANGLE ERROR', b'Radians'),
			_dec='Tracking angle error to waypoint'
		)
		self.Avionics.add(
			'GPS_ETE',
			(b'GPS ETE', b'Seconds'),
			_dec='Estimated time enroute to destination'
		)
		self.Avionics.add(
			'GPS_ETA',
			(b'GPS ETA', b'Seconds'),
			_dec='Estimated time of arrival at destination'
		)
		self.Avionics.add(
			'GPS_WP_NEXT_LAT',
			(b'GPS WP NEXT LAT', b'Degrees'),
			_dec='Latitude of next waypoint'
		)
		self.Avionics.add(
			'GPS_WP_NEXT_LON',
			(b'GPS WP NEXT LON', b'Degrees'),
			_dec='Longitude of next waypoint'
		)
		self.Avionics.add(
			'GPS_WP_NEXT_ALT',
			(b'GPS WP NEXT ALT', b'Meters'),
			_dec='Altitude of next waypoint'
		)
		self.Avionics.add(
			'GPS_WP_PREV_VALID',
			(b'GPS WP PREV VALID', b'Bool'),
			_dec='Is previous waypoint valid (i.e. current waypoint is not the first waypoint)'
		)
		self.Avionics.add(
			'GPS_WP_PREV_LAT',
			(b'GPS WP PREV LAT', b'Degrees'),
			_dec='Latitude of previous waypoint'
		)
		self.Avionics.add(
			'GPS_WP_PREV_LON',
			(b'GPS WP PREV LON', b'Degrees'),
			_dec='Longitude of previous waypoint'
		)
		self.Avionics.add(
			'GPS_WP_PREV_ALT',
			(b'GPS WP PREV ALT', b'Meters'),
			_dec='Altitude of previous waypoint'
		)
		self.Avionics.add(
			'GPS_WP_ETE',
			(b'GPS WP ETE', b'Seconds'),
			_dec='Estimated time enroute to waypoint'
		)
		self.Avionics.add(
			'GPS_WP_ETA',
			(b'GPS WP ETA', b'Seconds'),
			_dec='Estimated time of arrival at waypoint'
		)
		self.Avionics.add(
			'GPS_COURSE_TO_STEER',
			(b'GPS COURSE TO STEER', b'Radians'),
			_dec='Suggested heading to steer (for autopilot)'
		)
		self.Avionics.add(
			'GPS_FLIGHT_PLAN_WP_INDEX',
			(b'GPS FLIGHT PLAN WP INDEX', b'Number'),
			_dec='Index of waypoint'
		)
		self.Avionics.add(
			'GPS_FLIGHT_PLAN_WP_COUNT',
			(b'GPS FLIGHT PLAN WP COUNT', b'Number'),
			_dec='Number of waypoints'
		)
		self.Avionics.add(
			'GPS_IS_ACTIVE_WP_LOCKED',
			(b'GPS IS ACTIVE WP LOCKED', b'Bool'),
			_dec='Is switching to next waypoint locked'
		)
		self.Avionics.add(
			'GPS_IS_APPROACH_LOADED',
			(b'GPS IS APPROACH LOADED', b'Bool'),
			_dec='Is approach loaded'
		)
		self.Avionics.add(
			'GPS_IS_APPROACH_ACTIVE',
			(b'GPS IS APPROACH ACTIVE', b'Bool'),
			_dec='Is approach mode active'
		)
		self.Avionics.add(
			'GPS_APPROACH_IS_WP_RUNWAY',
			(b'GPS APPROACH IS WP RUNWAY', b'Bool'),
			_dec='Waypoint is the runway'
		)
		self.Avionics.add(
			'GPS_APPROACH_APPROACH_INDEX',
			(b'GPS APPROACH APPROACH INDEX', b'Number'),
			_dec='Index of approach for given airport'
		)
		self.Avionics.add(
			'GPS_APPROACH_TRANSITION_INDEX',
			(b'GPS APPROACH TRANSITION INDEX', b'Number'),
			_dec='Index of approach transition'
		)
		self.Avionics.add(
			'GPS_APPROACH_IS_FINAL',
			(b'GPS APPROACH IS FINAL', b'Bool'),
			_dec='Is approach transition final approach segment'
		)
		self.Avionics.add(
			'GPS_APPROACH_IS_MISSED',
			(b'GPS APPROACH IS MISSED', b'Bool'),
			_dec='Is approach segment missed approach segment'
		)
		self.Avionics.add(
			'GPS_APPROACH_TIMEZONE_DEVIATION',
			(b'GPS APPROACH TIMEZONE DEVIATION', b'Seconds'),
			_dec='Deviation of local time from GMT'
		)
		self.Avionics.add(
			'GPS_APPROACH_WP_INDEX',
			(b'GPS APPROACH WP INDEX', b'Number'),
			_dec='Index of current waypoint'
		)
		self.Avionics.add(
			'GPS_APPROACH_WP_COUNT',
			(b'GPS APPROACH WP COUNT', b'Number'),
			_dec='Number of waypoints'
		)
		self.Avionics.add(
			'GPS_DRIVES_NAV1',
			(b'GPS DRIVES NAV1', b'Bool'),
			_dec='GPS is driving Nav 1 indicator'
		)
		self.Avionics.add(
			'COM_RECEIVE_ALL',
			(b'COM RECEIVE ALL', b'Bool'),
			_dec='Toggles all COM radios to receive on'
		)
		self.Avionics.add(
			'COM_AVAILABLE',
			(b'COM AVAILABLE', b'Bool'),
			_dec='True if either COM1 or COM2 is available'
		)
		self.Avionics.add(
			'COM_TEST:index',
			(b'COM TEST:index', b'Bool'),
			_dec='Enter an index of 1 or 2. True if the COM system is working.'
		)
		self.Avionics.add(
			'TRANSPONDER_AVAILABLE',
			(b'TRANSPONDER AVAILABLE', b'Bool'),
			_dec='True if a transponder is available'
		)
		self.Avionics.add(
			'ADF_AVAILABLE',
			(b'ADF AVAILABLE', b'Bool'),
			_dec='True if ADF is available'
		)
		self.Avionics.add(
			'ADF_FREQUENCY:index',
			(b'ADF FREQUENCY:index', b'Frequency BCD16'),
			_dec='Legacy, use ADF ACTIVE FREQUENCY'
		)
		self.Avionics.add(
			'ADF_EXT_FREQUENCY:index',
			(b'ADF EXT FREQUENCY:index', b'Frequency BCD16'),
			_dec='Legacy, use ADF ACTIVE FREQUENCY'
		)
		self.Avionics.add(
			'ADF_IDENT',
			(b'ADF IDENT', b'String'),
			_dec='ICAO code'
		)
		self.Avionics.add(
			'ADF_NAME',
			(b'ADF NAME', b'String'),
			_dec='Descriptive name'
		)
		self.Avionics.add(
			'NAV_IDENT',
			(b'NAV IDENT', b'String'),
			_dec='ICAO code'
		)
		self.Avionics.add(
			'NAV_NAME',
			(b'NAV NAME', b'String'),
			_dec='Descriptive name'
		)
		self.Avionics.add(
			'NAV_GLIDE_SLOPE',
			(b'NAV GLIDE SLOPE', b'Number'),
			_dec='The glide slope gradient.'
		)
		self.Avionics.add(
			'NAV_RELATIVE_BEARING_TO_STATION:index',
			(b'NAV RELATIVE BEARING TO STATION:index', b'Degrees'),
			_dec='Relative bearing to station'
		)
		self.Avionics.add(
			'SELECTED_DME',
			(b'SELECTED DME', b'Number'),
			_dec='Selected DME'
		)
		self.Avionics.add(
			'GPS_WP_NEXT_ID',
			(b'GPS WP NEXT ID', b'String'),
			_dec='ID of next GPS waypoint'
		)
		self.Avionics.add(
			'GPS_WP_PREV_ID',
			(b'GPS WP PREV ID', b'String'),
			_dec='ID of previous GPS waypoint'
		)
		self.Avionics.add(
			'GPS_TARGET_DISTANCE',
			(b'GPS TARGET DISTANCE', b'Meters'),
			_dec='Distance to target'
		)
		self.Avionics.add(
			'GPS_TARGET_ALTITUDE',
			(b'GPS TARGET ALTITUDE', b'Meters'),
			_dec='Altitude of GPS target'
		)
		self.Avionics.add(
			'ADF_LATLONALT:index',
			(b'ADF LATLONALT:index', b'SIMCONNECT_DATA_LATLONALTstructure'),
			_dec='''
			Returns the latitude, longitude and altitude of the station
			the radio equipment is currently tuned to, or zeros if the
			radio is not tuned to any ADF station.
			Index of 1 or 2 for ADF 1 and ADF 2.'''
		)
		self.Avionics.add(
			'NAV_VOR_LATLONALT:index',
			(b'NAV VOR LATLONALT:index', b'SIMCONNECT_DATA_LATLONALTstructure'),
			_dec='Returns the VOR station latitude, longitude and altitude.'
		)
		self.Avionics.add(
			'NAV_GS_LATLONALT:index',
			(b'NAV GS LATLONALT:index', b'SIMCONNECT_DATA_LATLONALTstructure'),
			_dec='Returns the glide slope.'
		)
		self.Avionics.add(
			'NAV_DME_LATLONALT:index',
			(b'NAV DME LATLONALT:index', b'SIMCONNECT_DATA_LATLONALTstructure'),
			_dec='Returns the DME station.'
		)
		self.Avionics.add(
			'INNER_MARKER_LATLONALT',
			(b'INNER MARKER LATLONALT', b'SIMCONNECT_DATA_LATLONALTstructure'),
			_dec='''
				Returns the latitude, longitude and altitude of the inner marker 
				of an approach to a runway, if the aircraft is within the required 
				proximity, otherwise it will return zeros.'''
		)
		self.Avionics.add(
			'MIDDLE_MARKER_LATLONALT',
			(b'MIDDLE MARKER LATLONALT', b'SIMCONNECT_DATA_LATLONALTstructure'),
			_dec='Returns the latitude, longitude and altitude of the middle marker.'
		)
		self.Avionics.add(
			'OUTER_MARKER_LATLONALT',
			(b'OUTER MARKER LATLONALT', b'SIMCONNECT_DATA_LATLONALTstructure'),
			_dec='Returns the latitude, longitude and altitude of the outer marker.'
		)


		self.Controls = sm.new_request_holder()
		self.Controls.add(
			'YOKE_Y_POSITION',
			(b'YOKE Y POSITION', b'Position (-16K to 0) -16K = Yoke fully pushed in'),
			_dec='Percent control deflection fore/aft (for animation)'
		)
		self.Controls.add(
			'YOKE_X_POSITION',
			(b'YOKE X POSITION', b'Position (-16K to 0) -16K ='),
			_dec='Percent control deflection left/right (for animation)'
		)
		self.Controls.add(
			'RUDDER_PEDAL_POSITION',
			(b'RUDDER PEDAL POSITION', b'Position (-16K to 0) -16K = left pedal pushed full in'),
			_dec='Percent rudder pedal deflection (for animation)'
		)
		self.Controls.add(
			'RUDDER_POSITION',
			(b'RUDDER POSITION', b'Position (-16K to 0) -16K = full left'),
			_dec='Percent rudder input deflection'
		)
		self.Controls.add(
			'ELEVATOR_POSITION',
			(b'ELEVATOR POSITION', b'Position (-16K to 0) -16K = full down'),
			_dec='Percent elevator input deflection'
		)
		self.Controls.add(
			'AILERON_POSITION',
			(b'AILERON POSITION', b'Position (-16K to 0) -16K = full left'),
			_dec='Percent aileron input left/right'
		)
		self.Controls.add(
			'ELEVATOR_TRIM_POSITION',
			(b'ELEVATOR TRIM POSITION', b'Radians'),
			_dec='Elevator trim deflection'
		)
		self.Controls.add(
			'ELEVATOR_TRIM_INDICATOR',
			(b'ELEVATOR TRIM INDICATOR', b'Position (-16K to 0) -16K = full down'),
			_dec='Percent elevator trim (for indication)'
		)
		self.Controls.add(
			'ELEVATOR_TRIM_PCT',
			(b'ELEVATOR TRIM PCT', b'Percent Over 100'),
			_dec='Percent elevator trim'
		)
		self.Controls.add(
			'BRAKE_LEFT_POSITION',
			(b'BRAKE LEFT POSITION', b'Position (0 to 32K) 0 = off, 32K full'),
			_dec='Percent left brake'
		)
		self.Controls.add(
			'BRAKE_RIGHT_POSITION',
			(b'BRAKE RIGHT POSITION', b'Position (0 to 32K) 0 = off, 32K full'),
			_dec='Percent right brake'
		)
		self.Controls.add(
			'BRAKE_INDICATOR',
			(b'BRAKE INDICATOR', b'Position (0 to 16K) 0 = off, 16K full'),
			_dec='Brake on indication'
		)
		self.Controls.add(
			'BRAKE_PARKING_POSITION',
			(b'BRAKE PARKING POSITION', b'Position (0 to 32K) 0 = off, 32K full'),
			_dec='Parking brake on'
		)
		self.Controls.add(
			'BRAKE_PARKING_INDICATOR',
			(b'BRAKE PARKING INDICATOR', b'Bool'),
			_dec='Parking brake indicator'
		)
		self.Controls.add(
			'SPOILERS_ARMED',
			(b'SPOILERS ARMED', b'Bool'),
			_dec='Auto-spoilers armed'
		)
		self.Controls.add(
			'SPOILERS_HANDLE_POSITION',
			(b'SPOILERS HANDLE POSITION', b'Percent Over 100 or Position (16K = down, 0 = up)'),
			_dec='Spoiler handle position'
		)
		self.Controls.add(
			'SPOILERS_LEFT_POSITION',
			(b'SPOILERS LEFT POSITION', b'Percent Over 100 or Position (0 = retracted, 16K fully extended)'),
			_dec='Percent left spoiler deflected'
		)
		self.Controls.add(
			'SPOILERS_RIGHT_POSITION',
			(b'SPOILERS RIGHT POSITION', b'Percent Over 100 or Position (0 = retracted, 16K fully extended)'),
			_dec='Percent right spoiler deflected'
		)
		self.Controls.add(
			'FLAPS_HANDLE_PERCENT',
			(b'FLAPS HANDLE PERCENT', b'Percent Over 100'),
			_dec='Percent flap handle extended'
		)
		self.Controls.add(
			'FLAPS_HANDLE_INDEX',
			(b'FLAPS HANDLE INDEX', b'Number'),
			_dec='Index of current flap position'
		)
		self.Controls.add(
			'FLAPS_NUM_HANDLE_POSITIONS',
			(b'FLAPS NUM HANDLE POSITIONS', b'Number'),
			_dec='Number of flap positions'
		)
		self.Controls.add(
			'TRAILING_EDGE_FLAPS_LEFT_PERCENT',
			(b'TRAILING EDGE FLAPS LEFT PERCENT', b'Percent Over 100'),
			_dec='Percent left trailing edge flap extended'
		)
		self.Controls.add(
			'TRAILING_EDGE_FLAPS_RIGHT_PERCENT',
			(b'TRAILING EDGE FLAPS RIGHT PERCENT', b'Percent Over 100'),
			_dec='Percent right trailing edge flap extended'
		)
		self.Controls.add(
			'TRAILING_EDGE_FLAPS_LEFT_ANGLE',
			(b'TRAILING EDGE FLAPS LEFT ANGLE', b'Radians'),
			_dec='Angle left trailing edge flap extended. Use TRAILING EDGE FLAPS LEFT PERCENT to set a value.'
		)
		self.Controls.add(
			'TRAILING_EDGE_FLAPS_RIGHT_ANGLE',
			(b'TRAILING EDGE FLAPS RIGHT ANGLE', b'Radians'),
			_dec='Angle right trailing edge flap extended. Use TRAILING EDGE FLAPS RIGHT PERCENT to set a value.'
		)
		self.Controls.add(
			'LEADING_EDGE_FLAPS_LEFT_PERCENT',
			(b'LEADING EDGE FLAPS LEFT PERCENT', b'Percent Over 100'),
			_dec='Percent left leading edge flap extended'
		)
		self.Controls.add(
			'LEADING_EDGE_FLAPS_RIGHT_PERCENT',
			(b'LEADING EDGE FLAPS RIGHT PERCENT', b'Percent Over 100'),
			_dec='Percent right leading edge flap extended'
		)
		self.Controls.add(
			'LEADING_EDGE_FLAPS_LEFT_ANGLE',
			(b'LEADING EDGE FLAPS LEFT ANGLE', b'Radians'),
			_dec='Angle left leading edge flap extended. Use LEADING EDGE FLAPS LEFT PERCENT to set a value.'
		)
		self.Controls.add(
			'LEADING_EDGE_FLAPS_RIGHT_ANGLE',
			(b'LEADING EDGE FLAPS RIGHT ANGLE', b'Radians'),
			_dec='Angle right leading edge flap extended. Use LEADING EDGE FLAPS RIGHT PERCENT to set a value.'
		)
		self.Controls.add(
			'AILERON_LEFT_DEFLECTION',
			(b'AILERON LEFT DEFLECTION', b'Radians'),
			_dec='Angle deflection'
		)
		self.Controls.add(
			'AILERON_LEFT_DEFLECTION_PCT',
			(b'AILERON LEFT DEFLECTION PCT', b'Percent Over 100'),
			_dec='Percent deflection'
		)
		self.Controls.add(
			'AILERON_RIGHT_DEFLECTION',
			(b'AILERON RIGHT DEFLECTION', b'Radians'),
			_dec='Angle deflection'
		)
		self.Controls.add(
			'AILERON_RIGHT_DEFLECTION_PCT',
			(b'AILERON RIGHT DEFLECTION PCT', b'Percent Over 100'),
			_dec='Percent deflection'
		)
		self.Controls.add(
			'AILERON_AVERAGE_DEFLECTION',
			(b'AILERON AVERAGE DEFLECTION', b'Radians'),
			_dec='Angle deflection'
		)
		self.Controls.add(
			'AILERON_TRIM',
			(b'AILERON TRIM', b'Radians'),
			_dec='Angle deflection'
		)
		self.Controls.add(
			'AILERON_TRIM_PCT',
			(b'AILERON TRIM PCT', b'Percent Over 100'),
			_dec='Percent deflection'
		)
		self.Controls.add(
			'RUDDER_DEFLECTION',
			(b'RUDDER DEFLECTION', b'Radians'),
			_dec='Angle deflection'
		)
		self.Controls.add(
			'RUDDER_DEFLECTION_PCT',
			(b'RUDDER DEFLECTION PCT', b'Percent Over 100'),
			_dec='Percent deflection'
		)
		self.Controls.add(
			'RUDDER_TRIM',
			(b'RUDDER TRIM', b'Radians'),
			_dec='Angle deflection'
		)
		self.Controls.add(
			'RUDDER_TRIM_PCT',
			(b'RUDDER TRIM PCT', b'Percent Over 100'),
			_dec='Percent deflection'
		)
		self.Controls.add(
			'FLAPS_AVAILABLE',
			(b'FLAPS AVAILABLE', b'Bool'),
			_dec='True if flaps available'
		)
		self.Controls.add(
			'FLAP_DAMAGE_BY_SPEED',
			(b'FLAP DAMAGE BY SPEED', b'Bool'),
			_dec='True if flagps are damaged by excessive speed'
		)
		self.Controls.add(
			'FLAP_SPEED_EXCEEDED',
			(b'FLAP SPEED EXCEEDED', b'Bool'),
			_dec='True if safe speed limit for flaps exceeded'
		)
		self.Controls.add(
			'ELEVATOR_DEFLECTION',
			(b'ELEVATOR DEFLECTION', b'Radians'),
			_dec='Angle deflection'
		)
		self.Controls.add(
			'ELEVATOR_DEFLECTION_PCT',
			(b'ELEVATOR DEFLECTION PCT', b'Percent Over 100'),
			_dec='Percent deflection'
		)
		self.Controls.add(
			'ALTERNATE_STATIC_SOURCE_OPEN',
			(b'ALTERNATE STATIC SOURCE OPEN', b'Bool'),
			_dec='Alternate static air source'
		)
		self.Controls.add(
			'AILERON_TRIM_PCT',
			(b'AILERON TRIM PCT', b'Float. Percent over 100'),
			_dec='The trim position of the ailerons. Zero is fully retracted.'
		)
		self.Controls.add(
			'RUDDER_TRIM_PCT',
			(b'RUDDER TRIM PCT', b'Float. Percent over 100'),
			_dec='The trim position of the rudder. Zero is no trim.'
		)
		self.Controls.add(
			'FOLDING_WING_HANDLE_POSITION',
			(b'FOLDING WING HANDLE POSITION', b'Bool'),
			_dec='True if the folding wing handle is engaged.'
		)
		self.Controls.add(
			'FUEL_DUMP_SWITCH',
			(b'FUEL DUMP SWITCH', b'Bool'),
			_dec='If true the aircraft is dumping fuel at the rate set in the configuration file.'
		)

		self.Autopilot = sm.new_request_holder()
		self.Autopilot.add(
			'AUTOPILOT_AVAILABLE',
			(b'AUTOPILOT AVAILABLE', b'Bool'),
			_dec='Available flag'
		)
		self.Autopilot.add(
			'AUTOPILOT_MASTER',
			(b'AUTOPILOT MASTER', b'Bool'),
			_dec='On/off flag'
		)
		self.Autopilot.add(
			'AUTOPILOT_NAV_SELECTED',
			(b'AUTOPILOT NAV SELECTED', b'Number'),
			_dec='Index of Nav radio selected'
		)
		self.Autopilot.add(
			'AUTOPILOT_WING_LEVELER',
			(b'AUTOPILOT WING LEVELER', b'Bool'),
			_dec='Wing leveler active'
		)
		self.Autopilot.add(
			'AUTOPILOT_NAV1_LOCK',
			(b'AUTOPILOT NAV1 LOCK', b'Bool'),
			_dec='Lateral nav mode active'
		)
		self.Autopilot.add(
			'AUTOPILOT_HEADING_LOCK',
			(b'AUTOPILOT HEADING LOCK', b'Bool'),
			_dec='Heading mode active'
		)
		self.Autopilot.add(
			'AUTOPILOT_HEADING_LOCK_DIR',
			(b'AUTOPILOT HEADING LOCK DIR', b'Degrees'),
			_dec='Selected heading'
		)
		self.Autopilot.add(
			'AUTOPILOT_ALTITUDE_LOCK',
			(b'AUTOPILOT ALTITUDE LOCK', b'Bool'),
			_dec='Altitude hole active'
		)
		self.Autopilot.add(
			'AUTOPILOT_ALTITUDE_LOCK_VAR',
			(b'AUTOPILOT ALTITUDE LOCK VAR', b'Feet'),
			_dec='Selected altitude'
		)
		self.Autopilot.add(
			'AUTOPILOT_ATTITUDE_HOLD',
			(b'AUTOPILOT ATTITUDE HOLD', b'Bool'),
			_dec='Attitude hold active'
		)
		self.Autopilot.add(
			'AUTOPILOT_GLIDESLOPE_HOLD',
			(b'AUTOPILOT GLIDESLOPE HOLD', b'Bool'),
			_dec='GS hold active'
		)
		self.Autopilot.add(
			'AUTOPILOT_PITCH_HOLD_REF',
			(b'AUTOPILOT PITCH HOLD REF', b'Radians'),
			_dec='Current reference pitch'
		)
		self.Autopilot.add(
			'AUTOPILOT_APPROACH_HOLD',
			(b'AUTOPILOT APPROACH HOLD', b'Bool'),
			_dec='Approach mode active'
		)
		self.Autopilot.add(
			'AUTOPILOT_BACKCOURSE_HOLD',
			(b'AUTOPILOT BACKCOURSE HOLD', b'Bool'),
			_dec='Back course mode active'
		)
		self.Autopilot.add(
			'AUTOPILOT_VERTICAL_HOLD_VAR',
			(b'AUTOPILOT VERTICAL HOLD VAR', b'Feet/minute'),
			_dec='Selected vertical speed'
		)
		self.Autopilot.add(
			'AUTOPILOT_PITCH_HOLD',
			(b'AUTOPILOT PITCH HOLD', b'Bool'),
			_dec='Set to True if the autopilot pitch hold has is engaged.'
		)
		self.Autopilot.add(
			'AUTOPILOT_FLIGHT_DIRECTOR_ACTIVE',
			(b'AUTOPILOT FLIGHT DIRECTOR ACTIVE', b'Bool'),
			_dec='Flight director active'
		)
		self.Autopilot.add(
			'AUTOPILOT_FLIGHT_DIRECTOR_PITCH',
			(b'AUTOPILOT FLIGHT DIRECTOR PITCH', b'Radians'),
			_dec='Reference pitch angle'
		)
		self.Autopilot.add(
			'AUTOPILOT_FLIGHT_DIRECTOR_BANK',
			(b'AUTOPILOT FLIGHT DIRECTOR BANK', b'Radians'),
			_dec='Reference bank angle'
		)
		self.Autopilot.add(
			'AUTOPILOT_AIRSPEED_HOLD',
			(b'AUTOPILOT AIRSPEED HOLD', b'Bool'),
			_dec='Airspeed hold active'
		)
		self.Autopilot.add(
			'AUTOPILOT_AIRSPEED_HOLD_VAR',
			(b'AUTOPILOT AIRSPEED HOLD VAR', b'Knots'),
			_dec='Selected airspeed'
		)
		self.Autopilot.add(
			'AUTOPILOT_MACH_HOLD',
			(b'AUTOPILOT MACH HOLD', b'Bool'),
			_dec='Mach hold active'
		)
		self.Autopilot.add(
			'AUTOPILOT_MACH_HOLD_VAR',
			(b'AUTOPILOT MACH HOLD VAR', b'Number'),
			_dec='Selected mach'
		)
		self.Autopilot.add(
			'AUTOPILOT_YAW_DAMPER',
			(b'AUTOPILOT YAW DAMPER', b'Bool'),
			_dec='Yaw damper active'
		)
		self.Autopilot.add(
			'AUTOPILOT_RPM_HOLD_VAR',
			(b'AUTOPILOT RPM HOLD VAR', b'Number'),
			_dec='Selected rpm'
		)
		self.Autopilot.add(
			'AUTOPILOT_THROTTLE_ARM',
			(b'AUTOPILOT THROTTLE ARM', b'Bool'),
			_dec='Autothrottle armed'
		)
		self.Autopilot.add(
			'AUTOPILOT_TAKEOFF_POWER_ACTIVE',
			(b'AUTOPILOT TAKEOFF POWER ACTIVE', b'Bool'),
			_dec='Takeoff / Go Around power mode active'
		)
		self.Autopilot.add(
			'AUTOTHROTTLE_ACTIVE',
			(b'AUTOTHROTTLE ACTIVE', b'Bool'),
			_dec='Auto-throttle active'
		)
		self.Autopilot.add(
			'AUTOPILOT_NAV1_LOCK',
			(b'AUTOPILOT NAV1 LOCK', b'Bool'),
			_dec='True if autopilot nav1 lock applied'
		)
		self.Autopilot.add(
			'AUTOPILOT_VERTICAL_HOLD',
			(b'AUTOPILOT VERTICAL HOLD', b'Bool'),
			_dec='True if autopilot vertical hold applied'
		)
		self.Autopilot.add(
			'AUTOPILOT_RPM_HOLD',
			(b'AUTOPILOT RPM HOLD', b'Bool'),
			_dec='True if autopilot rpm hold applied'
		)
		self.Autopilot.add(
			'AUTOPILOT_MAX_BANK',
			(b'AUTOPILOT MAX BANK', b'Radians'),
			_dec='True if autopilot max bank applied'
		)
		self.Autopilot.add(
			'FLY_BY_WIRE_ELAC_SWITCH',
			(b'FLY BY WIRE ELAC SWITCH', b'Bool'),
			_dec='True if the fly by wire Elevators and Ailerons computer is on.'
		)
		self.Autopilot.add(
			'FLY_BY_WIRE_FAC_SWITCH',
			(b'FLY BY WIRE FAC SWITCH', b'Bool'),
			_dec='True if the fly by wire Flight Augmentation computer is on.'
		)
		self.Autopilot.add(
			'FLY_BY_WIRE_SEC_SWITCH',
			(b'FLY BY WIRE SEC SWITCH', b'Bool'),
			_dec='True if the fly by wire Spoilers and Elevators computer is on.'
		)
		self.Autopilot.add(
			'FLY_BY_WIRE_ELAC_FAILED',
			(b'FLY BY WIRE ELAC FAILED', b'Bool'),
			_dec='True if the Elevators and Ailerons computer has failed.'
		)
		self.Autopilot.add(
			'FLY_BY_WIRE_FAC_FAILED',
			(b'FLY BY WIRE FAC FAILED', b'Bool'),
			_dec='True if the Flight Augmentation computer has failed.'
		)
		self.Autopilot.add(
			'FLY_BY_WIRE_SEC_FAILED',
			(b'FLY BY WIRE SEC FAILED', b'Bool'),
			_dec='True if the Spoilers and Elevators computer has failed.'
		)


		self.Landing_Gear = sm.new_request_holder()
		self.Landing_Gear.add(
			'IS_GEAR_RETRACTABLE',
			(b'IS GEAR RETRACTABLE', b'Bool'),
			_dec='True if gear can be retracted'
		)
		self.Landing_Gear.add(
			'IS_GEAR_SKIS',
			(b'IS GEAR SKIS', b'Bool'),
			_dec='True if landing gear is skis'
		)
		self.Landing_Gear.add(
			'IS_GEAR_FLOATS',
			(b'IS GEAR FLOATS', b'Bool'),
			_dec='True if landing gear is floats'
		)
		self.Landing_Gear.add(
			'IS_GEAR_SKIDS',
			(b'IS GEAR SKIDS', b'Bool'),
			_dec='True if landing gear is skids'
		)
		self.Landing_Gear.add(
			'IS_GEAR_WHEELS',
			(b'IS GEAR WHEELS', b'Bool'),
			_dec='True if landing gear is wheels'
		)
		self.Landing_Gear.add(
			'GEAR_HANDLE_POSITION',
			(b'GEAR HANDLE POSITION', b'Bool'),
			_dec='True if gear handle is applied'
		)
		self.Landing_Gear.add(
			'GEAR_HYDRAULIC_PRESSURE',
			(b'GEAR HYDRAULIC PRESSURE', b'Pound force per square foot (psf)'),
			_dec='Gear hydraulic pressure'
		)
		self.Landing_Gear.add(
			'TAILWHEEL_LOCK_ON',
			(b'TAILWHEEL LOCK ON', b'Bool'),
			_dec='True if tailwheel lock applied'
		)
		self.Landing_Gear.add(
			'GEAR_CENTER_POSITION',
			(b'GEAR CENTER POSITION', b'Percent Over 100'),
			_dec='Percent center gear extended'
		)
		self.Landing_Gear.add(
			'GEAR_LEFT_POSITION',
			(b'GEAR LEFT POSITION', b'Percent Over 100'),
			_dec='Percent left gear extended'
		)
		self.Landing_Gear.add(
			'GEAR_RIGHT_POSITION',
			(b'GEAR RIGHT POSITION', b'Percent Over 100'),
			_dec='Percent right gear extended'
		)
		self.Landing_Gear.add(
			'GEAR_TAIL_POSITION',
			(b'GEAR TAIL POSITION', b'Percent Over 100'),
			_dec='Percent tail gear extended'
		)
		self.Landing_Gear.add(
			'GEAR_AUX_POSITION',
			(b'GEAR AUX POSITION', b'Percent Over 100'),
			_dec='Percent auxiliary gear extended'
		)
		self.Landing_Gear.add(
			'GEAR_ANIMATION_POSITION:index',
			(b'GEAR ANIMATION POSITION:index', b'Number'),
			_dec='Percent gear animation extended'
		)
		self.Landing_Gear.add(
			'GEAR_TOTAL_PCT_EXTENDED',
			(b'GEAR TOTAL PCT EXTENDED', b'Percentage'),
			_dec='Percent total gear extended'
		)
		self.Landing_Gear.add(
			'AUTO_BRAKE_SWITCH_CB',
			(b'AUTO BRAKE SWITCH CB', b'Number'),
			_dec='Auto brake switch position'
		)
		self.Landing_Gear.add(
			'WATER_RUDDER_HANDLE_POSITION',
			(b'WATER RUDDER HANDLE POSITION', b'Percent Over 100'),
			_dec='Position of the water rudder handle (0 handle retracted, 100 rudder handle applied)'
		)
		self.Landing_Gear.add(
			'WATER_LEFT_RUDDER_EXTENDED',
			(b'WATER LEFT RUDDER EXTENDED', b'Percentage'),
			_dec='Percent extended'
		)
		self.Landing_Gear.add(
			'WATER_RIGHT_RUDDER_EXTENDED',
			(b'WATER RIGHT RUDDER EXTENDED', b'Percentage'),
			_dec='Percent extended'
		)
		self.Landing_Gear.add(
			'GEAR_CENTER_STEER_ANGLE',
			(b'GEAR CENTER STEER ANGLE', b'Percent Over 100'),
			_dec='Center wheel angle, negative to the left, positive to the right.'
		)
		self.Landing_Gear.add(
			'GEAR_LEFT_STEER_ANGLE',
			(b'GEAR LEFT STEER ANGLE', b'Percent Over 100'),
			_dec='Left wheel angle, negative to the left, positive to the right.'
		)
		self.Landing_Gear.add(
			'GEAR_RIGHT_STEER_ANGLE',
			(b'GEAR RIGHT STEER ANGLE', b'Percent Over 100'),
			_dec='Right wheel angle, negative to the left, positive to the right.'
		)
		self.Landing_Gear.add(
			'GEAR_AUX_STEER_ANGLE',
			(b'GEAR AUX STEER ANGLE', b'Percent Over 100'),
			_dec='''
			Aux wheel angle, negative to the left,
			positive to the right.
			The aux wheel is the fourth set of gear,
			sometimes used on helicopters.'''
		)
		self.Landing_Gear.add(
			'WATER_LEFT_RUDDER_STEER_ANGLE',
			(b'WATER LEFT RUDDER STEER ANGLE', b'Percent Over 100'),
			_dec='Water left rudder angle, negative to the left, positive to the right.'
		)
		self.Landing_Gear.add(
			'WATER_RIGHT_RUDDER_STEER_ANGLE',
			(b'WATER RIGHT RUDDER STEER ANGLE', b'Percent Over 100'),
			_dec='Water right rudder angle, negative to the left, positive to the right.'
		)
		self.Landing_Gear.add(
			'GEAR_CENTER_STEER_ANGLE_PCT',
			(b'GEAR CENTER STEER ANGLE PCT', b'Percent Over 100'),
			_dec='Center steer angle as a percentage'
		)
		self.Landing_Gear.add(
			'GEAR_LEFT_STEER_ANGLE_PCT',
			(b'GEAR LEFT STEER ANGLE PCT', b'Percent Over 100'),
			_dec='Left steer angle as a percentage'
		)
		self.Landing_Gear.add(
			'GEAR_RIGHT_STEER_ANGLE_PCT',
			(b'GEAR RIGHT STEER ANGLE PCT', b'Percent Over 100'),
			_dec='Right steer angle as a percentage'
		)
		self.Landing_Gear.add(
			'GEAR_AUX_STEER_ANGLE_PCT',
			(b'GEAR AUX STEER ANGLE PCT', b'Percent Over 100'),
			_dec='Aux steer angle as a percentage'
		)
		self.Landing_Gear.add(
			'WATER_LEFT_RUDDER_STEER_ANGLE_PCT',
			(b'WATER LEFT RUDDER STEER ANGLE PCT', b'Percent Over 100'),
			_dec='Water left rudder angle as a percentage'
		)
		self.Landing_Gear.add(
			'WATER_RIGHT_RUDDER_STEER_ANGLE_PCT',
			(b'WATER RIGHT RUDDER STEER ANGLE PCT', b'Percent Over 100'),
			_dec='Water right rudder as a percentage'
		)
		self.Landing_Gear.add(
			'CENTER_WHEEL_RPM',
			(b'CENTER WHEEL RPM', b'Rpm'),
			_dec='Center landing gear rpm'
		)
		self.Landing_Gear.add(
			'LEFT_WHEEL_RPM',
			(b'LEFT WHEEL RPM', b'Rpm'),
			_dec='Left landing gear rpm'
		)
		self.Landing_Gear.add(
			'RIGHT_WHEEL_RPM',
			(b'RIGHT WHEEL RPM', b'Rpm'),
			_dec='Right landing gear rpm'
		)
		self.Landing_Gear.add(
			'AUX_WHEEL_RPM',
			(b'AUX WHEEL RPM', b'Rpm'),
			_dec='Rpm of fourth set of gear wheels.'
		)
		self.Landing_Gear.add(
			'CENTER_WHEEL_ROTATION_ANGLE',
			(b'CENTER WHEEL ROTATION ANGLE', b'Radians'),
			_dec='Center wheel rotation angle'
		)
		self.Landing_Gear.add(
			'LEFT_WHEEL_ROTATION_ANGLE',
			(b'LEFT WHEEL ROTATION ANGLE', b'Radians'),
			_dec='Left wheel rotation angle'
		)
		self.Landing_Gear.add(
			'RIGHT_WHEEL_ROTATION_ANGLE',
			(b'RIGHT WHEEL ROTATION ANGLE', b'Radians'),
			_dec='Right wheel rotation angle'
		)
		self.Landing_Gear.add(
			'AUX_WHEEL_ROTATION_ANGLE',
			(b'AUX WHEEL ROTATION ANGLE', b'Radians'),
			_dec='Aux wheel rotation angle'
		)
		self.Landing_Gear.add(
			'GEAR_EMERGENCY_HANDLE_POSITION',
			(b'GEAR EMERGENCY HANDLE POSITION', b'Bool'),
			_dec='True if gear emergency handle applied'
		)
		self.Landing_Gear.add(
			'ANTISKID_BRAKES_ACTIVE',
			(b'ANTISKID BRAKES ACTIVE', b'Bool'),
			_dec='True if antiskid brakes active'
		)
		self.Landing_Gear.add(
			'RETRACT_FLOAT_SWITCH',
			(b'RETRACT FLOAT SWITCH', b'Bool'),
			_dec='True if retract float switch on'
		)
		self.Landing_Gear.add(
			'RETRACT_LEFT_FLOAT_EXTENDED',
			(b'RETRACT LEFT FLOAT EXTENDED', b'Percent (0 is fully retracted, 100 is fully extended)'),
			_dec='If aircraft has retractable floats.'
		)
		self.Landing_Gear.add(
			'RETRACT_RIGHT_FLOAT_EXTENDED',
			(b'RETRACT RIGHT FLOAT EXTENDED', b'Percent (0 is fully retracted, 100 is fully extended)'),
			_dec='If aircraft has retractable floats.'
		)
		self.Landing_Gear.add(
			'STEER_INPUT_CONTROL',
			(b'STEER INPUT CONTROL', b'Percent over 100'),
			_dec='Position of steering tiller'
		)
		self.Landing_Gear.add(
			'GEAR_DAMAGE_BY_SPEED',
			(b'GEAR DAMAGE BY SPEED', b'Bool'),
			_dec='True if gear has been damaged by excessive speed'
		)
		self.Landing_Gear.add(
			'GEAR_SPEED_EXCEEDED',
			(b'GEAR SPEED EXCEEDED', b'Bool'),
			_dec='True if safe speed limit for gear exceeded'
		)
		self.Landing_Gear.add(
			'NOSEWHEEL_LOCK_ON',
			(b'NOSEWHEEL LOCK ON', b'Bool'),
			_dec='True if the nosewheel lock is engaged.'
		)

		self.Environment = sm.new_request_holder()
		self.Environment.add(
			'AMBIENT_DENSITY',
			(b'AMBIENT DENSITY', b'Slugs per cubic feet'),
			_dec='Ambient density'
		)
		self.Environment.add(
			'AMBIENT_TEMPERATURE',
			(b'AMBIENT TEMPERATURE', b'Celsius'),
			_dec='Ambient temperature'
		)
		self.Environment.add(
			'AMBIENT_PRESSURE',
			(b'AMBIENT PRESSURE', b'Inches of mercury, inHg'),
			_dec='Ambient pressure'
		)
		self.Environment.add(
			'AMBIENT_WIND_VELOCITY',
			(b'AMBIENT WIND VELOCITY', b'Knots'),
			_dec='Wind velocity'
		)
		self.Environment.add(
			'AMBIENT_WIND_DIRECTION',
			(b'AMBIENT WIND DIRECTION', b'Degrees'),
			_dec='Wind direction'
		)
		self.Environment.add(
			'AMBIENT_WIND_X',
			(b'AMBIENT WIND X', b'Meters per second'),
			_dec='Wind component in East/West direction.'
		)
		self.Environment.add(
			'AMBIENT_WIND_Y',
			(b'AMBIENT WIND Y', b'Meters per second'),
			_dec='Wind component in vertical direction.'
		)
		self.Environment.add(
			'AMBIENT_WIND_Z',
			(b'AMBIENT WIND Z', b'Meters per second'),
			_dec='Wind component in North/South direction.'
		)
		self.Environment.add(
			'STRUCT_AMBIENT_WIND',
			(b'STRUCT AMBIENT WIND', b'Feet_per_second'),
			_dec='X (latitude), Y (vertical) and Z (longitude) components of the wind.'
		)
		self.Environment.add(
			'AIRCRAFT_WIND_X',
			(b'AIRCRAFT WIND X', b'Knots'),
			_dec='Wind component in aircraft lateral axis'
		)
		self.Environment.add(
			'AIRCRAFT_WIND_Y',
			(b'AIRCRAFT WIND Y', b'Knots'),
			_dec='Wind component in aircraft vertical axis'
		)
		self.Environment.add(
			'AIRCRAFT_WIND_Z',
			(b'AIRCRAFT WIND Z', b'Knots'),
			_dec='Wind component in aircraft longitudinal axis'
		)
		self.Environment.add(
			'BAROMETER_PRESSURE',
			(b'BAROMETER PRESSURE', b'Millibars'),
			_dec='Barometric pressure'
		)
		self.Environment.add(
			'SEA_LEVEL_PRESSURE',
			(b'SEA LEVEL PRESSURE', b'Millibars'),
			_dec='Barometric pressure at sea level'
		)
		self.Environment.add(
			'TOTAL_AIR_TEMPERATURE',
			(b'TOTAL AIR TEMPERATURE', b'Celsius'),
			_dec='Total air temperature is the air temperature at the front of the aircraft where the ram pressure from the speed of the aircraft is taken into account.'
		)
		self.Environment.add(
			'WINDSHIELD_RAIN_EFFECT_AVAILABLE',
			(b'WINDSHIELD RAIN EFFECT AVAILABLE', b'Bool'),
			_dec='Is visual effect available on this aircraft'
		)
		self.Environment.add(
			'AMBIENT_IN_CLOUD',
			(b'AMBIENT IN CLOUD', b'Bool'),
			_dec='True if the aircraft is in a cloud.'
		)
		self.Environment.add(
			'AMBIENT_VISIBILITY',
			(b'AMBIENT VISIBILITY', b'Meters'),
			_dec='Ambient visibility'
		)
		self.Environment.add(
			'STANDARD_ATM_TEMPERATURE',
			(b'STANDARD ATM TEMPERATURE', b'Rankine'),
			_dec='Outside temperature on the standard ATM scale'
		)

		self.Miscellaneous_Systems = sm.new_request_holder()
		self.Miscellaneous_Systems.add(
			'SMOKE_ENABLE',
			(b'SMOKE ENABLE', b'Bool'),
			_dec='Set to True to activate the smoke system, if one is available (for example, on the Extra).'
		)
		self.Miscellaneous_Systems.add(
			'SMOKESYSTEM_AVAILABLE',
			(b'SMOKESYSTEM AVAILABLE', b'Bool'),
			_dec='Smoke system available'
		)
		self.Miscellaneous_Systems.add(
			'PITOT_HEAT',
			(b'PITOT HEAT', b'Bool'),
			_dec='Pitot heat active'
		)
		self.Miscellaneous_Systems.add(
			'FOLDING_WING_LEFT_PERCENT',
			(b'FOLDING WING LEFT PERCENT', b'Percent Over 100'),
			_dec='Left folding wing position, 100 is fully folded'
		)
		self.Miscellaneous_Systems.add(
			'FOLDING_WING_RIGHT_PERCENT',
			(b'FOLDING WING RIGHT PERCENT', b'Percent Over 100'),
			_dec='Right folding wing position, 100 is fully folded'
		)
		self.Miscellaneous_Systems.add(
			'CANOPY_OPEN',
			(b'CANOPY OPEN', b'Percent Over 100'),
			_dec='Percent primary door/exit open'
		)
		self.Miscellaneous_Systems.add(
			'TAILHOOK_POSITION',
			(b'TAILHOOK POSITION', b'Percent Over 100'),
			_dec='Percent tail hook extended'
		)
		self.Miscellaneous_Systems.add(
			'EXIT_OPEN:index',
			(b'EXIT OPEN:index', b'Percent Over 100'),
			_dec='Percent door/exit open'
		)
		self.Miscellaneous_Systems.add(
			'STALL_HORN_AVAILABLE',
			(b'STALL HORN AVAILABLE', b'Bool'),
			_dec='True if stall alarm available'
		)
		self.Miscellaneous_Systems.add(
			'ENGINE_MIXURE_AVAILABLE',
			(b'ENGINE MIXURE AVAILABLE', b'Bool'),
			_dec='True if engine mixture is available for prop engines. Obsolete value as mixture is always available. Spelling error in variable name.'
		)
		self.Miscellaneous_Systems.add(
			'CARB_HEAT_AVAILABLE',
			(b'CARB HEAT AVAILABLE', b'Bool'),
			_dec='True if carb heat available'
		)
		self.Miscellaneous_Systems.add(
			'SPOILER_AVAILABLE',
			(b'SPOILER AVAILABLE', b'Bool'),
			_dec='True if spoiler system available'
		)
		self.Miscellaneous_Systems.add(
			'IS_TAIL_DRAGGER',
			(b'IS TAIL DRAGGER', b'Bool'),
			_dec='True if the aircraft is a taildragger'
		)
		self.Miscellaneous_Systems.add(
			'STROBES_AVAILABLE',
			(b'STROBES AVAILABLE', b'Bool'),
			_dec='True if strobe lights are available'
		)
		self.Miscellaneous_Systems.add(
			'TOE_BRAKES_AVAILABLE',
			(b'TOE BRAKES AVAILABLE', b'Bool'),
			_dec='True if toe brakes are available'
		)
		self.Miscellaneous_Systems.add(
			'ELECTRICAL_MASTER_BATTERY',
			(b'ELECTRICAL MASTER BATTERY', b'Bool'),
			_dec='Battery switch position'
		)
		self.Miscellaneous_Systems.add(
			'ELECTRICAL_TOTAL_LOAD_AMPS',
			(b'ELECTRICAL TOTAL LOAD AMPS', b'Amperes'),
			_dec='Total load amps'
		)
		self.Miscellaneous_Systems.add(
			'ELECTRICAL_BATTERY_LOAD',
			(b'ELECTRICAL BATTERY LOAD', b'Amperes'),
			_dec='Battery load'
		)
		self.Miscellaneous_Systems.add(
			'ELECTRICAL_BATTERY_VOLTAGE',
			(b'ELECTRICAL BATTERY VOLTAGE', b'Volts'),
			_dec='Battery voltage'
		)
		self.Miscellaneous_Systems.add(
			'ELECTRICAL_MAIN_BUS_VOLTAGE',
			(b'ELECTRICAL MAIN BUS VOLTAGE', b'Volts'),
			_dec='Main bus voltage'
		)
		self.Miscellaneous_Systems.add(
			'ELECTRICAL_MAIN_BUS_AMPS',
			(b'ELECTRICAL MAIN BUS AMPS', b'Amperes'),
			_dec='Main bus current'
		)
		self.Miscellaneous_Systems.add(
			'ELECTRICAL_AVIONICS_BUS_VOLTAGE',
			(b'ELECTRICAL AVIONICS BUS VOLTAGE', b'Volts'),
			_dec='Avionics bus voltage'
		)
		self.Miscellaneous_Systems.add(
			'ELECTRICAL_AVIONICS_BUS_AMPS',
			(b'ELECTRICAL AVIONICS BUS AMPS', b'Amperes'),
			_dec='Avionics bus current'
		)
		self.Miscellaneous_Systems.add(
			'ELECTRICAL_HOT_BATTERY_BUS_VOLTAGE',
			(b'ELECTRICAL HOT BATTERY BUS VOLTAGE', b'Volts'),
			_dec='Voltage available when battery switch is turned off'
		)
		self.Miscellaneous_Systems.add(
			'ELECTRICAL_HOT_BATTERY_BUS_AMPS',
			(b'ELECTRICAL HOT BATTERY BUS AMPS', b'Amperes'),
			_dec='Current available when battery switch is turned off'
		)
		self.Miscellaneous_Systems.add(
			'ELECTRICAL_BATTERY_BUS_VOLTAGE',
			(b'ELECTRICAL BATTERY BUS VOLTAGE', b'Volts'),
			_dec='Battery bus voltage'
		)
		self.Miscellaneous_Systems.add(
			'ELECTRICAL_BATTERY_BUS_AMPS',
			(b'ELECTRICAL BATTERY BUS AMPS', b'Amperes'),
			_dec='Battery bus current'
		)
		self.Miscellaneous_Systems.add(
			'ELECTRICAL_GENALT_BUS_VOLTAGE:index',
			(b'ELECTRICAL GENALT BUS VOLTAGE:index', b'Volts'),
			_dec='Genalt bus voltage (takes engine index)'
		)
		self.Miscellaneous_Systems.add(
			'ELECTRICAL_GENALT_BUS_AMPS:index',
			(b'ELECTRICAL GENALT BUS AMPS:index', b'Amperes'),
			_dec='Genalt bus current (takes engine index)'
		)
		self.Miscellaneous_Systems.add(
			'CIRCUIT_GENERAL_PANEL_ON',
			(b'CIRCUIT GENERAL PANEL ON', b'Bool'),
			_dec='Is electrical power available to this circuit'
		)
		self.Miscellaneous_Systems.add(
			'CIRCUIT_FLAP_MOTOR_ON',
			(b'CIRCUIT FLAP MOTOR ON', b'Bool'),
			_dec='Is electrical power available to this circuit'
		)
		self.Miscellaneous_Systems.add(
			'CIRCUIT_GEAR_MOTOR_ON',
			(b'CIRCUIT GEAR MOTOR ON', b'Bool'),
			_dec='Is electrical power available to this circuit'
		)
		self.Miscellaneous_Systems.add(
			'CIRCUIT_AUTOPILOT_ON',
			(b'CIRCUIT AUTOPILOT ON', b'Bool'),
			_dec='Is electrical power available to this circuit'
		)
		self.Miscellaneous_Systems.add(
			'CIRCUIT_AVIONICS_ON',
			(b'CIRCUIT AVIONICS ON', b'Bool'),
			_dec='Is electrical power available to this circuit'
		)
		self.Miscellaneous_Systems.add(
			'CIRCUIT_PITOT_HEAT_ON',
			(b'CIRCUIT PITOT HEAT ON', b'Bool'),
			_dec='Is electrical power available to this circuit'
		)
		self.Miscellaneous_Systems.add(
			'CIRCUIT_PROP_SYNC_ON',
			(b'CIRCUIT PROP SYNC ON', b'Bool'),
			_dec='Is electrical power available to this circuit'
		)
		self.Miscellaneous_Systems.add(
			'CIRCUIT_AUTO_FEATHER_ON',
			(b'CIRCUIT AUTO FEATHER ON', b'Bool'),
			_dec='Is electrical power available to this circuit'
		)
		self.Miscellaneous_Systems.add(
			'CIRCUIT_AUTO_BRAKES_ON',
			(b'CIRCUIT AUTO BRAKES ON', b'Bool'),
			_dec='Is electrical power available to this circuit'
		)
		self.Miscellaneous_Systems.add(
			'CIRCUIT_STANDY_VACUUM_ON',
			(b'CIRCUIT STANDY VACUUM ON', b'Bool'),
			_dec='Is electrical power available to this circuit'
		)
		self.Miscellaneous_Systems.add(
			'CIRCUIT_MARKER_BEACON_ON',
			(b'CIRCUIT MARKER BEACON ON', b'Bool'),
			_dec='Is electrical power available to this circuit'
		)
		self.Miscellaneous_Systems.add(
			'CIRCUIT_GEAR_WARNING_ON',
			(b'CIRCUIT GEAR WARNING ON', b'Bool'),
			_dec='Is electrical power available to this circuit'
		)
		self.Miscellaneous_Systems.add(
			'CIRCUIT_HYDRAULIC_PUMP_ON',
			(b'CIRCUIT HYDRAULIC PUMP ON', b'Bool'),
			_dec='Is electrical power available to this circuit'
		)
		self.Miscellaneous_Systems.add(
			'HYDRAULIC_PRESSURE:index',
			(b'HYDRAULIC PRESSURE:index', b'Pound force per square foot'),
			_dec='Hydraulic system pressure. Indexes start at 1.'
		)
		self.Miscellaneous_Systems.add(
			'HYDRAULIC_RESERVOIR_PERCENT:index',
			(b'HYDRAULIC RESERVOIR PERCENT:index', b'Percent Over 100'),
			_dec='Hydraulic pressure changes will follow changes to this variable. Indexes start at 1.'
		)
		self.Miscellaneous_Systems.add(
			'HYDRAULIC_SYSTEM_INTEGRITY',
			(b'HYDRAULIC SYSTEM INTEGRITY', b'Percent Over 100'),
			_dec='Percent system functional'
		)
		self.Miscellaneous_Systems.add(
			'STRUCTURAL_DEICE_SWITCH',
			(b'STRUCTURAL DEICE SWITCH', b'Bool'),
			_dec='True if the aircraft structure deice switch is on'
		)
		self.Miscellaneous_Systems.add(
			'APPLY_HEAT_TO_SYSTEMS',
			(b'APPLY HEAT TO SYSTEMS', b'Bool'),
			_dec='Used when too close to a fire.'
		)
		self.Miscellaneous_Systems.add(
			'DROPPABLE_OBJECTS_TYPE:index',
			(b'DROPPABLE OBJECTS TYPE:index', b'String'),
			_dec='The type of droppable object at the station number identified by the index.'
		)
		self.Miscellaneous_Systems.add(
			'DROPPABLE_OBJECTS_COUNT:index',
			(b'DROPPABLE OBJECTS COUNT:index', b'Number'),
			_dec='The number of droppable objects at the station number identified by the index.'
		)

		self.Miscellaneous = sm.new_request_holder()
		self.Miscellaneous.add(
			'TOTAL_WEIGHT',
			(b'TOTAL WEIGHT', b'Pounds'),
			_dec='Total weight of the aircraft'
		)
		self.Miscellaneous.add(
			'MAX_GROSS_WEIGHT',
			(b'MAX GROSS WEIGHT', b'Pounds'),
			_dec='Maximum gross weight of the aircaft'
		)
		self.Miscellaneous.add(
			'EMPTY_WEIGHT',
			(b'EMPTY WEIGHT', b'Pounds'),
			_dec='Empty weight of the aircraft'
		)
		self.Miscellaneous.add(
			'IS_USER_SIM',
			(b'IS USER SIM', b'Bool'),
			_dec='Is this the user loaded aircraft'
		)
		self.Miscellaneous.add(
			'SIM_DISABLED',
			(b'SIM DISABLED', b'Bool'),
			_dec='Is sim disabled'
		)
		self.Miscellaneous.add(
			'G_FORCE',
			(b'G FORCE', b'GForce'),
			_dec='Current g force'
		)
		self.Miscellaneous.add(
			'ATC_HEAVY',
			(b'ATC HEAVY', b'Bool'),
			_dec='Is this aircraft recognized by ATC as heavy'
		)
		self.Miscellaneous.add(
			'AUTO_COORDINATION',
			(b'AUTO COORDINATION', b'Bool'),
			_dec='Is auto-coordination active'
		)
		self.Miscellaneous.add(
			'REALISM',
			(b'REALISM', b'Number'),
			_dec='General realism percent'
		)
		self.Miscellaneous.add(
			'TRUE_AIRSPEED_SELECTED',
			(b'TRUE AIRSPEED SELECTED', b'Bool'),
			_dec='True if True Airspeed has been selected'
		)
		self.Miscellaneous.add(
			'DESIGN_SPEED_VS0',
			(b'DESIGN SPEED VS0', b'Feet per second'),
			_dec='Design speed at VS0'
		)
		self.Miscellaneous.add(
			'DESIGN_SPEED_VS1',
			(b'DESIGN SPEED VS1', b'Feet per second'),
			_dec='Design speed at VS1'
		)
		self.Miscellaneous.add(
			'DESIGN_SPEED_VC',
			(b'DESIGN SPEED VC', b'Feet per second'),
			_dec='Design speed at VC'
		)
		self.Miscellaneous.add(
			'MIN_DRAG_VELOCITY',
			(b'MIN DRAG VELOCITY', b'Feet per second'),
			_dec='Minimum drag velocity'
		)
		self.Miscellaneous.add(
			'ESTIMATED_CRUISE_SPEED',
			(b'ESTIMATED CRUISE SPEED', b'Feet per second'),
			_dec='Estimated cruise speed'
		)
		self.Miscellaneous.add(
			'CG_PERCENT',
			(b'CG PERCENT', b'Percent over 100'),
			_dec='Longitudinal CG position as a percent of reference chord'
		)
		self.Miscellaneous.add(
			'CG_PERCENT_LATERAL',
			(b'CG PERCENT LATERAL', b'Percent over 100'),
			_dec='Lateral CG position as a percent of reference chord'
		)
		self.Miscellaneous.add(
			'IS_SLEW_ACTIVE',
			(b'IS SLEW ACTIVE', b'Bool'),
			_dec='True if slew is active'
		)
		self.Miscellaneous.add(
			'IS_SLEW_ALLOWED',
			(b'IS SLEW ALLOWED', b'Bool'),
			_dec='True if slew is enabled'
		)
		self.Miscellaneous.add(
			'ATC_SUGGESTED_MIN_RWY_TAKEOFF',
			(b'ATC SUGGESTED MIN RWY TAKEOFF', b'Feet'),
			_dec='Suggested minimum runway length for takeoff. Used by ATC '
		)
		self.Miscellaneous.add(
			'ATC_SUGGESTED_MIN_RWY_LANDING',
			(b'ATC SUGGESTED MIN RWY LANDING', b'Feet'),
			_dec='Suggested minimum runway length for landing. Used by ATC '
		)
		self.Miscellaneous.add(
			'PAYLOAD_STATION_WEIGHT:index',
			(b'PAYLOAD STATION WEIGHT:index', b'Pounds'),
			_dec='Individual payload station weight'
		)
		self.Miscellaneous.add(
			'PAYLOAD_STATION_COUNT',
			(b'PAYLOAD STATION COUNT', b'Number'),
			_dec='Number of payload stations'
		)
		self.Miscellaneous.add(
			'USER_INPUT_ENABLED',
			(b'USER INPUT ENABLED', b'Bool'),
			_dec='Is input allowed from the user'
		)
		self.Miscellaneous.add(
			'TYPICAL_DESCENT_RATE',
			(b'TYPICAL DESCENT RATE', b'Feet per minute'),
			_dec='Normal descent rate'
		)
		self.Miscellaneous.add(
			'VISUAL_MODEL_RADIUS',
			(b'VISUAL MODEL RADIUS', b'Meters'),
			_dec='Model radius'
		)
		self.Miscellaneous.add(
			'SIGMA_SQRT',
			(b'SIGMA SQRT', b'Number'),
			_dec='Sigma sqrt'
		)
		self.Miscellaneous.add(
			'DYNAMIC_PRESSURE',
			(b'DYNAMIC PRESSURE', b'Pounds per square foot'),
			_dec='Dynamic pressure'
		)
		self.Miscellaneous.add(
			'TOTAL_VELOCITY',
			(b'TOTAL VELOCITY', b'Feet per second'),
			_dec='Velocity regardless of direction. For example, if a helicopter is ascending vertically at 100 fps, getting this variable will return 100.'
		)
		self.Miscellaneous.add(
			'AIRSPEED_SELECT_INDICATED_OR_TRUE',
			(b'AIRSPEED SELECT INDICATED OR TRUE', b'Knots'),
			_dec='The airspeed, whether true or indicated airspeed has been selected.'
		)
		self.Miscellaneous.add(
			'VARIOMETER_RATE',
			(b'VARIOMETER RATE', b'Feet per second'),
			_dec='Variometer rate'
		)
		self.Miscellaneous.add(
			'VARIOMETER_SWITCH',
			(b'VARIOMETER SWITCH', b'Bool'),
			_dec='True if the variometer switch is on'
		)
		self.Miscellaneous.add(
			'PRESSURE_ALTITUDE',
			(b'PRESSURE ALTITUDE', b'Meters'),
			_dec='Altitude reading'
		)
		self.Miscellaneous.add(
			'MAGNETIC_COMPASS',
			(b'MAGNETIC COMPASS', b'Degrees'),
			_dec='Compass reading'
		)
		self.Miscellaneous.add(
			'TURN_INDICATOR_RATE',
			(b'TURN INDICATOR RATE', b'Radians per second'),
			_dec='Turn indicator reading'
		)
		self.Miscellaneous.add(
			'TURN_INDICATOR_SWITCH',
			(b'TURN INDICATOR SWITCH', b'Bool'),
			_dec='True if turn indicator switch is on'
		)
		self.Miscellaneous.add(
			'YOKE_Y_INDICATOR',
			(b'YOKE Y INDICATOR', b'Position'),
			_dec='Yoke position in vertical direction'
		)
		self.Miscellaneous.add(
			'YOKE_X_INDICATOR',
			(b'YOKE X INDICATOR', b'Position'),
			_dec='Yoke position in horizontal direction'
		)
		self.Miscellaneous.add(
			'RUDDER_PEDAL_INDICATOR',
			(b'RUDDER PEDAL INDICATOR', b'Position'),
			_dec='Rudder pedal position'
		)
		self.Miscellaneous.add(
			'BRAKE_DEPENDENT_HYDRAULIC_PRESSURE',
			(b'BRAKE DEPENDENT HYDRAULIC PRESSURE', b'Pounds per square foot'),
			_dec='Brake dependent hydraulic pressure reading'
		)
		self.Miscellaneous.add(
			'PANEL_ANTI_ICE_SWITCH',
			(b'PANEL ANTI ICE SWITCH', b'Bool'),
			_dec='True if panel anti-ice switch is on'
		)
		self.Miscellaneous.add(
			'WING_AREA',
			(b'WING AREA', b'Square feet'),
			_dec='Total wing area'
		)
		self.Miscellaneous.add(
			'WING_SPAN',
			(b'WING SPAN', b'Feet'),
			_dec='Total wing span'
		)
		self.Miscellaneous.add(
			'BETA_DOT',
			(b'BETA DOT', b'Radians per second'),
			_dec='Beta dot'
		)
		self.Miscellaneous.add(
			'LINEAR_CL_ALPHA',
			(b'LINEAR CL ALPHA', b'Per radian'),
			_dec='Linear CL alpha'
		)
		self.Miscellaneous.add(
			'STALL_ALPHA',
			(b'STALL ALPHA', b'Radians'),
			_dec='Stall alpha'
		)
		self.Miscellaneous.add(
			'ZERO_LIFT_ALPHA',
			(b'ZERO LIFT ALPHA', b'Radians'),
			_dec='Zero lift alpha'
		)
		self.Miscellaneous.add(
			'CG_AFT_LIMIT',
			(b'CG AFT LIMIT', b'Percent over 100'),
			_dec='Aft limit of CG'
		)
		self.Miscellaneous.add(
			'CG_FWD_LIMIT',
			(b'CG FWD LIMIT', b'Percent over 100'),
			_dec='Forward limit of CG'
		)
		self.Miscellaneous.add(
			'CG_MAX_MACH',
			(b'CG MAX MACH', b'Machs'),
			_dec='Max mach CG'
		)
		self.Miscellaneous.add(
			'CG_MIN_MACH',
			(b'CG MIN MACH', b'Machs'),
			_dec='Min mach CG'
		)
		self.Miscellaneous.add(
			'PAYLOAD_STATION_NAME',
			(b'PAYLOAD STATION NAME', b'String'),
			_dec='Descriptive name for payload station'
		)
		self.Miscellaneous.add(
			'ELEVON_DEFLECTION',
			(b'ELEVON DEFLECTION', b'Radians'),
			_dec='Elevon deflection'
		)
		self.Miscellaneous.add(
			'EXIT_POSX',
			(b'EXIT POSX', b'Feet'),
			_dec='Position of exit relative to datum reference point'
		)
		self.Miscellaneous.add(
			'EXIT_POSY',
			(b'EXIT POSY', b'Feet'),
			_dec='Position of exit relative to datum reference point'
		)
		self.Miscellaneous.add(
			'EXIT_POSZ',
			(b'EXIT POSZ', b'Feet'),
			_dec='Position of exit relative to datum reference point'
		)
		self.Miscellaneous.add(
			'DECISION_HEIGHT',
			(b'DECISION HEIGHT', b'Feet'),
			_dec='Design decision height'
		)
		self.Miscellaneous.add(
			'DECISION_ALTITUDE_MSL',
			(b'DECISION ALTITUDE MSL', b'Feet'),
			_dec='Design decision altitude above mean sea level'
		)
		self.Miscellaneous.add(
			'EMPTY_WEIGHT_PITCH_MOI',
			(b'EMPTY WEIGHT PITCH MOI', b'Slugs per feet squared'),
			_dec='Empty weight pitch moment of inertia'
		)
		self.Miscellaneous.add(
			'EMPTY_WEIGHT_ROLL_MOI',
			(b'EMPTY WEIGHT ROLL MOI', b'Slugs per feet squared'),
			_dec='Empty weight roll moment of inertia'
		)
		self.Miscellaneous.add(
			'EMPTY_WEIGHT_YAW_MOI',
			(b'EMPTY WEIGHT YAW MOI', b'Slugs per feet squared'),
			_dec='Empty weight yaw moment of inertia'
		)
		self.Miscellaneous.add(
			'EMPTY_WEIGHT_CROSS_COUPLED_MOI',
			(b'EMPTY WEIGHT CROSS COUPLED MOI', b'Slugs per feet squared'),
			_dec='Empty weigth cross coupled moment of inertia'
		)
		self.Miscellaneous.add(
			'TOTAL_WEIGHT_PITCH_MOI',
			(b'TOTAL WEIGHT PITCH MOI', b'Slugs per feet squared'),
			_dec='Total weight pitch moment of inertia'
		)
		self.Miscellaneous.add(
			'TOTAL_WEIGHT_ROLL_MOI',
			(b'TOTAL WEIGHT ROLL MOI', b'Slugs per feet squared'),
			_dec='Total weight roll moment of inertia'
		)
		self.Miscellaneous.add(
			'TOTAL_WEIGHT_YAW_MOI',
			(b'TOTAL WEIGHT YAW MOI', b'Slugs per feet squared'),
			_dec='Total weight yaw moment of inertia'
		)
		self.Miscellaneous.add(
			'TOTAL_WEIGHT_CROSS_COUPLED_MOI',
			(b'TOTAL WEIGHT CROSS COUPLED MOI', b'Slugs per feet squared'),
			_dec='Total weight cross coupled moment of inertia'
		)
		self.Miscellaneous.add(
			'WATER_BALLAST_VALVE',
			(b'WATER BALLAST VALVE', b'Bool'),
			_dec='True if water ballast valve is available'
		)
		self.Miscellaneous.add(
			'MAX_RATED_ENGINE_RPM',
			(b'MAX RATED ENGINE RPM', b'Rpm'),
			_dec='Maximum rated rpm'
		)
		self.Miscellaneous.add(
			'FULL_THROTTLE_THRUST_TO_WEIGHT_RATIO',
			(b'FULL THROTTLE THRUST TO WEIGHT RATIO', b'Number'),
			_dec='Full throttle thrust to weight ratio'
		)
		self.Miscellaneous.add(
			'PROP_AUTO_CRUISE_ACTIVE',
			(b'PROP AUTO CRUISE ACTIVE', b'Bool'),
			_dec='True if prop auto cruise active'
		)
		self.Miscellaneous.add(
			'PROP_ROTATION_ANGLE',
			(b'PROP ROTATION ANGLE', b'Radians'),
			_dec='Prop rotation angle'
		)
		self.Miscellaneous.add(
			'PROP_BETA_MAX',
			(b'PROP BETA MAX', b'Radians'),
			_dec='Prop beta max'
		)
		self.Miscellaneous.add(
			'PROP_BETA_MIN',
			(b'PROP BETA MIN', b'Radians'),
			_dec='Prop beta min'
		)
		self.Miscellaneous.add(
			'PROP_BETA_MIN_REVERSE',
			(b'PROP BETA MIN REVERSE', b'Radians'),
			_dec='Prop beta min reverse'
		)
		self.Miscellaneous.add(
			'ELECTRICAL_OLD_CHARGING_AMPS',
			(b'ELECTRICAL OLD CHARGING AMPS', b'Amps'),
			_dec='Legacy, use ELECTRICAL BATTERY LOAD'
		)
		self.Miscellaneous.add(
			'HYDRAULIC_SWITCH',
			(b'HYDRAULIC SWITCH', b'Bool'),
			_dec='True if hydraulic switch is on'
		)
		self.Miscellaneous.add(
			'CONCORDE_VISOR_POSITION_PERCENT',
			(b'CONCORDE VISOR POSITION PERCENT', b'Percent over 100'),
			_dec='0 = up, 1.0 = extended/down'
		)
		self.Miscellaneous.add(
			'CONCORDE_NOSE_ANGLE',
			(b'CONCORDE NOSE ANGLE', b'Radians'),
			_dec='0 = up'
		)
		self.Miscellaneous.add(
			'REALISM_CRASH_WITH_OTHERS',
			(b'REALISM CRASH WITH OTHERS', b'Bool'),
			_dec='True indicates crashing with other aircraft is possible.'
		)
		self.Miscellaneous.add(
			'REALISM_CRASH_DETECTION',
			(b'REALISM CRASH DETECTION', b'Bool'),
			_dec='True indicates crash detection is turned on.'
		)
		self.Miscellaneous.add(
			'MANUAL_INSTRUMENT_LIGHTS',
			(b'MANUAL INSTRUMENT LIGHTS', b'Bool'),
			_dec='True if instrument lights are set manually'
		)
		self.Miscellaneous.add(
			'PITOT_ICE_PCT',
			(b'PITOT ICE PCT', b'Percent over 100'),
			_dec='Amount of pitot ice. 100 is fully iced.'
		)
		self.Miscellaneous.add(
			'SEMIBODY_LOADFACTOR_Y',
			(b'SEMIBODY LOADFACTOR Y', b'Number'),
			_dec='Semibody loadfactor x and z are not supported.'
		)
		self.Miscellaneous.add(
			'SEMIBODY_LOADFACTOR_YDOT',
			(b'SEMIBODY LOADFACTOR YDOT', b'Per second'),
			_dec='Semibody loadfactory ydot'
		)
		self.Miscellaneous.add(
			'RAD_INS_SWITCH',
			(b'RAD INS SWITCH', b'Bool'),
			_dec='True if Rad INS switch on'
		)
		self.Miscellaneous.add(
			'SIMULATED_RADIUS',
			(b'SIMULATED RADIUS', b'Feet'),
			_dec='Simulated radius'
		)
		self.Miscellaneous.add(
			'STRUCTURAL_ICE_PCT',
			(b'STRUCTURAL ICE PCT', b'Percent over 100'),
			_dec='Amount of ice on aircraft structure. 100 is fully iced.'
		)
		self.Miscellaneous.add(
			'ARTIFICIAL_GROUND_ELEVATION',
			(b'ARTIFICIAL GROUND ELEVATION', b'Feet'),
			_dec='In case scenery is not loaded for AI planes, this variable can be used to set a default surface elevation.'
		)
		self.Miscellaneous.add(
			'SURFACE_INFO_VALID',
			(b'SURFACE INFO VALID', b'Bool'),
			_dec='True indicates SURFACE CONDITION is meaningful.'
		)
		self.Miscellaneous.add(
			'PUSHBACK_ANGLE',
			(b'PUSHBACK ANGLE', b'Radians'),
			_dec='Pushback angle (the heading of the tug)'
		)
		self.Miscellaneous.add(
			'PUSHBACK_CONTACTX',
			(b'PUSHBACK CONTACTX', b'Feet'),
			_dec='The towpoint position, relative to the aircrafts datum reference point.'
		)
		self.Miscellaneous.add(
			'PUSHBACK_CONTACTY',
			(b'PUSHBACK CONTACTY', b'Feet'),
			_dec='Pushback contact position in vertical direction'
		)
		self.Miscellaneous.add(
			'PUSHBACK_CONTACTZ',
			(b'PUSHBACK CONTACTZ', b'Feet'),
			_dec='Pushback contact position in fore/aft direction'
		)
		self.Miscellaneous.add(
			'PUSHBACK_WAIT',
			(b'PUSHBACK WAIT', b'Bool'),
			_dec='True if waiting for pushback.'
		)
		self.Miscellaneous.add(
			'YAW_STRING_ANGLE',
			(b'YAW STRING ANGLE', b'Radians'),
			_dec='The yaw string angle. Yaw strings are attached to gliders as visible indicators of the yaw angle. An animation of this is not implemented in ESP.'
		)
		self.Miscellaneous.add(
			'YAW_STRING_PCT_EXTENDED',
			(b'YAW STRING PCT EXTENDED', b'Percent over 100'),
			_dec='Yaw string angle as a percentage'
		)
		self.Miscellaneous.add(
			'INDUCTOR_COMPASS_PERCENT_DEVIATION',
			(b'INDUCTOR COMPASS PERCENT DEVIATION', b'Percent over 100'),
			_dec='Inductor compass deviation reading'
		)
		self.Miscellaneous.add(
			'INDUCTOR_COMPASS_HEADING_REF',
			(b'INDUCTOR COMPASS HEADING REF', b'Radians'),
			_dec='Inductor compass heading'
		)
		self.Miscellaneous.add(
			'ANEMOMETER_PCT_RPM',
			(b'ANEMOMETER PCT RPM', b'Percent over 100'),
			_dec='Anemometer rpm as a percentage'
		)
		self.Miscellaneous.add(
			'ROTOR_ROTATION_ANGLE',
			(b'ROTOR ROTATION ANGLE', b'Radians'),
			_dec='Main rotor rotation angle (helicopters only)'
		)
		self.Miscellaneous.add(
			'DISK_PITCH_ANGLE',
			(b'DISK PITCH ANGLE', b'Radians'),
			_dec='Main rotor pitch angle (helicopters only)'
		)
		self.Miscellaneous.add(
			'DISK_BANK_ANGLE',
			(b'DISK BANK ANGLE', b'Radians'),
			_dec='Main rotor bank angle (helicopters only)'
		)
		self.Miscellaneous.add(
			'DISK_PITCH_PCT',
			(b'DISK PITCH PCT', b'Percent over 100'),
			_dec='Main rotor pitch percent (helicopters only)'
		)
		self.Miscellaneous.add(
			'DISK_BANK_PCT',
			(b'DISK BANK PCT', b'Percent over 100'),
			_dec='Main rotor bank percent (helicopters only)'
		)
		self.Miscellaneous.add(
			'DISK_CONING_PCT',
			(b'DISK CONING PCT', b'Percent over 100'),
			_dec='Main rotor coning percent (helicopters only)'
		)
		self.Miscellaneous.add(
			'NAV_VOR_LLAF64',
			(b'NAV VOR LLAF64', b'LLA structure'),
			_dec='Nav VOR latitude, longitude, altitude'
		)
		self.Miscellaneous.add(
			'NAV_GS_LLAF64',
			(b'NAV GS LLAF64', b'LLA structure'),
			_dec='Nav GS latitude, longitude, altitude'
		)
		self.Miscellaneous.add(
			'STATIC_CG_TO_GROUND',
			(b'STATIC CG TO GROUND', b'Feet'),
			_dec='Static CG to ground'
		)
		self.Miscellaneous.add(
			'STATIC_PITCH',
			(b'STATIC PITCH', b'Radians'),
			_dec='Static pitch'
		)
		self.Miscellaneous.add(
			'TOW_RELEASE_HANDLE',
			(b'TOW RELEASE HANDLE', b'Percent over 100'),
			_dec='Position of tow release handle. 100 is fully deployed.'
		)
		self.Miscellaneous.add(
			'TOW_CONNECTION',
			(b'TOW CONNECTION', b'Bool'),
			_dec='True if a towline is connected to both tow plane and glider.'
		)
		self.Miscellaneous.add(
			'APU_PCT_RPM',
			(b'APU PCT RPM', b'Percent over 100'),
			_dec='Auxiliary power unit rpm, as a percentage'
		)
		self.Miscellaneous.add(
			'APU_PCT_STARTER',
			(b'APU PCT STARTER', b'Percent over 100'),
			_dec='Auxiliary power unit starter, as a percentage'
		)
		self.Miscellaneous.add(
			'APU_VOLTS',
			(b'APU VOLTS', b'Volts'),
			_dec='Auxiliary power unit voltage'
		)
		self.Miscellaneous.add(
			'APU_GENERATOR_SWITCH',
			(b'APU GENERATOR SWITCH', b'Bool'),
			_dec='True if APU generator switch on'
		)
		self.Miscellaneous.add(
			'APU_GENERATOR_ACTIVE',
			(b'APU GENERATOR ACTIVE', b'Bool'),
			_dec='True if APU generator active'
		)
		self.Miscellaneous.add(
			'APU_ON_FIRE_DETECTED',
			(b'APU ON FIRE DETECTED', b'Bool'),
			_dec='True if APU on fire'
		)
		self.Miscellaneous.add(
			'PRESSURIZATION_CABIN_ALTITUDE',
			(b'PRESSURIZATION CABIN ALTITUDE', b'Feet'),
			_dec='The current altitude of the cabin pressurization..'
		)
		self.Miscellaneous.add(
			'PRESSURIZATION_CABIN_ALTITUDE_GOAL',
			(b'PRESSURIZATION CABIN ALTITUDE GOAL', b'Feet'),
			_dec='The set altitude of the cabin pressurization.'
		)
		self.Miscellaneous.add(
			'PRESSURIZATION_CABIN_ALTITUDE_RATE',
			(b'PRESSURIZATION CABIN ALTITUDE RATE', b'Feet per second'),
			_dec='The rate at which cabin pressurization changes.'
		)
		self.Miscellaneous.add(
			'PRESSURIZATION_PRESSURE_DIFFERENTIAL',
			(b'PRESSURIZATION PRESSURE DIFFERENTIAL', b'Pounds per square foot'),
			_dec='The difference in pressure between the set altitude pressurization and the current pressurization.'
		)
		self.Miscellaneous.add(
			'PRESSURIZATION_DUMP_SWITCH',
			(b'PRESSURIZATION DUMP SWITCH', b'Bool'),
			_dec='True if the cabin pressurization dump switch is on.'
		)
		self.Miscellaneous.add(
			'FIRE_BOTTLE_SWITCH',
			(b'FIRE BOTTLE SWITCH', b'Bool'),
			_dec='True if the fire bottle switch is on.'
		)
		self.Miscellaneous.add(
			'FIRE_BOTTLE_DISCHARGED',
			(b'FIRE BOTTLE DISCHARGED', b'Bool'),
			_dec='True if the fire bottle is discharged.'
		)
		self.Miscellaneous.add(
			'CABIN_NO_SMOKING_ALERT_SWITCH',
			(b'CABIN NO SMOKING ALERT SWITCH', b'Bool'),
			_dec='True if the No Smoking switch is on.'
		)
		self.Miscellaneous.add(
			'CABIN_SEATBELTS_ALERT_SWITCH',
			(b'CABIN SEATBELTS ALERT SWITCH', b'Bool'),
			_dec='True if the Seatbelts switch is on.'
		)
		self.Miscellaneous.add(
			'GPWS_WARNING',
			(b'GPWS WARNING', b'Bool'),
			_dec='True if Ground Proximity Warning System installed.'
		)
		self.Miscellaneous.add(
			'GPWS_SYSTEM_ACTIVE',
			(b'GPWS SYSTEM ACTIVE', b'Bool'),
			_dec='True if the Ground Proximity Warning System is active'
		)
		self.Miscellaneous.add(
			'IS_LATITUDE_LONGITUDE_FREEZE_ON',
			(b'IS LATITUDE LONGITUDE FREEZE ON', b'Bool'),
			_dec='True if the lat/lon of the aircraft '
		)
		self.Miscellaneous.add(
			'IS_ALTITUDE_FREEZE_ON',
			(b'IS ALTITUDE FREEZE ON', b'Bool'),
			_dec='True if the altitude of the aircraft is frozen.'
		)
		self.Miscellaneous.add(
			'IS_ATTITUDE_FREEZE_ON',
			(b'IS ATTITUDE FREEZE ON', b'Bool'),
			_dec='True if the attitude (pitch, bank and heading) of the aircraft is frozen.'
		)

		self.String = sm.new_request_holder()
		self.String.add(
			'ATC_TYPE',
			(b'ATC TYPE', b'String (30)'),
			_dec='Type used by ATC'
		)
		self.String.add(
			'ATC_MODEL',
			(b'ATC MODEL', b'String (10)'),
			_dec='Model used by ATC'
		)
		self.String.add(
			'ATC_ID',
			(b'ATC ID', b'String (10)'),
			_dec='ID used by ATC'
		)
		self.String.add(
			'ATC_AIRLINE',
			(b'ATC AIRLINE', b'String (50)'),
			_dec='Airline used by ATC'
		)
		self.String.add(
			'ATC_FLIGHT_NUMBER',
			(b'ATC FLIGHT NUMBER', b'String (6)'),
			_dec='Flight Number used by ATC'
		)
		self.String.add(
			'TITLE',
			(b'TITLE', b'Variable length string'),
			_dec='Title from aircraft.cfg'
		)
		self.String.add(
			'HSI_STATION_IDENT',
			(b'HSI STATION IDENT', b'String(6)'),
			_dec='Tuned station identifier'
		)
		self.String.add(
			'GPS_WP_PREV_ID',
			(b'GPS WP_PREV ID', b'String'),
			_dec='ID of previous GPS waypoint'
		)
		self.String.add(
			'GPS_WP_NEXT_ID',
			(b'GPS WP_NEXT ID', b'String'),
			_dec='ID of next GPS waypoint'
		)
		self.String.add(
			'GPS_APPROACH_AIRPORT_ID',
			(b'GPS APPROACH AIRPORT ID', b'String'),
			_dec='ID of airport'
		)
		self.String.add(
			'GPS_APPROACH_APPROACH_ID',
			(b'GPS APPROACH APPROACH ID', b'String'),
			_dec='ID of approach'
		)
		self.String.add(
			'GPS_APPROACH_TRANSITION_ID',
			(b'GPS APPROACH TRANSITION ID', b'String'),
			_dec='ID of approach transition'
		)
