from flask import Flask, render_template, request
import cv2

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    # access the default camera
    cap = cv2.VideoCapture(0)

    # read a frame from the camera
    ret, frame = cap.read()

    # save the frame to a file
    cv2.imwrite('static/user_picture.jpg', frame)

    # release the camera
    cap.release()

    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
