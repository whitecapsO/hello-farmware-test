from farmware_tools import app
from farmware_tools import device
from farmware_tools import env
from farmware_tools import get_config_value

try:
    INPUT_VALUE = get_config_value(farmware_name="HelloFarmware", config_name="input", value_type=str)
    device.log(message="Hello Farmware! Input was: {}".format(INPUT_VALUE), message_type="success")
    # device.log(message="Message 1 Test", message_type="success")
    # device.log(message="Message 2 Test", message_type="success")
    # device.log(message="Message 3 Test", message_type="success")
    # device.log(message="Message 4 Test", message_type="success")
    # device.log(message="Message 5 Test", message_type="success")

        device.move_absolute(
        device.assemble_coordinate(100, 100, 0),
        100,
        device.assemble_coordinate(0, 0, 0))

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
        # device.assemble_coordinate(0, 0, 0))
except Exception as error:
    device.log(repr(error))
