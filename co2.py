# CO2 sensor

# comands:
# ssh student@192.168.23.207
# password: Engineering!1
# python co2reading.py

# go to GUI: nav > config ip adress > data should be ssh number


import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)
import post_to_web as PTW
import time


co = 1
print RPL.analogRead(co)
average = [ ]
base = 0
CO2detect = 0
content = 0
PTW.state['CO2detect'] = 1
PTW.state['Co2'] = 1

# ^ setup

# begins by averaging the first 1000 readings in order to get a base reading
base = RPL.analogRead(co)

while True:
    content = RPL.analogRead(co)
    if content <= 250 or base - content >= 30:
        CO2detect = 2
        PTW.state['CO2detect'] = 2
        
    elif content <= 190 or base - content >= 50:
        CO2detect = 3
        PTW.state['CO2detect'] = 3

    else:
        CO2detect = 1
        PTW.state['CO2detect'] = 1
        x = 0
    PTW.state['Co2'] = content
    PTW.post()
