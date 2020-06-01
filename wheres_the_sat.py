#!/usr/bin/env python
from skyfield.api import EarthSatellite
from skyfield.api import load
from skyfield.positionlib import Geocentric
from skyfield.units import Angle

ts = load.timescale()
# Time used to find correct satellite
t = ts.utc(2020, 3, 18, 6, 17, 23.0)

# Coordinates used to find correct satellite
loc = Geocentric([-393.9579313710918, -4609.1758828158, -4905.812181143784])

stations = load.tle_file('wheres_the_sat.tle')
print('Loaded', len(stations), 'stations')

# Zero degrees separation
nada = Angle(degrees=0)

# Iterate over stations looking for a collision (zero degrees separation)
for station in stations:
	geocentric = station.at(t)
	if geocentric.separation_from(loc).degrees == nada.degrees:
		# Found a collision
		print(station.name)
		tgt = station

# Time used to find next waypoint
t2 = ts.utc(2020, 3, 18, 22, 44, 49.0)
# Coordinates of next waypoint
geocentric = tgt.at(t2)
print(geocentric.position.km)
