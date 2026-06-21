import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# --- 1. INITIALIZATION ---

# Load the Emotion "Brain" (Mini-Xception)
model_path = 'fer2013_mini_XCEPTION.102-0.66.hdf5'
classifier = load_model(model_path, compile=False)
# We keep this list here just so we know what index belongs to what emotion
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Set up the Modern Face Detector
# NOTE: Download 'blaze_face_short_range.tflite' and rename to 'detector.tflite'
base_options = python.BaseOptions(model_asset_path='detector.tflite')
options = vision.FaceDetectorOptions(base_options=base_options)
detector = vision.FaceDetector.create_from_options(options)

# Start Webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    # Convert OpenCV image to MediaPipe Image format
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    # Detect faces
    detection_result = detector.detect(mp_image)

    # Process results
    if detection_result.detections:
        for detection in detection_result.detections:
            # Get Bounding Box
            bbox = detection.bounding_box
            x, y, w, h = bbox.origin_x, bbox.origin_y, bbox.width, bbox.height
            
            # Clip coordinates to screen size
            x, y = max(0, x), max(0, y)
            
            # --- Emotion Recognition Part ---
            face_roi = frame[y:y+h, x:x+w]
            if face_roi.size > 0:
                gray_face = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)
                # 1. Change size to 64x64 to match your specific model
                gray_face = cv2.resize(gray_face, (64, 64))
                gray_face = gray_face.astype('float32') / 255.0
                
                # 2. Safely add the channel (1) and batch (1) dimensions
                gray_face = img_to_array(gray_face) # Makes it (64, 64, 1)
                gray_face = np.expand_dims(gray_face, axis=0) # Makes it (1, 64, 64, 1)

                prediction = classifier.predict(gray_face, verbose=0)[0]
                
                # --- NEW CHILL VS ENERGETIC LOGIC ---
                # Group the 7 emotions into strictly Chill or Energetic
                # Energetic = Happy (index 3) + Surprise (index 5)
                energetic_score = prediction[3] + prediction[5]

                # Chill = Angry (0), Disgust (1), Fear (2), Sad (4), Neutral (6)
                chill_score = prediction[0] + prediction[1] + prediction[2] + prediction[4] + prediction[6]

                # Only output one of these two words!
                if energetic_score > chill_score:
                    final_emotion = "Energetic"
                    box_color = (0, 255, 255) # Yellow box for energetic
                else:
                    final_emotion = "Chill"
                    box_color = (255, 150, 0) # Blue/Teal box for chill

                # Drawing the new colored box and simplified text
                cv2.rectangle(frame, (x, y), (x+w, y+h), box_color, 2)
                cv2.putText(frame, final_emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, box_color, 2)

    cv2.imshow('Robot Vision', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()