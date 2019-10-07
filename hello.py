    
#!/usr/bin/env python

'''Hello Farmware
A simple Farmware example that tells FarmBot to log a new message.
'''

from farmware_tools import app
from farmware_tools import device
from farmware_tools import env
from farmware_tools import get_config_value

device.log(message='Hello Farmware!', message_type='success')