#!/usr/bin/env python

'''Hello Farmware Input
A simple Farmware example that tells FarmBot to log a new message including the provided input.
'''
from farmware_tools import app
from farmware_tools import device
from farmware_tools import env

try:
	device.move_absolute(
	    {
	        'kind': 'coordinate',
	        'args': {'x': 10, 'y': 10, 'z': 0}
	    },
	    100,
	    {
	        'kind': 'coordinate',
	        'args': {'x': 0, 'y': 0, 'z': 0}
	    }
	)
	INPUT_VALUE = get_config_value(farmware_name='Hello Farmware Input', config_name='input', value_type=str)
	device.log(message='Hello Farmware! Input was: {}'.format(INPUT_VALUE), message_type='success')
except Exception as error:
    device.log(repr(error))
