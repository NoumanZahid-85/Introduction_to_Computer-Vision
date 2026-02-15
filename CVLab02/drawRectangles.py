import cv2

image = cv2.imread("batman.jpg")

# Rectangle 1
cv2.rectangle(image, (100, 100), (300, 300), (0, 255, 0), 3)

# Rectangle 2 (Filled)
cv2.rectangle(image, (350, 150), (550, 350), (255, 0, 0), -1)

cv2.imshow("Task 4 - Rectangles", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
