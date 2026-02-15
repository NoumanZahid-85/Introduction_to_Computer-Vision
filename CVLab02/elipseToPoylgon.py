import cv2
image = cv2.imread("batman.jpg")

# Original ellipse
center = (300, 300)
axes = (150, 80)
angle = 30

cv2.ellipse(image, center, axes, angle, 0, 360, (0, 255, 0), 2)

# Convert ellipse to polygon
points = cv2.ellipse2Poly(center, axes, angle, 0, 360, 10)

# Draw polygon
cv2.polylines(image, [points], True, (0, 0, 255), 2)

cv2.imshow("Task 2 - Ellipse to Polygon", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
