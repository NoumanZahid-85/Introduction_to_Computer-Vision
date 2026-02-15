import cv2
image = cv2.imread("batman.jpg")

# Normal line
cv2.line(image, (100, 100), (500, 100), (0, 255, 0), 3)

# Arrowed line
cv2.arrowedLine(image, (100, 200), (500, 300), (0, 0, 255), 3)

cv2.imshow("Task 5 - Lines", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
