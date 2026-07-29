from config import train_path,test_path
from load_dataset import load_dataset
from data_cleaning import clean_dataset  
from image_preprocessing import preprocess_dataset
from hand_detection import detect_hand
from feature_engineering import create_landmark_csv 
print("=" * 50)
print("SIGN LANGUAGE RECOGNITION TRAINING PIPELINE")
print("=" * 50)
print("\nStep 1 : Loading Dataset")
images, labels = load_dataset(train_path)
print("Total Images :", len(images))
print("Total Labels :", len(labels))
print("\nStep 2 : Data Cleaning")
images, labels = clean_dataset(images, labels)
print("Valid Images :", len(images))
print("\nStep 3 : Image Preprocessing")
processed_images = preprocess_dataset(images)
print("Processed Images :", len(processed_images))
print("\nStep 4 : Hand Detection")
landmarks = extract_landmarks(processed_images)
print("Landmarks Extracted :", len(landmarks))
print("\nStep 5 : Feature Engineering")
features = normalize_landmarks(landmarks)
print("Feature Vectors :", len(features))
print("\nStep 6 : Creating CSV")
create_csv(features, labels)
print("\nCSV Created Successfully")
print("\nPipeline Completed Successfully")