#!/usr/bin/env python

'''Hello Farmware Test

A simple Farmware example that tells FarmBot to log a new message including the provided input.
'''

from farmware_tools import get_config_value, device

evName = get_config_value(farmware_name='Hello Farmware Test', config_name='input', value_type=str)
evValue = get_config_value(farmware_name='Hello Farmware Test', config_name='input', value_type=str)

# Load the arguements
# evName = get_config_value(farmware_name='FarmwareEnVar', config_name='evName', value_type=str)
# evValue = get_config_value(farmware_name='FarmwareEnVar', config_name='evValue', value_type=str)

device.log(message="Creating environment variable: " + str(evName) + " value is: " + str(evValue), message_type="success")

if evName != "":
    # Check if the environment variable already exists and if so set the value
    currentValue = os.environ.get(evName,"")
    if currentValue != "" :
        device.log(message="Environment variable exists for name: " + str(evName) + " current value is: " + str(currentValue) + " setting value to: " + str(evValue), message_type="success")
        os.environ['evName'] = evValue
    # Otherwise create a new environment variable and set the value
    else :
        device.log(message="Creating environment variable: " + str(evName) + " value is: " + str(evValue), message_type="success")
        os.environ['evName'] = evValue

''' #device.log(message='Hello Farmware! Test input was: {}'.format(INPUT_VALUE), message_type='success')
""" device.log(message="Message 1 Test", message_type="success")
device.log(message="Message 2 Test", message_type="success")
device.log(message="Message 3 Test", message_type="success")
device.log(message="Message 4 Test", message_type="success")
device.log(message="Message 5 Test", message_type="success") """

currentPosition = device.get_current_position()

device.move_absolute(
device.assemble_coordinate(2218.2, 41, 0),
100,
device.assemble_coordinate(0, 0, 0))

device.log(message="currentPosition:" + str(currentPosition), message_type="success")

# device.move_absolute(
# device.assemble_coordinate(200, 200, 0),
# 100,
# device.assemble_coordinate(0, 0, 0))

# device.move_absolute(
# device.assemble_coordinate(300, 300, 0),
# 100,
# device.assemble_coordinate(0, 0, 0))

# device.move_absolute(
# device.assemble_coordinate(400, 400, 0),
# 100,
# device.assemble_coordinate(0, 0, 0))

# device.move_absolute(
# device.assemble_coordinate(500, 500, 0),
# 100,
# device.assemble_coordinate(0, 0, 0)) '''