#!/usr/bin/env python

'''Hello Farmware Test
Farmware that creates a new or updates an existing enviroment variable on the Raspberry Pi. 
Had to reuse the original test to do this as Farmbot wouldn't load new Farmwares.
'''

from farmware_tools import device
from farmware_tools import get_config_value
import json
import os

evName = get_config_value(farmware_name='Hello Farmware Test', config_name='evName', value_type=str)
evValue = get_config_value(farmware_name='Hello Farmware Test', config_name='evValue', value_type=str)

device.log(message="Recieved environment variable name: " + str(evName) + " environment variable value: " + str(evValue), message_type="success")

if evName == "default" :
    device.log(message="Please enter an environment variable name" + str(evValue), message_type="success")
elif evValue == "default" :
    device.log(message="Please enter an environment variable value" + str(evValue), message_type="success")
else :
    configFileName = 'config.json'
    config = {evName: evValue}   
    fileName = '/tmp/farmware/' + configFileName

    # If the file exists delete it
    if os.path.isfile(fileName) :
        os.remove(fileName)
        device.log(message="Config file: " + str(fileName) + " existed so deleteing it", message_type="success")
    
    # Create a new file and load the config
    with open(fileName, 'w') as f:
        json.dump(config, f)
        f.close()
    device.log(message="Created new config file: " + str(fileName) + " and wrote environment variables to it", message_type="success")
