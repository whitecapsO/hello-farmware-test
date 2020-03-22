#!/usr/bin/env python

'''Hello Farmware Test
Farmware that creates a new or updates an existing enviroment variable on the Raspberry Pi. 
Had to reuse the original test to do this as Farmbot wouldn't load new Farmwares.
'''

from farmware_tools import device
#from farmware_tools import env
from farmware_tools import get_config_value
import os

evName = get_config_value(farmware_name='Hello Farmware Test', config_name='evName', value_type=str)
evValue = get_config_value(farmware_name='Hello Farmware Test', config_name='evValue', value_type=str)

device.log(message="Recieved environment variable name: " + str(evName) + " environment variable value: " + str(evValue), message_type="success")

if evName == "default" :
    device.log(message="Please enter an environment variable name" + str(evValue), message_type="success")
elif evName == "default" :
    device.log(message="Please enter an environment variable value" + str(evValue), message_type="success")
else :

    #evCurrentValue = env.os.environ.get(evName, False)
    evCurrentValue = os.environ.get(evName, False)
    if evCurrentValue == False :
        device.log(message="Creating environment variable: " + str(evName) + " value is: " + str(evValue), message_type="success")
        #env.os.environ[evName] = evValue
        os.environ[evName] = evValue
    else :
        device.log(message="Environment variable exists for name: " + str(evName) + " current value is: " + str(evCurrentValue) + " setting value to: " + str(evValue), message_type="success")   
        os.environ[evName] = evValue
       #env.os.environ[evName] = evValue