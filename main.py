import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    success, image = cap.read()

    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    all_circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    all_circles_rounded = np.uint16(np.around(all_circles))

    for (x, y, r) in all_circles_rounded[0, :]:
        cv2.circle(img, (x, y), r, (0, 0, 255), 3)
        cv2.circle(img, (x, y), 2, (0, 255, 255), 3)

    cv2.imshow('rez', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()