import cv2

# Read image
image = cv2.imread("google.jpg")  

# Check if image loaded
if image is None:
    print("Error: Image not found!")
    exit()
    
height, width = image.shape[:2]
resized = cv2.resize(image, (width // 2, height // 2))
rotated = cv2.rotate(resized, cv2.ROTATE_180)
flipped = cv2.flip(rotated, 0)
cv2.imshow("Final Image", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("task1_output.jpg", flipped)

print("Task 1 completed and image saved.")
