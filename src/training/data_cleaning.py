import os
import cv2
from config import train_path,test_path
# Valid image extensions
valid_extensions = (".jpg", ".jpeg", ".png")
def clean_dataset(Dataset_path):
    valid_images = 0
    classes = os.listdir(Dataset_path)
    for label in classes:
        folder_path = os.path.join(Dataset_path, label)
        if not os.path.isdir(folder_path):
            continue
        image_names = os.listdir(folder_path)
        for image_name in image_names:
            if not image_name.lower().endswith(valid_extensions):
                continue
            image_path = os.path.join(folder_path, image_name)
            image = cv2.imread(image_path)
            if image is None:
                print("Corrupted:", image_path)
                continue
            height, width, channels = image.shape
            if height == 0 or width == 0:
                continue
            valid_images += 1
    return valid_images

if __name__ == "__main__":

    train_valid = clean_dataset(train_path)

    test_valid = clean_dataset(test_path)

    print("Training Images :", train_valid)
    print("Testing Images :", test_valid)