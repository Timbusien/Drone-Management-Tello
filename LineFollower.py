import cv2
import numpy

cap = cv2.VideoCapture(1)
hsvVals = [0, 0, 117, 179, 22, 219]
sensors = 3
threshold = 0.2


def thresholding(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = numpy.array([hsvVals[0], hsvVals[1], hsvVals[2]])
    upper = numpy.array([hsvVals[3], hsvVals[4], hsvVals[5]])
    mask = cv2.inRange(hsv, lower, upper)
    return mask


def get_Contours(imgThres, image):
    contours, hieracrhy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    biggest = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(biggest)
    cx = x + w // 2
    cy = y + h // 2
    cv2.drawContours(imgThres, biggest, -1, (255, 0, 255), 7)
    cv2.circle(image, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    return cx


def getSensorOutput(imgThres, sensors):
    images = numpy.hsplit(imgThres, sensors)
    totalPixels = (image.shape[1] // sensors) * image.shape[0]
    senOut = []

    for x, im in enumerate(images):
        pixelCount = cv2.countNonZero(im)
        if pixelCount > threshold * totalPixels:
            senOut.append(1)
        else:
            senOut.append(0)
    #     cv2.imshow(str(x), im)
    # print(senOut)

    return senOut


def sendCommands(senOut, cx):
    pass

while True:
    _, image = cap.read()
    image = cv2.resize(image, (480, 360))
    # image = cv2.flip(image, 0)

    imgThres = thresholding(image)
    cx = get_Contours(imgThres, image)
    senOut = getSensorOutput(imgThres, sensors)
    sendCommands(senOut, cx)
    getSensorOutput(imgThres, sensors)
    cv2.imshow('Output', image)
    cv2.imshow('Path', imgThres)
    cv2.waitKey(1)


