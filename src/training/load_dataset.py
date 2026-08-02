import os
import cv2
from config import train_path, test_path
def load_dataset(dataset_path):
    images = []
    labels = []
    for class_name in os.listdir(dataset_path):
        class_folder = os.path.join(dataset_path, class_name)
        if not os.path.isdir(class_folder):
            continue
        print(f"Loading class: {class_name}")
        for image_name in os.listdir(class_folder):
            image_path = os.path.join(class_folder, image_name)
            image = cv2.imread(image_path)
            if image is None:
                continue
            images.append(image)
            labels.append(class_name)
    return images, labels

if __name__ == "__main__":

    X_train, y_train = load_dataset(train_path)

    X_test, y_test = load_dataset(test_path)

    print("Training Images :", len(X_train))
    print("Training Labels :", len(y_train))

    print("Testing Images :", len(X_test))
    print("Testing Labels :", len(y_test))