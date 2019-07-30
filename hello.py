#!/usr/bin/env python

'''Hello Farmware

A simple Farmware example that tells FarmBot to log a new message.
'''

#from farmware_tools import device
from farmware_tools import app
from farmware_tools import device
from farmware_tools import env
from farmware_tools import get_config_value


device.log(message='Setting variables', message_type='success')
rows = get_config_value(farmware_name='Gridit', config_name='rows', value_type=int)
cols = get_config_value(farmware_name='Gridit', config_name='cols', value_type=int)
spaceBetweenRows = get_config_value(farmware_name='Gridit', config_name='spaceBetweenRows', value_type=float)
spaceBetweenCols = get_config_value(farmware_name='Gridit', config_name='spaceBetweenCols', value_type=float)
startX = get_config_value(farmware_name='Gridit', config_name='startX', value_type=float)
startY = get_config_value(farmware_name='Gridit', config_name='startY', value_type=float)
startZ = get_config_value(farmware_name='Gridit', config_name='startZ', value_type=float)
sequenceBeforeMove = get_config_value(farmware_name='Gridit', config_name='sequenceBeforeMove', value_type=str)
sequenceAfterMove = get_config_value(farmware_name='Gridit', config_name='sequenceAfterMove', value_type=str)

# Values for testing
rows = 4
cols = 7 
spaceBetweenRows = 47
spaceBetweenColumns = 45 
startX = 310.2
startY = 563.8
startZ = 210.96
sequenceBeforeMove = 'PickUpSeed' 
sequenceAfterMove = 'PlantSeed'

device.log(message='Setting sequenceId variables', message_type='success')
sequenceBeforeMoveId = app.find_sequence_by_name(name=sequenceBeforeMove)
sequenceAfterMoveId = app.find_sequence_by_name(name=sequenceAfterMove)

# Start the grid movement
device.log(message='Starting row loop', message_type='success')
device.log(message='Hello Farmware!', message_type='success')
