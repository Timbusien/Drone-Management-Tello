from djitellopy import tello
import KeyPressModule
from time import sleep

KeyPressModule.initial()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())


def getKeyboardInput():
    left_right, forward_backward, up_down, yell_velocity = 0, 0, 0, 0
    speed = 50

# left and right moving keys
    if KeyPressModule.get_keyboard('LEFT'):
        left_right = -speed

    elif KeyPressModule.get_keyboard('RIGHT'):
        left_right = speed

# forward and backward moving keys
    elif KeyPressModule.get_keyboard('UP'):
        forward_backward = speed

    elif KeyPressModule.get_keyboard('DOWN'):
        forward_backward = -speed

# up and down moving keys
    elif KeyPressModule.get_keyboard('w'):
        up_down = speed

    elif KeyPressModule.get_keyboard('s'):
        up_down = -speed

# yell velocity keys
    elif KeyPressModule.get_keyboard('a'):
        yell_velocity = -speed

    elif KeyPressModule.get_keyboard('d'):
        yell_velocity = speed

# land key
    elif KeyPressModule.get_keyboard('q'):
        yell_velocity = drone.land()

# takeoff key
    elif KeyPressModule.get_keyboard('e'):
        yell_velocity = drone.takeoff()

    return [left_right, forward_backward, up_down, yell_velocity]


drone.takeoff()

while True:
    values = getKeyboardInput()
    drone.send_rc_control(values[0], values[1], values[2], values[3])
    sleep(0.05)


