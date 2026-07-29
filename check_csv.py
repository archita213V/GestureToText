import os
import pandas as pd

train_csv = "../landmarks/TrainLandmarks.csv"
test_csv = "../landmarks/TestLandmarks.csv"

print("Train :", os.path.abspath("../landmarks/TrainLandmarks.csv"))
print("Test  :", os.path.abspath("../landmarks/TestLandmarks.csv"))


print(os.path.exists("../landmarks/TrainLandmarks.csv"))
print(os.path.exists("../landmarks/TestLandmarks.csv"))
print(os.path.realpath("../landmarks/TestLandmarks.csv"))

print("Train Exists :", os.path.exists(train_csv))
print("Test Exists  :", os.path.exists(test_csv))

if os.path.exists(train_csv):
    train_df = pd.read_csv(train_csv)
    print("\nTrain Shape :", train_df.shape)
    print(train_df.head())

if os.path.exists(test_csv):
    test_df = pd.read_csv(test_csv)
    print("\nTest Shape :", test_df.shape)
    print(test_df.head())