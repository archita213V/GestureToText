import os
import cv2
import csv
import mediapipe as mp
from config import train_path, test_path
def create_landmark_csv(dataset_path, output_csv):
    """
    Extract 21 hand landmarks from all images and
    save them into a CSV file.
    """
    # Create output folder if it doesn't exist
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=1,
        min_detection_confidence=0.5
    )
    with open(output_csv, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        # CSV Header
        header = []
        for i in range(1, 22):
            header.extend([f"x{i}", f"y{i}", f"z{i}"])
        header.append("Label")
        writer.writerow(header)
        total_images = 0
        total_saved = 0
        classes = sorted(os.listdir(dataset_path))
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
                # Convert BGR → RGB
                rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                # Detect Hand
                results = hands.process(rgb_image)
                total_images += 1
                if results.multi_hand_landmarks:
                    # Only first hand
                    hand_landmarks = results.multi_hand_landmarks[0]
                    landmarks = []
                    # Store 21 landmarks
                    for landmark in hand_landmarks.landmark:
                        landmarks.append([
                            landmark.x,
                            landmark.y,
                            landmark.z
                        ])
                    # Wrist coordinates
                    wrist_x = landmarks[0][0]
                    wrist_y = landmarks[0][1]
                    wrist_z = landmarks[0][2]
                    features = []
                    # Normalize landmarks
                    for point in landmarks:
                        features.append(point[0] - wrist_x)
                        features.append(point[1] - wrist_y)
                        features.append(point[2] - wrist_z)
                    # Add class label
                    features.append(label)
                    # Save one row
                    writer.writerow(features)
                    total_saved += 1
    hands.close()
    print("\nCSV Saved Successfully")
    print("Output File      :", output_csv)
    print("Images Processed :", total_images)
    print("Rows Saved       :", total_saved)
if __name__ == "__main__":
    print("=" * 50)
    print("CREATING TRAINING LANDMARK CSV")
    print("=" * 50)
    create_landmark_csv(
        train_path,
        "../landmarks/TrainLandmarks.csv"
    )
    print("\n")
    print("=" * 50)
    print("CREATING TESTING LANDMARK CSV")
    print("=" * 50)
    create_landmark_csv(
        test_path,
        "../landmarks/TestLandmarks.csv"
    )
    print("\nAll CSV files created successfully!")
