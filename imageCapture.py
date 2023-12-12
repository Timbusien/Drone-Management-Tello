from djitellopy import tello
import cv2

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.streamon()

while True:
    image = drone.get_frame_read().frame
    # image = cv2.resize(image, (360, 240))
    cv2.imshow('Image', image)
    cv2.waitKey(1)

