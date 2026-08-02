import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = os.path.abspath(
    os.path.join(BASE_DIR, "..")
)

train_path = os.path.join(
    PROJECT_ROOT,
    "data",
    "Train_Alphabet"
)

test_path = os.path.join(
    PROJECT_ROOT,
    "data",
    "Test_Alphabet"
)
