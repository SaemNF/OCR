import cv2, argparse, pytesseract
import numpy as np

img_path = '/home/cbrd/Desktop/pictures/images.jpeg'

img = cv2.imread(img_path) # Read image 

# Setting parameter values 
#t_lower = 50 # Lower Threshold 
#t_upper = 150 # Upper threshold 

# Applying the Canny Edge filter 
# edge = cv2.Canny(img, t_lower, t_upper) 
edge = cv2.cvtColor(img, cv2.COLOR_BGR2HSV ) 
#edge = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY ) 

#define range of red color in HSV
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])

#threshold the HSV image to get only red colors
mask = cv2.inRange(edge, lower_red, upper_red)

#invert the mask to get non-red regions
mask_inv = cv2.bitwise_not(mask)

#black background
black_background = np.zeros_like(img)

#apply gaussion blur to non-red regions
#blurred = cv2.GaussianBlur(img, (15,15), 0)

# sharpen the red regions
sharpen_kernel = np.array([[-1,-1,-1],
                           [-1,9,-1],
                           [-1,-1,-1]])
sharpened_red = cv2.filter2D(img, -1, sharpen_kernel)
sharpened_red = cv2.bitwise_and(sharpened_red, sharpened_red, mask=mask)

#combine the original image with the blurred image
result = cv2.bitwise_and(img, img, mask=mask)
result += cv2.bitwise_and(black_background, black_background, mask=mask_inv)

custom_config = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(result,config=custom_config))

#display the result
cv2.imshow('original', img) 
cv2.imshow('edge', result) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 


