import cv2
from djitellopy import tello
import KeyPressModule
from time import sleep
import numpy
import math

'''ПАРАМЕТРЫ'''
forward_speed = 117/10
angular_speed = 360/10
interval = 0.25
distance_interval = forward_speed * interval
angular_interval = angular_speed * interval

x, y = 500, 500
a = 50


KeyPressModule.initial()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())
points = [(0, 0), (0, 0)]

def getKeyboardInput():
    left_right, forward_backward, up_down, yell_velocity = 0, 0, 0, 0
    speed = 15
    angular_speed = 50
    global x, y, yaw, a
    d = 0
# left and right moving keys
    if KeyPressModule.get_keyboard('LEFT'):
        left_right = -speed
        d = distance_interval
        a = -180

    elif KeyPressModule.get_keyboard('RIGHT'):
        left_right = speed
        d = -distance_interval
        a = 180

# forward and backward moving keys
    elif KeyPressModule.get_keyboard('UP'):
        forward_backward = speed
        d = distance_interval
        a = 270

    elif KeyPressModule.get_keyboard('DOWN'):
        forward_backward = -speed
        d = -distance_interval
        a = 90

# up and down moving keys
    elif KeyPressModule.get_keyboard('w'):
        up_down = speed

    elif KeyPressModule.get_keyboard('s'):
        up_down = -speed

# yell velocity keys
    elif KeyPressModule.get_keyboard('a'):
        yell_velocity = -angular_speed
        yaw -= angular_interval

    elif KeyPressModule.get_keyboard('d'):
        yell_velocity = angular_speed
        yaw += angular_interval

# land key
    elif KeyPressModule.get_keyboard('q'):
        yell_velocity = drone.land(); sleep(3)

# takeoff key
    elif KeyPressModule.get_keyboard('e'):
        yell_velocity = drone.takeoff()

    sleep(interval)
    a += yaw
    x += int(d * math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))

    return [left_right, forward_backward, up_down, yell_velocity, x, y]


def draw_Points(image, points):
    for point in points:
        cv2.circle(image, point, 20, (0, 0, 225), cv2.FILLED)
    cv2.circle(image, points[-1], 8, (0, 225, 0), cv2.FILLED)
    cv2.putText(image, f'({(points[-1][0] - 500) / 100}), {(points[-1][1] - 500) / 100}m',
                (points[-1][0] + 10, points[-1][1] + 30), cv2.FONT_HERSHEY_PLAIN, 1,
                (255, 0, 255), 1)


while True:
    values = getKeyboardInput()
    drone.send_rc_control(values[0], values[1], values[2], values[3])
    image = numpy.zeros((1000, 1000, 3), numpy.uint8)

    if (points[-1][0] != values[4] or points[-1][1] != values[5]):
        points.append((values[4], values[5]))

    draw_Points(image, points)
    cv2.imshow('Output', image)
    cv2.waitKey(1)



