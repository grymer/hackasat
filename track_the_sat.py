#!/usr/bin/env python
from skyfield.api import EarthSatellite
from skyfield.api import load
from skyfield.api import Topos
from datetime import datetime, timedelta
from skyfield.api import utc

# Convert supplied azimuth/elevation in degrees to motor duty cycle
def duty_cycle(angle):
	clipped = angle % 180
	return int((((7372 - 2457)/180)*clipped)+2457)

# Coordinates for groundstation
ground_station = Topos('-0.4396 N', '39.67 E')
epoch = datetime.fromtimestamp(1586094348.883889, utc)
tgt = 'GLOBALSTAR M092'

stations = load.tle_file('track_the_sat.tle')
print('Loaded', len(stations), 'stations')

by_name = {station.name: station for station in stations}

diff = by_name[tgt] - ground_station
	
ts = load.timescale()

moment = epoch
for i in range(1, 721):
	t = ts.utc(moment)
	alt, az, distance = diff.at(t).altaz()
	print(moment.timestamp(), duty_cycle(az.degrees), duty_cycle(alt.degrees), sep=', ')
	moment = moment + timedelta(seconds=1)
