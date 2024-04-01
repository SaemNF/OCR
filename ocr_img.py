import cv2, pytesseract, os
import numpy as np
import img_editor as edit


## Using camera to capture picture
# intialize the webcam and pass a constant which is 0
cam = cv2.VideoCapture(0)

# title of the app
cv2.namedWindow('python webcam screenshot app')
cv2.startWindowThread()

# let's assume the number of images gotten is 0
img_counter = 0

# path for the taken image
path = '/home/cbrd/Desktop/pictures'

# list of the pictures
pictures_list = []

# while loop
while True:
    # intializing the frame, ret
    ret, frame = cam.read()
    # if statement
    if not ret:
        print('failed to grab frame')
        break
    # the frame will show with the title of test
    cv2.imshow('test', frame)
    #to get continuous live video feed from my laptops webcam
    k  = cv2.waitKey(1) & 0xff
    # if the escape key is been pressed, the app will stop
    if k == 27:
        print('escape hit, closing the app')
        break
    # if the spacebar key is been pressed
    # screenshots will be taken
    elif k%256  == 32:
        # the format for storing the images scrreenshotted
        img_name = f'opencv_frame_{img_counter}.jpg'
        # saves the image as a png file
        cv2.imwrite(os.path.join(path, img_name), frame)
        print('screenshot taken')
        # print(os.listdir('/home/cbrd/Desktop/pictures')) 
        pictures_list.append(os.path.join(path, img_name))
        print("pictures_list:",pictures_list)
        # the number of images automaticallly increases by 1
        img_counter += 1

# release the camera
cam.release()

try:
    # stops the camera window
    cv2.waitKey(1)
    cv2.destoryAllWindows()
    cv2.waitKey(1)
except:
    pass

if pictures_list==[]:
    print("script end")
else:
    ## Processing the image
    print("processing the image..\n")

    img = cv2.imread(pictures_list[0])

    # get grayscale image
    def get_grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    get_grayscale(img)

    # Adding custom options
    custom_config = r'--oem 3 --psm 6'
    print(pytesseract.image_to_string(img,config=custom_config))

