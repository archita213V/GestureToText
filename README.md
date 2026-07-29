# Sign Language to Text Converter

## Overview

The Sign Language to Text Converter is a Machine Learning project that recognizes American Sign Language (ASL) alphabet gestures and converts them into text. The project uses MediaPipe to detect hand landmarks, extracts landmark-based features, trains a Machine Learning model for gesture classification, and performs real-time prediction using a webcam.

The system is designed to provide an efficient and accurate method for recognizing hand gestures while being computationally lightweight by using landmark coordinates instead of raw images.

---

# Features

* Detects hand landmarks using MediaPipe.
* Supports American Sign Language (ASL) alphabet recognition.
* Extracts 21 hand landmarks (63 features).
* Performs feature engineering using wrist-normalized coordinates.
* Creates structured CSV datasets for training and testing.
* Performs Exploratory Data Analysis (EDA).
* Trains a Machine Learning classification model.
* Evaluates model performance using standard metrics.
* Saves the trained model for future predictions.
* Supports real-time hand gesture recognition through a webcam.

---

# Project Workflow

```
Dataset Collection
        │
        ▼
Load Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Image Preprocessing
        │
        ▼
Hand Detection (MediaPipe)
        │
        ▼
Landmark Extraction
        │
        ▼
Feature Engineering
        │
        ▼
Create Landmark CSV
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Data Preparation
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Save Trained Model
        │
        ▼
Real-Time Prediction
```

---

# Technologies Used

### Programming Language

* Python

### Libraries

* OpenCV
* MediaPipe
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Joblib

### Machine Learning

* Random Forest Classifier

### Development Tools

* Visual Studio Code
* Jupyter Notebook
* Git
* GitHub

---

# Project Structure

```
gestureTotext/
│
├── data/
│   ├── Train_Alphabet/
│   └── Test_Alphabet/
│
├── landmarks/
│   ├── TrainLandmarks.csv
│   └── TestLandmarks.csv
│
├── models/
│
├── notebooks/
│
├── src/
│   ├── config.py
│   ├── load_dataset.py
│   ├── data_cleaning.py
│   ├── image_preprocessing.py
│   ├── hand_detection.py
│   ├── feature_engineering.py
│   ├── create_landmarks.py
│   ├── eda.py
│   ├── prepare_data.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   ├── realtime_prediction.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Dataset

The project uses an American Sign Language (ASL) alphabet dataset consisting of separate training and testing folders.

Dataset Structure

```
Train_Alphabet/
    A/
    B/
    C/
    ...
    Z/

Test_Alphabet/
    A/
    B/
    C/
    ...
    Z/
```

Each class contains multiple images representing a single ASL alphabet.

---

# Data Preprocessing

The preprocessing pipeline consists of the following steps:

* Load all images from the dataset.
* Remove unreadable or corrupted images.
* Resize every image to a fixed resolution.
* Convert images from BGR to RGB.
* Detect hands using MediaPipe.
* Extract 21 hand landmarks.
* Normalize landmarks with respect to the wrist coordinate.
* Store the extracted landmark coordinates into CSV files.

---

# Feature Engineering

The project uses landmark-based feature engineering.

For each detected hand:

* 21 landmarks are extracted.
* Each landmark contains:

  * x coordinate
  * y coordinate
  * z coordinate

Total Features

```
21 × 3 = 63 Features
```

The wrist landmark is used as the reference point to normalize all coordinates, making the model more robust to changes in hand position.

---

# Exploratory Data Analysis

EDA includes:

* Dataset shape
* Missing value analysis
* Duplicate value analysis
* Statistical summary
* Data types
* Class distribution
* Feature inspection

---

# Model Training

The project uses the Random Forest Classifier.

Training Steps

1. Load training CSV.
2. Separate features and labels.
3. Encode class labels.
4. Train the Random Forest model.
5. Evaluate on testing data.
6. Save the trained model.

---

# Evaluation Metrics

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Classification Report

---

# Installation

Clone the repository

```bash
git clone <repository_url>
```

Move to the project directory

```bash
cd gestureTotext
```

Create a virtual environment

```bash
python -m venv sign_env
```

Activate the virtual environment

Windows

```bash
sign_env\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Usage

Generate landmark CSV files

```bash
python src/create_landmarks.py
```

Perform Exploratory Data Analysis

```bash
python src/eda.py
```

Train the Machine Learning model

```bash
python src/train_model.py
```

Run real-time prediction

```bash
python src/realtime_prediction.py
```

---

# Future Improvements

* Word formation from detected alphabets.
* Sentence generation.
* Space and delete gesture recognition.
* Text-to-Speech conversion.
* Deep Learning model implementation.
* Web application deployment.
* Mobile application development.
* Support for dynamic sign language gestures.
* Improved recognition accuracy using advanced models.

---

# Applications

* Communication assistance for hearing and speech-impaired individuals.
* Educational platforms for learning sign language.
* Human-computer interaction.
* Accessibility tools.
* Smart assistive systems.
* Healthcare support applications.

---

# Author

**Archita Verma**

B.Tech Computer Science and Engineering

Machine Learning Enthusiast
