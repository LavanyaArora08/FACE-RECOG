import cv2

# access the default camera
cap = cv2.VideoCapture(0)

# read a frame from the camera
ret, frame = cap.read()

# show the frame in a window
cv2.imshow('Camera', frame)

# wait for the user to press a key
cv2.waitKey(0)

# save the frame to a file
cv2.imwrite('user_picture.jpg', frame)

# release the camera
cap.release()

# close all windows
cv2.destroyAllWindows()
