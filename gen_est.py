import cv2

# load the pre-trained models for age and gender classification from the Training folder in the current directory
age_net = cv2.dnn.readNetFromCaffe('deploy_age.prototxt', 'age_net.caffemodel')
gender_net = cv2.dnn.readNetFromCaffe('C:\\Users\\arora\\Desktop\\Programs\\FACE RECOG\\gender_deploy.prototxt', 'C:\\Users\\arora\\Desktop\\Programs\\FACE RECOG\\gender_net.caffemodel')

# access the default camera
cap = cv2.VideoCapture(0)

# read a frame from the camera
ret, frame = cap.read()

# estimate the age and gender of the user in the frame
blob = cv2.dnn.blobFromImage(frame, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746), swapRB=False, crop=False)
gender_net.setInput(blob)
gender_preds = gender_net.forward()
gender = "Male" if gender_preds[0][0] > gender_preds[0][1] else "Female"
age_net.setInput(blob)
age_preds = age_net.forward()
age = int(age_preds[0][0] * 100)

# display the estimated age and gender on the frame
cv2.putText(frame, f"Age: {age} -Gender: {gender}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

# show the frame in a window
cv2.imshow('Camera', frame)

# wait for the user to press a key
cv2.waitKey(0)

# release the camera
cap.release()

# close all windows
cv2.destroyAllWindows()