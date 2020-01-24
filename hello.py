#!/usr/bin/env python

'''Hello Farmware Test

A simple Farmware example that tells FarmBot to log a new message including the provided input.
'''

from farmware_tools import get_config_value, device

INPUT_VALUE = get_config_value(farmware_name='Hello Farmware Test', config_name='input', value_type=str)
device.log(message='Hello Farmware! Test input was: {}'.format(INPUT_VALUE), message_type='success')
device.log(message="Message 1 Test", message_type="success")
device.log(message="Message 2 Test", message_type="success")
device.log(message="Message 3 Test", message_type="success")
device.log(message="Message 4 Test", message_type="success")
device.log(message="Message 5 Test", message_type="success")