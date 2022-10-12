# Trout-Creek-stream-gauge
River stage in distance from strut on bridge condemned after 2007 flood and plotting code

GNU GPL v3 license applies to software.

CC-BY 4.0 license applies to data.

## Data columns

**CSV column**|**Description**
-----|-----
Time [UTC]|Universal Coordinated Time
PressOB [mBar]|Atmospheric pressure from the on-board (and housing-enclosed) BME280 sensor, in units of millibars
RH\_OB [%]|Atmospheric relative humidity from the on-board (and housing-enclosed) BME280 sensor, in percent saturation
TempOB [C]|Atmospheric temperature from the on-board (and housing-enclosed) BME280 sensor, in degrees Celsius
Temp RTC [C]|Atmospheric temperature from the on-board DS3231 real-time clock, in degrees Celsius
Bat [V]|Voltage of the batteries comprising the main power supply; during the 2021–2022 deployment, this was provided by 3x AA cells in series
Range [cm]|Distance reported by the LiDAR Lite laser rangefinder in centimeters
Pitch [deg]|Pitch from horizontal, along long axis of rangefinder assembly ([See annotated figure in README](https://github.com/NorthernWidget-Skunkworks/Project-Symbiont-LiDAR))
Roll [deg]|Roll from horizontal, along long axis of rangefinder assembly ([See annotated figure in README](https://github.com/NorthernWidget-Skunkworks/Project-Symbiont-LiDAR))
