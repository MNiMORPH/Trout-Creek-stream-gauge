[![DOI](https://zenodo.org/badge/549840719.svg)](https://zenodo.org/badge/latestdoi/549840719)

# Trout-Creek-stream-gauge
River stage in distance from strut on bridge condemned after 2007 flood and plotting code

GNU GPL v3 license applies to software.

CC-BY 4.0 license applies to data.

## Location

**Lon**|**Lat**
-----|-----
-91.94081|44.19646

## Data collection timeline

### Full date range

2021-06-03 to 2022-09-13 (old bridge)
2023-10-28 to the time of writing (new bridge)

### Start: 2021-06-03

Installed during field work associated with NSF-funded project, [1944782 -- CAREER: Alluvial-river dynamics through watershed networks](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1944782).

### Reprogram: 2021-08-17

ADW realized that even if the [Margay data logger](github.com/NorthernWidget/Project-Margay) should be able to last for >1 year at 1-minute logging intervals, the laser required much more power. ADW reduced the logging frequency from once per minute to once per five minutes.

### Removal: 2022-09-13

The condemned bridge on which we installed the stream gauge was taken out for replacement. Jaime Edwards and Garrett Owens, both of the Minnesota Department of Natural Resources, rescued the stream gauge and data logger and delivered it to ADW at SAFL. Shortly thereafter, ADW shipped the Margay logger to colleagues working on the Athabasca Glacier.

### Reinstallation: 2023-10-28

After Caltronics built and sent us the first batch of Margay v3.0 data loggers, we prepared and installed one on the upstream side of the rebuilt bridge during the make-up field trip for UMN's *ESCI 4701/8701: Geomorphology* class. We fixed the data logger to the steel I-beam on the side via 4x 1" C clamps (standard/removable hardware-store ones) via the Nilon cutting board on which it was already mounted. We separated the laser rangefinder from the cutting-board platform and fixed it to the top of a horizontal beam such that it looks down directly over the water, and then cinched the cables to the same beam. Turning on and off the data logger requires climbing over the bridge railing and reaching down. The box opens top-down, which is a bit concerning to me, but maybe shouldn't be.

Note on what we learned from before: We should add lock washers to the #4 screws holding the Margay data logger in place. These screws below the mounting plate had come loose, so we took it apart to tighten them. Many of the screws for the battery pack were loose too, despite their lock washers.

Those involved in the deployment were:
* Andy Wickert
* Vaughn Swindlehurst (UMN ESCI undergrad)
* Brady Bettin (UMN ESCI undergrad)

The logger was set to record data every 1 minute.

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

Stream gauge in context, bolted to bridge. Wide-angle camera shot. Prof. Crystal Ng under bridge with acoustic Doppler velocimiter (ADV); Profs. Doug Faulkner, Colin Belby, and students in the far distance.

*Photo: Andy Wickert*

<br/>

![Margay data logger and box with mounting plate and stand-offs.](images/DSC_3278_TroutGaugeLoggerTopOpen.JPG)

Margay data logger and box with mounting plate and stand-offs. Note how it is bolted to bridge struts.

*Photo: Andy Wickert*

<br/>

![Laser rangefinder from the base of the stream-gauge installation. Held on by square U bolts via a cutting board from the local hardware store (St. Charles, MN).](images/DSC_2522_TroutGaugeBottomLiDARLite.JPG)

Laser rangefinder from the base of the stream-gauge installation. Held on by square U bolts via a cutting board from the local hardware store (St. Charles, MN). The data logger is on the opposite side of the cutting board (nylon platform).

*Photo: Andy Wickert*

## Funding support

<img src="https://www.nsf.gov/news/mmg/media/images/nsf_logo_f_ba321daf-8607-41d7-94bc-1db6039d7893.jpg" alt="NSF" width="240px">

<img src="https://ane4bf-datap1.s3-eu-west-1.amazonaws.com/wmocms/s3fs-public/styles/featured_media_detail/public/advanced_page/featured_media/wmologo2016_fulltext_horizontal_rgb_en-2.jpg?C4guHHfFZ0Uv029Eo5AvJLFg6nMR47hI&itok=NVNNIT7H" alt="WMO" width="240px">

<img src="https://northernwidget.com/assets/images/NWseal_600px.png" alt="Northern Widget LLC" width="160px">
