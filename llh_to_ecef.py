# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
# Converts LLH to ECEF vector components
# Parameters:
# lat_deg: LLH latitude in deg
# lon_deg: LLH longitude in deg
# hae_km: LLH height above ellipsoid in km
# Output:
# Prints the ECEF x-component, y-component, and z-component in km
#
# Written by Josefine Krohn (based off of code written by Dr. Brad Denby)
#
# import Python modules
import math # math module
# "constants"
R_E_KM = 6378.1363
E_E = 0.081819221456


# converting angles in deg to rad
lat_rad = lat_deg*math.pi/180
lon_rad = lon_deg*math.pi/180


# calculations
denom = math.sqrt(1 - (E_E**2)*(math.sin(lat_rad)**2))
c_E = R_E_KM/denom
s_E = R_E_KM*(1 - E_E**2)/denom
r_x_km = (c_E + hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
r_y_km = (c_E + hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
r_z_km = (s_E + hae_km)*math.sin(lat_rad)


# print ECEF x-component, y-component, and z-component in km
print(r_x_km)
print(r_y_km)
print(r_z_km)

