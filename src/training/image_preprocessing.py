import os
import cv2
from config import train_path, test_path
def preprocess_dataset(dataset_path):
    """
    Preprocess all images in the dataset.

    Steps:
    1. Read image
    2. Resize image
    3. Convert BGR to RGB

    Returns:
        processed_images
        labels
    """
    processed_images = []
    labels = []
    classes = os.listdir(dataset_path)
    for label in classes:
        folder_path = os.path.join(dataset_path, label)
        if not os.path.isdir(folder_path):
            continue
        image_names = os.listdir(folder_path)
        for image_name in image_names:
            image_path = os.path.join(folder_path, image_name)
            # Read image
            image = cv2.imread(image_path)
            if image is None:
                continue
            # Resize image
            image = cv2.resize(image, (640, 480))
            # Convert BGR to RGB
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # Store processed image and label
            processed_images.append(rgb_image)
            labels.append(label)
    return processed_images, labels
if __name__ == "__main__":
    X_train, y_train = preprocess_dataset(train_path)
    X_test, y_test = preprocess_dataset(test_path)
    print("Training Images :", len(X_train))
    print("Training Labels :", len(y_train))
    print("\nTesting Images :", len(X_test))
    print("Testing Labels :", len(y_test))