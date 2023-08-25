'''
Since I had no way to execute the code due to hardware restriction, it may not be 100% accurate
'''
import cv2 
import numpy as np
import tensorflow as tf

# We use a pretrained, or our final trained model here
model = tf.keras.models.load_model('hand_detection_model.h5')

# Initialize the camera or video capture
cap = cv2.VideoCapture(0) 

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform image preprocessing on the captured frame (resize, normalize, denoise, upscale, downscale, etc.)

    # Detect hands using the trained model
    hands = hand_detection(frame, model)

    # Iterate through detected hands and draw bounding boxes
    for hand in hands:
        x, y, w, h = hand  # Assuming 'hand' contains coordinates and dimensions
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with detected hands
    cv2.imshow('Hand Detection', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
