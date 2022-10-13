#! /usr/bin/python3

import pandas as pd
from matplotlib import pyplot as plt
from pandas.plotting import register_matplotlib_converters
import glob

_supplement = False # Set true for supplementary figure

###############################
# IMPORT AND CONCATENATE DATA #
###############################

df = None
for infilename in sorted(glob.glob('../data/Log*.txt')):
    print( infilename, end='; number of data entries: ')
    _df = pd.read_csv(infilename, header=1, infer_datetime_format=True, parse_dates=True, index_col='Time [UTC]', dtype=float, na_values=[' NAN', 50])
    print( len(_df) )
    if df is not None:
        df = df.append(_df)
    else:
        df = _df

dfhr = df.resample('H').mean()

register_matplotlib_converters()

if _supplement:
    minus_days = 0
    plus_days = 0
else:
    minus_days = 360 # After Log00035 added in from bridge removal
    plus_days = 16

# All hourly

if _supplement:
    _fs = 18, 12
else:
    _fs = (9,12)

fig = plt.figure(figsize=_fs)

# Battery voltage
ax1 = plt.subplot(5, 1, 1)
plt.plot(dfhr[' Bat [V]'], 'k-')
plt.ylabel('Battery voltage [V]', fontweight='bold')
if not _supplement:
    plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())

# On-board Temperature
ax2 = plt.subplot(5, 1, 2)
plt.plot(dfhr[' TempOB [C]'], 'g-')
plt.ylabel('On-board\ntemperature [$^\circ$C]', fontweight='bold')
if not _supplement:
    plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
    plt.ylim(( 0, 90 ))
else:
    plt.ylim(-40,90)
    plt.yticks([-40, -0, 40, 80])
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())

# On-board Atmospheric pressure
ax3 = plt.subplot(5, 1, 3)
plt.plot(dfhr[' PresOB [mBar]'], 'g-')
plt.ylabel('On-board atmospheric\npressure [millibar]', fontweight='bold')
if not _supplement:
    plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
    plt.ylim(( 970, 1005 ))
else:
    plt.ylim(( 960, 1020 ))
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())

# On-board relative humidity
ax4 = plt.subplot(5, 1, 4)
plt.plot(dfhr[' RH_OB [%]'], 'g-')
plt.ylabel('On-board\nrelative humidity [%]', fontweight='bold')
if not _supplement:
    plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())

# Stage
ax5 = plt.subplot(5, 1, 5)
plt.plot(dfhr[' Range [cm]'], 'b-')
#plt.ylim(plt.ylim()[::-1])
if not _supplement:
    plt.ylabel('Distance from\nrangefinder to\nwater surface [cm]', fontweight='bold')
    plt.ylim(( 380, 270 ))
    plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
else:
    plt.ylabel('Distance from\nrangefinder to\nsurface [cm]', fontweight='bold')
    plt.ylim(( 390, 270 ))
#plt.xticks(rotation=45)
fig.autofmt_xdate() # Better rotation

plt.xlabel('Date', fontweight='bold')
plt.tight_layout()
if _supplement:
    _fn = 'TroutData_supplement.pdf'
else:
    _fn = 'TroutData.pdf'
plt.savefig(_fn)
plt.show()

