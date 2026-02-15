import cv2
image = cv2.imread("google.jpg")  
if image is None:
    print("Error: Image not found!")
    exit()
    
height, width = image.shape[:2]
resized = cv2.resize(image, (width // 2, height // 2))
rotated = cv2.rotate(resized, cv2.ROTATE_180)
flipped = cv2.flip(rotated, 0)

# 2. Apply Gaussian Blur (5x5 kernel), GaussianBlur(src, kernal size as width, height, sigmaX.
blurred_image = cv2.GaussianBlur(flipped, (7, 7), 0) 

# 3. Convert blurred image to grayscale
gray_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('processed_image.jpg', gray_image)
cv2.imshow("Final Output - Task 2", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Image saved as 'processed_image.jpg'")