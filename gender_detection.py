import cv2
import numpy as np
import tensorflow as tf

# Define paths to the training data folders
MALE_DIR = "C:/Users/arora/Desktop/Programs/FACE RECOG/Training/male"
FEMALE_DIR = "C:/Users/arora/Desktop/Programs/FACE RECOG/Training/female"

# Define image dimensions and batch size for training
IMG_WIDTH = 128
IMG_HEIGHT = 128
BATCH_SIZE = 32

# Load the trained model from disk
model = tf.keras.models.load_model("C:/Users/arora/Desktop/Programs/FACE RECOG/gender_model.h5")

# Define a function to preprocess an image for input to the model
def preprocess_image(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

# Initialize the default camera
cap = cv2.VideoCapture(0)

# Start capturing frames from the camera
while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    
    # If the frame is not read correctly, break the loop
    if not ret:
        break
    
    # Preprocess the frame for input to the model
    preprocessed = preprocess_image(frame)
    
    # Use the model to predict the gender of the person in the frame
    prediction = model.predict(preprocessed)[0]
    
    # Choose the gender label with the highest probability
    if prediction[0] > prediction[1]:
        gender = "Male"
    else:
        gender = "Female"
    
    # Add the predicted gender label to the frame and display it
    cv2.putText(frame, gender, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Gender Detection", frame)
    
    # Wait for the user to press the 'q' key to quit the program
    if cv2.waitKey(1) == ord("q"):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
