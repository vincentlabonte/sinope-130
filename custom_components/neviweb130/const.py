"""Constants for neviweb130 component."""

DOMAIN = "neviweb130"
CONF_NETWORK = 'network'
CONF_NETWORK2 = 'network2'
CONF_HOMEKIT_MODE = 'homekit_mode'
CONF_STAT_INTERVAL = 'stat_interval'

ATTR_ALERT = "alert"
ATTR_SIGNATURE = "signature"
ATTR_POWER_MODE = "powerMode"
ATTR_MODE = "mode"
ATTR_ONOFF = "onOff"
ATTR_ONOFF2 = "onOff2"
ATTR_INTENSITY = "intensity"
ATTR_INTENSITY_MIN = "intensityMin"
ATTR_WATTAGE = "loadConnected"
ATTR_WATTAGE_INSTANT = "wattageInstant"
ATTR_WATTAGE_OVERRIDE = "wattageOverride"
ATTR_SETPOINT_MODE = "setpointMode"
ATTR_ROOM_SETPOINT = "roomSetpoint"
ATTR_ROOM_SETPOINT_AWAY = "roomSetpointAway"
ATTR_ROOM_TEMPERATURE = "roomTemperature"
ATTR_OUTPUT_PERCENT_DISPLAY = "outputPercentDisplay"
ATTR_ROOM_SETPOINT_MIN = "roomSetpointMin"
ATTR_ROOM_SETPOINT_MAX = "roomSetpointMax"
ATTR_GFCI_STATUS = "gfciStatus"
ATTR_GFCI_ALERT = "alertGfci"
ATTR_WATER_LEAK_STATUS = "waterLeakStatus"
ATTR_WATER_LEAK_ALARM_STATUS = "waterleakDetectionAlarmStatus"
ATTR_WATER_LEAK_DISCONECTED_STATUS = "waterleakDisconnectedAlarmStatus"
ATTR_POWER_SUPPLY = "backupPowerSupply"
ATTR_BATTERY_VOLTAGE = "batteryVoltage"
ATTR_BATTERY_STATUS = "batteryStatus"
ATTR_BATTERY_TYPE = "batteryType"
ATTR_FLOOR_MODE = "airFloorMode"
ATTR_FLOOR_OUTPUT2 = "loadWattOutput2" #status on/off, value=xx
ATTR_FLOOR_AUX = "auxHeatConfig"
ATTR_KEYPAD = "lockKeypad"
ATTR_OCCUPANCY = "occupancyMode"
ATTR_FLOOR_OUTPUT1 = "loadWattOutput1" #status on/off, value=xx
ATTR_LIGHT_WATTAGE = "loadWattOutput1" #status on/off, value=xx
ATTR_WIFI_WATTAGE = "loadWatt"
ATTR_WIFI_WATT_NOW = "loadWattNow"
ATTR_WIFI = "wifiRssi"
ATTR_RSSI = "rssi"
ATTR_DISPLAY2 = "config2ndDisplay"
ATTR_WIFI_KEYPAD = "keyboardLock"
ATTR_TIMER = "powerTimer"
ATTR_TIMER2 = "powerTimer2"
ATTR_DRSTATUS = "drStatus"
ATTR_BACKLIGHT = "backlightAdaptive"
ATTR_BACKLIGHT_AUTO_DIM = "backlightAutoDim"
ATTR_LED_ON_INTENSITY = "statusLedOnIntensity"
ATTR_LED_OFF_INTENSITY = "statusLedOffIntensity"
ATTR_LED_ON_COLOR = "statusLedOnColor"
ATTR_LED_OFF_COLOR = "statusLedOffColor"
ATTR_STATE = "state"
ATTR_RED = "red"
ATTR_GREEN = "green"
ATTR_BLUE = "blue"
ATTR_TIME = "timeFormat"
ATTR_TEMP = "temperatureFormat"
ATTR_MOTOR_POS = "motorPosition"
ATTR_TEMP_ALARM = "temperatureAlarmStatus"
ATTR_TEMPERATURE = "temperature"
ATTR_WATER_TEMPERATURE = "waterTemperature"
ATTR_ROOM_TEMP_ALARM = "roomTemperatureAlarmStatus"
ATTR_VALVE_CLOSURE = "valveClosureSource" #source
ATTR_LEAK_ALERT = "alertWaterLeak"
ATTR_BATT_ALERT = "alertLowBatt"
ATTR_TEMP_ALERT = "alertLowTemp"
ATTR_FUEL_ALERT = "alertLowFuel"
ATTR_FUEL_PERCENT_ALERT = "alertLowFuelPercent"
ATTR_CONF_CLOSURE = "cfgValveClosure"
ATTR_MOTOR_TARGET = "motorTargetPosition"
ATTR_FLOOR_AIR_LIMIT = "floorMaxAirTemperature"
ATTR_FLOOR_MAX = "floorLimitHigh"
ATTR_FLOOR_MIN = "floorLimitLow"
ATTR_ROOM_TEMP_DISPLAY = "roomTemperatureDisplay"
ATTR_EARLY_START = "earlyStartCfg"
ATTR_FLOOR_SENSOR = "floorSensorType"
ATTR_AUX_CYCLE = "auxCycleLength"
ATTR_CYCLE = "cycleLength"
ATTR_CYCLE_OUTPUT2= "cycleLengthOutput2" #status on/off, value (second)
ATTR_PUMP_PROTEC = "pumpProtection" #status on/off, duration, frequency
ATTR_PUMP_PROTEC_DURATION = "pumpProtectDuration" #status on/off, value
ATTR_PUMP_PROTEC_PERIOD = "pumpProtectPeriod" #status on/off, value
ATTR_TYPE = "type"
ATTR_PHASE_CONTROL = "phaseControl"
ATTR_SYSTEM_MODE = "systemMode"
ATTR_DRSETPOINT = "drSetpoint"
ATTR_DRACTIVE = "drActive"
ATTR_OPTOUT = "optOut"
ATTR_SETPOINT = "setpoint"
ATTR_INPUT_STATUS = "inputStatus"
ATTR_INPUT2_STATUS = "input2Status"
ATTR_EXT_TEMP = "externalTemperature"
ATTR_REL_HUMIDITY = "relativeHumidity"
ATTR_STATUS = "status"
ATTR_ERROR_CODE_SET1 = "errorCodeSet1"
ATTR_FLOW_METER_CONFIG = "flowMeterMeasurementConfig"
ATTR_VALVE_INFO = "valveInfo"
ATTR_STM8_ERROR = "stm8Error"
ATTR_TANK_SIZE = "tankSize"
ATTR_CONTROLLED_DEVICE = "controlledDevice"
ATTR_COLD_LOAD_PICKUP_STATUS = "coldLoadPickupStatus"
ATTR_KEY_DOUBLE_UP = "configKeyDoubleUp"
ATTR_ANGLE = "angle"
ATTR_SAMPLING = "samplingTime"
ATTR_TANK_TYPE = "tankType"
ATTR_TANK_HEIGHT = "tankHeight"
ATTR_TANK_PERCENT = "tankPercent"
ATTR_GAUGE_TYPE = "gaugeType"
ATTR_COOL_SETPOINT = "coolSetpoint"
ATTR_COOL_SETPOINT_MIN = "coolSetpointMin"
ATTR_COOL_SETPOINT_MAX = "coolSetpointMax"
ATTR_WATER_TEMP_MIN = "drConfigWaterTempMin"
ATTR_MIN_WATER_TEMP = "minWaterTankTemperature"
ATTR_WATT_TIME_ON = "drWTTimeOn"
ATTR_DR_WATER_TEMP_TIME = "drConfigWaterTempTime"
ATTR_WATER_TEMP_TIME = "waterTempTime"
ATTR_FLOW_ALARM1 = "flowMeterAlarm1Config"
ATTR_FLOW_ALARM2 = "flowMeterAlarm2Config"
ATTR_AWAY_ACTION = "awayAction"
ATTR_FLOW_ENABLED = "flowMeterEnabled"
ATTR_FLOW_MODEL_CONFIG = "FlowModel"
ATTR_FLOW_ALARM_TIMER = "flowMeterAlarmDisableTimer"
ATTR_FLOW_THRESHOLD = "alarm1FlowThreshold"
ATTR_FLOW_ALARM1_LENGHT = "alarm1Length"
ATTR_FLOW_ALARM1_PERIOD = "alarm1Period"
ATTR_FLOW_ALARM1_OPTION = "alarm1Options"
ATTR_DR_PROTEC_STATUS = "drProtectionLegStatus"
ATTR_LEG_PROTEC_STATUS = "legProtectionStatus"
ATTR_COLD_LOAD_PICKUP_REMAIN_TIME = "coldLoadPickupRemainingTime"
ATTR_COLD_LOAD_PICKUP_TEMP = "coldLoadPickupTemperature"
ATTR_TEMP_ACTION_LOW = "temperatureActionLow"
ATTR_BATT_ACTION_LOW = "batteryActionLow"
ATTR_NAME_1 = "input1name"
ATTR_NAME_2 = "input2name"
ATTR_OUTPUT_NAME_1 = "output1name"
ATTR_OUTPUT_NAME_2 = "output2name"
ATTR_WATER_TANK_ON = "waterTankTimeOn"
ATTR_HEAT_LOCK_TEMP = "heatLockoutTemperature"
ATTR_COOL_LOCK_TEMP = "coolLockoutTemperature"
ATTR_AVAIL_MODE = "availableMode"
ATTR_FAN_SPEED = "fanSpeed"
ATTR_FAN_CAP = "fanCapabilities"
ATTR_FAN_SWING_VERT = "fanSwingVertical"
ATTR_FAN_SWING_HORIZ = "fanSwingHorizontal"
ATTR_FAN_SWING_CAP = "fanSwingCapabilities"
ATTR_FAN_SWING_CAP_HORIZ = "fanSwingCapabilityHorizontal"
ATTR_FAN_SWING_CAP_VERT = "fanSwingCapabilityVertical"
ATTR_DISPLAY_CONF = "displayConfig"
ATTR_DISPLAY_CAP = "displayCapability"
ATTR_MODEL = "model"
ATTR_SOUND_CONF = "soundConfig"
ATTR_SOUND_CAP = "soundCapability"
ATTR_LANGUAGE = "language"
ATTR_MODE = "mode"
ATTR_HC_DEV = "hcDevice"
ATTR_BALANCE_PT = "balancePoint"
ATTR_BATT_PERCENT_NORMAL = "batteryPercentNormalized"
ATTR_BATT_STATUS_NORMAL = "batteryStatusNormalized"
ATTR_BATT_INFO = "displayBatteryInfo"
ATTR_INPUT_1_ON_DELAY = "inputOnDebounceDelay"
ATTR_INPUT_2_ON_DELAY = "inputOnDebounceDelay2"
ATTR_INPUT_1_OFF_DELAY = "inputOffDebounceDelay"
ATTR_INPUT_2_OFF_DELAY = "inputOffDebounceDelay2"
ATTR_VALUE = "value"
ATTR_ACTIVE = "active"
ATTR_ONOFF_NUM = "onOff_num"
ATTR_CLOSE_VALVE = "closeValve"
ATTR_TRIGGER_ALARM = "triggerAlarm"
ATTR_DELAY = "delay"
ATTR_INPUT_NUMBER = "input_number"
ATTR_COLD_LOAD_PICKUP = "coldLoadPickup"
ATTR_HEAT_LOCKOUT_TEMP = "heatLockoutTemp"

MODE_AUTO = "auto"
MODE_AUTO_BYPASS = "autoBypass"
MODE_MANUAL = "manual"
MODE_AWAY = "away"
MODE_HOME = "home"
MODE_OFF = "off"

STATE_WATER_LEAK = "water"
STATE_VALVE_STATUS = "open"
STATE_KEYPAD_STATUS = "unlocked"

SERVICE_SET_LED_INDICATOR = "set_led_indicator"
SERVICE_SET_CLIMATE_KEYPAD_LOCK = "set_climate_keypad_lock"
SERVICE_SET_LIGHT_KEYPAD_LOCK = "set_light_keypad_lock"
SERVICE_SET_SWITCH_KEYPAD_LOCK = "set_switch_keypad_lock"
SERVICE_SET_LIGHT_TIMER = "set_light_timer"
SERVICE_SET_SWITCH_TIMER = "set_switch_timer"
SERVICE_SET_SWITCH_TIMER_2 = "set_switch_timer2"
SERVICE_SET_SECOND_DISPLAY = "set_second_display"
SERVICE_SET_BACKLIGHT = "set_backlight"
SERVICE_SET_EARLY_START = "set_early_start"
SERVICE_SET_TIME_FORMAT = "set_time_format"
SERVICE_SET_TEMPERATURE_FORMAT = "set_temperature_format"
SERVICE_SET_WATTAGE = "set_wattage"
SERVICE_SET_SETPOINT_MAX = "set_setpoint_max"
SERVICE_SET_SETPOINT_MIN = "set_setpoint_min"
SERVICE_SET_SENSOR_ALERT = "set_sensor_alert"
SERVICE_SET_VALVE_ALERT = "set_valve_alert"
SERVICE_SET_VALVE_TEMP_ALERT = "set_valve_temp_alert"
SERVICE_SET_FLOOR_AIR_LIMIT = "set_floor_air_limit"
SERVICE_SET_AIR_FLOOR_MODE = "set_air_floor_mode"
SERVICE_SET_PHASE_CONTROL = "set_phase_control"
SERVICE_SET_HVAC_DR_OPTIONS = "set_hvac_dr_options"
SERVICE_SET_HVAC_DR_SETPOINT = "set_hvac_dr_setpoint"
SERVICE_SET_LOAD_DR_OPTIONS = "set_load_dr_options"
SERVICE_SET_CONTROL_ONOFF = "set_control_onoff"
SERVICE_SET_AUXILIARY_LOAD = "set_auxiliary_load"
SERVICE_SET_AUX_CYCLE_OUTPUT = "set_aux_cycle_output"
SERVICE_SET_CYCLE_OUTPUT = "set_cycle_output"
SERVICE_SET_BATTERY_TYPE = "set_battery_type"
SERVICE_SET_PUMP_PROTECTION = "set_pump_protection"
SERVICE_SET_TANK_SIZE = "set_tank_size"
SERVICE_SET_CONTROLLED_DEVICE = "set_controlled_device"
SERVICE_SET_COOL_SETPOINT_MAX = "set_cool_setpoint_max"
SERVICE_SET_COOL_SETPOINT_MIN = "set_cool_setpoint_min"
SERVICE_SET_LOW_TEMP_PROTECTION = "set_low_temp_protection"
SERVICE_SET_FLOW_METER_MODEL = "set_flow_meter_model"
SERVICE_SET_FLOW_METER_DELAY = "set_flow_meter_delay"
SERVICE_SET_FLOW_METER_OPTIONS = "set_flow_meter_options"
SERVICE_SET_FLOOR_LIMIT_LOW = "set_floor_limit_low"
SERVICE_SET_FLOOR_LIMIT_HIGH = "set_floor_limit_high"
SERVICE_SET_TANK_TYPE = "set_tank_type"
SERVICE_SET_GAUGE_TYPE = "set_gauge_type"
SERVICE_SET_LOW_FUEL_ALERT = "set_low_fuel_alert"
SERVICE_SET_TANK_HEIGHT = "set_tank_height"
SERVICE_SET_FUEL_ALERT = "set_fuel_alert"
SERVICE_SET_POWER_SUPPLY = "set_power_supply"
SERVICE_SET_BATTERY_ALERT = "set_battery_alert"
SERVICE_SET_INPUT_OUTPUT_NAMES = "set_input_output_names"
SERVICE_SET_ACTIVATION = "set_activation"
SERVICE_SET_KEY_DOUBLE_UP = "set_key_double_up"
SERVICE_SET_SENSOR_TYPE = "set_sensor_type"
SERVICE_SET_REMAINING_TIME = "set_remaining_time"
SERVICE_SET_ON_OFF_INPUT_DELAY = "set_on_off_input_delay"
