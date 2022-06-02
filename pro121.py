#importing libraries
import cv2
import numpy as np

#starting the video capture and image
video = cv2.VideoCapture(0)
image = cv2.imread("city.jpg")

#using while need to read the frames of the video and image
while True:

#start reading the frames
    ret , frame = video.read()
    print(frame)



#resizing the image and video 
    frame = cv2.resize(frame , (640 , 480))
    image = cv2.resize(frame  , (640 , 480))

#using the variables creating RGB faint black colur and dark shade black
    u_black = np.array([104,153,700])
    l_black = np.array([30,30,0])


#creating mask using inRnage and passing frame inside it.
    mask = cv2.inRange(frame , l_black , u_black)
    res = cv2.bitwise_and(frame , frame , mask = mask)

#using np.where function to return frame and image
    f = frame - res
    f = np.where(f == 0 , image, f)



#showing the real video and image using imshow() of fucntion
    cv2.imshow("video" , frame)
    cv2.imshow("mask" , f)



#breaking the loop if the user press q (doubt)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

#now releasing the video and close the video windows
video.release()
cv2.destroyAllWindows()
