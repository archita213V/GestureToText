import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("../landmarks/TrainLandmarks.csv")

# 1. Shape
print("\nDataset Shape")
print(df.shape)

# 2. First 5 Rows
print("\nFirst 5 Rows")
print(df.head())

# 3. Last 5 Rows
print("\nLast 5 Rows")
print(df.tail())

# 4. Data Types
print("\nData Types")
print(df.dtypes)

# 5. Missing Values
print("\nMissing Values")
print(df.isnull().sum())

# 6. Duplicate Rows
print("\nDuplicate Rows")
print(df.duplicated().sum())

# 7. Statistical Summary
print("\nStatistical Summary")
print(df.describe())

# 8. Class Distribution
print("\nClass Distribution")
print(df["Label"].value_counts())

# Plot Class Distribution
plt.figure(figsize=(10,5))
df["Label"].value_counts().plot(kind="bar")
plt.title("Class Distribution")
plt.xlabel("Alphabet")
plt.ylabel("Number of Samples")
plt.tight_layout()
plt.show()