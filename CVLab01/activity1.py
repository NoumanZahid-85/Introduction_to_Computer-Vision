import cv2

image = cv2.imread('google.jpg')   # load img
# Check if image loaded
if image is None:
    print("Error: Image not found.")
    exit()

height, width = image.shape[:2] # only take first two height and width dimensions
resized_image = cv2.resize(image, (width // 2, height // 2))

rotated_image = cv2.rotate(resized_image, cv2.ROTATE_180) # rotate this img to 180 clockwise
flipped_image = cv2.flip(rotated_image, 0)

cv2.imshow("Final Output - Task 1", flipped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



