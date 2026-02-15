import cv2
import numpy as np
image = cv2.imread("batman.jpg")

points = np.array([[100, 400],
                   [200, 350],
                   [300, 450],
                   [400, 300]], np.int32)

points = points.reshape((-1, 1, 2))

cv2.polylines(image, [points], False, (255, 0, 255), 3)

cv2.imshow("Task 6 - Polyline", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
