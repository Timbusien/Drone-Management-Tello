# https://store.dji.com/product/tello
from djitellopy import tello
import KeyPressModule
import time
import cv2

KeyPressModule.initial()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())
drone.streamon()
global image


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
        yell_velocity = drone.land(); time.sleep(3)

# takeoff key
    elif KeyPressModule.get_keyboard('e'):
        yell_velocity = drone.takeoff()

# save key
    elif KeyPressModule.get_keyboard('z'):
        cv2.imwrite(f'Saves/Images/{time.time()}.jpg', image)
        time.sleep(0.5)

    return [left_right, forward_backward, up_down, yell_velocity]


drone.takeoff()

while True:
    values = getKeyboardInput()
    drone.send_rc_control(values[0], values[1], values[2], values[3])
    image = drone.get_frame_read().frame
    # image = cv2.resize(image, (360, 240))
    cv2.imshow('Image', image)
    cv2.waitKey(1)





