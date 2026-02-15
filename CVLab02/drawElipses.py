import cv2

image = cv2.imread("batman.jpg")

# Ellipse 1
cv2.ellipse(image, (200, 200), (100, 50), 0, 0, 360, (0, 255, 0), 3)

# Ellipse 2 (Rotated)
cv2.ellipse(image, (400, 200), (80, 120), 45, 0, 360, (255, 0, 0), 3)

# Ellipse 3 (Partial Arc)
cv2.ellipse(image, (300, 400), (150, 70), 30, 0, 180, (0, 0, 255), 3)

cv2.imshow("Task 1 - Ellipses", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
