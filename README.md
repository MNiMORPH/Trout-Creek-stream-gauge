# Trout-Creek-stream-gauge
River stage in distance from strut on bridge condemned after 2007 flood and plotting code

GNU GPL v3 license applies to software.

CC-BY 4.0 license applies to data.

## Location

**Lon**|**Lat**
-----|-----
44.19646|-91.94081

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

## Deployment images

![Stream gauge in context, bolted to bridge. Wide-angle camera shot. Prof. Crystal Ng under bridge with acoustic Doppler velocimiter (ADV); Profs. Doug Faulkner, Colin Belby, and students in the far distance.](images/DSC_2517_BridgeWideAngle.JPG)

![Margay data logger and box with mounting plate and stand-offs.](images/DSC_3278_TroutGaugeLoggerTopOpen.JPG)

![Laser rangefinder from the base of the stream-gauge installation. Held on by square U bolts via a cutting board from the local hardware store (St. Charles, MN).](images/DSC_2522_TroutGaugeBottomLiDARLite.JPG)
