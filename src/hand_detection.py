import os
import cv2
import mediapipe as mp
from config import train_path, test_path
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.5
)
mp_draw = mp.solutions.drawing_utils
def detect_hand(dataset_path):
    """
    Detect hand landmarks from all images in the dataset.
    """
    total_images = 0
    detected_hands = 0
    classes = os.listdir(dataset_path)
    for label in classes:
        class_path = os.path.join(dataset_path, label)
        if not os.path.isdir(class_path):
            continue
        image_names = os.listdir(class_path)
        for image_name in image_names:
            image_path = os.path.join(class_path, image_name)
            image = cv2.imread(image_path)
            if image is None:
                continue
            # Resize image
            image = cv2.resize(image, (640, 480))
            # Convert BGR to RGB
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # Detect Hand
            results = hands.process(rgb_image)
            total_images += 1
            if results.multi_hand_landmarks:
                detected_hands += 1
                for hand_landmarks in results.multi_hand_landmarks:
                    features = []
                    for landmark in hand_landmarks.landmark:
                        features.append(landmark.x)
                        features.append(landmark.y)
                        features.append(landmark.z)
                    print(
                        f"{label} -> {image_name} -> "
                        f"Features: {len(features)}"
                    )
                    # Draw landmarks
                    mp_draw.draw_landmarks(
                        image,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS
                    )
            # Show image
            cv2.imshow("Hand Detection", image)
            # Press ESC to stop
            if cv2.waitKey(1) & 0xFF == 27:
                hands.close()
                cv2.destroyAllWindows()
                return
    print("Total Images      :", total_images)
    print("Hands Detected    :", detected_hands)
  
if __name__ == "__main__":
    print("Processing Training Dataset...\n")
    detect_hand(train_path)
    print("\nProcessing Testing Dataset...\n")
    detect_hand(test_path)
    hands.close()
    cv2.destroyAllWindows()
    