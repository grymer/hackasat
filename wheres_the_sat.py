#!/usr/bin/env python
from skyfield.api import EarthSatellite
from skyfield.api import load
from skyfield.api import Topos

# The supplied TLE has incorrect checksums, which should be 2 and 4 respectively.
# However, Skyfield will parse the TLE without modification and not fail on bad checksums.
line1 = '1 13337U 98067A   20087.38052801 -.00000452  00000-0  00000+0 0  9995'
line2 = '2 13337  51.6460  33.2488 0005270  61.9928  83.3154 15.48919755219337'

ts = load.timescale()

satellite = EarthSatellite(line1, line2, 'REDACTED', ts)

# Time of fly-by
t = ts.utc(2020, 3, 26, 21, 52, 12)

# Coordinates for the Washington Monument
monument = Topos('38.8895 N', '77.0353 W')

geocentric = satellite.at(t)

difference = satellite - monument
topocentric = difference.at(t)

alt, az, distance = topocentric.altaz()

# Convert elevation to KML tilt
print(90 - alt.degrees, 'deg')
# Satellite-relative azimuth
print(az.degrees - 180, 'deg')
print(int(distance.m), 'm')
