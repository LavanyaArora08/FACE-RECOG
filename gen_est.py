import cv2


gender_net = cv2.dnn.readNetFromCaffe('C:\\Users\\arora\\Desktop\\Programs\\FACE RECOG\\gender_deploy.prototxt', 'C:\\Users\\arora\\Desktop\\Programs\\FACE RECOG\\gender_net.caffemodel')

# access cam
cap = cv2.VideoCapture(0)

ret, frame = cap.read()

blob = cv2.dnn.blobFromImage(frame, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746), swapRB=False, crop=False)
gender_net.setInput(blob)
gender_preds = gender_net.forward()
gender = "Male" if gender_preds[0][0] > gender_preds[0][1] else "Female"


cv2.putText(frame, f" Gender: {gender}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

cv2.imshow('Camera', frame)

cv2.waitKey(0)

cap.release()

# close all windows
cv2.destroyAllWindows()
