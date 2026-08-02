import cv2
from camera import Camera
from hand_detector import HandDetector
from feature_extractor import FeatureExtractor
from predictor import Predictor
camera = Camera()
detector = HandDetector()
extractor = FeatureExtractor()
predictor = Predictor()
while True:
    frame = camera.get_frame()
    if frame is None:
        break
    results = detector.detect(frame)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            features = extractor.extract(hand_landmarks)
            prediction = predictor.predict(features)
            detector.draw(frame, results)
            cv2.putText(
                frame,
                f"Prediction : {prediction}",
                (20,50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2
            )
    cv2.imshow("ASL Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
detector.close()