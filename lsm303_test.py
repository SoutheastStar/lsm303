# P9_19 --->  SCL (LSM303DLHC)
# P9_20 --->  SDA (LSM303DLHC)

import lsm303
from termcolor import colored
from time import sleep

print colored('Press CTRL+C to stop','green')
print colored('setup: lsm303 ...','green')
sleep(1.0)

bus = lsm303.setup_bus(3)                      # bus: 3 indicates /dev/i2c-3
Sa  = lsm303.setup_acc(bus,lsm303.SCALE_A_8G)  # acc. scale +/- 8.0 g
Sm  = lsm303.setup_mag(bus,lsm303.SCALE_M_81G) # mag. scale +/- 8.1 gauss

while(True):
    a = lsm303.get_acc(bus,Sa)
    m = lsm303.get_mag(bus,Sm)
    print colored('--------------------------------------------------','cyan')	
    print colored('ax = {0:.2f} g; ay = {1:.2f} g; az = {2:.2f} g.','red') .format(a[0],a[1],a[2])
    print colored('mx = {0:.2f} gauss; my = {1:.2f} gauss; mz = {2:.2f} gauss.','red') .format(m[0],m[1],m[2])
    sleep(0.5)
