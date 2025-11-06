# Programming Activity: ML in Medical Imaging

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)** 

# Machine Learning in Medical Imaging

## Table of Contents
1. [Introduction](#introduction)
2. [Medical Imaging Modalities](#medical-imaging-modalities)
3. [Machine Learning Overview](#machine-learning-overview)
4. [Applications in Medical Imaging](#applications-in-medical-imaging)
5. [Data Preparation](#data-preparation)
6. [Feature Extraction](#feature-extraction)
7. [Model Selection](#model-selection)
8. [Evaluation Metrics](#evaluation-metrics)
9. [Sample Python Program](#sample-python-program)
10. [Challenges and Limitations](#challenges-and-limitations)
11. [Future Trends](#future-trends)
12. [References](#references)

---

## Introduction
Machine learning (ML) has revolutionized the field of medical imaging, enabling automated diagnosis, improved detection accuracy, and personalized treatment planning. ML algorithms can analyze complex imaging data from modalities like CT, MRI, X-ray, and Ultrasound, assisting radiologists in decision-making.

---

## Medical Imaging Modalities
Common imaging modalities used in ML applications:

- **X-ray**: Quick, low-cost imaging, primarily for bone fractures, chest imaging.
- **CT (Computed Tomography)**: Cross-sectional imaging for detailed anatomical assessment.
- **MRI (Magnetic Resonance Imaging)**: Soft tissue contrast for brain, spinal cord, and joints.
- **Ultrasound**: Real-time imaging, used in obstetrics and organ evaluation.
- **PET (Positron Emission Tomography)**: Functional imaging, often combined with CT/MRI.

---

## Machine Learning Overview
### Types of Machine Learning
- **Supervised Learning**: Models are trained using labeled data (e.g., disease vs. no disease).
- **Unsupervised Learning**: Models identify patterns in unlabeled data (e.g., clustering tumor types).
- **Reinforcement Learning**: Models learn optimal actions via rewards and penalties, often used in robotic surgery.

### Popular Algorithms in Medical Imaging
- Convolutional Neural Networks (CNNs)
- Support Vector Machines (SVMs)
- Random Forests
- K-Nearest Neighbors (KNN)
- Autoencoders for feature extraction

---

## Applications in Medical Imaging
- **Tumor Detection & Segmentation**: Identifying and outlining tumors in MRI/CT scans.
- **Disease Classification**: Detecting pneumonia, COVID-19, Alzheimer’s, etc.
- **Image Enhancement**: Noise reduction and super-resolution imaging.
- **Organ & Tissue Segmentation**: Automating contouring in radiotherapy planning.
- **Predictive Analytics**: Prognosis and treatment response prediction.

---

## Data Preparation
1. **Data Acquisition**: Collect imaging data from hospitals, public datasets (e.g., NIH Chest X-ray, BraTS, LIDC-IDRI).
2. **Annotation**: Labeling of images by radiologists.
3. **Preprocessing**:
    - Normalization (e.g., Hounsfield Units for CT)
    - Resizing and cropping
    - Denoising and artifact removal
    - Data augmentation (flipping, rotation, intensity scaling)

---

## Feature Extraction
- **Manual Features**:
    - Shape, texture, intensity
    - Statistical measures (mean, variance)
- **Automatic Features**:
    - CNN-based feature maps
    - Pretrained models (ResNet, VGG, DenseNet) for transfer learning

---

## Model Selection
- Choose algorithms based on:
    - Problem type (classification, segmentation, detection)
    - Dataset size
    - Computational resources
- Examples:
    - **Classification**: CNN, DenseNet
    - **Segmentation**: U-Net, Mask R-CNN
    - **Detection**: Faster R-CNN, YOLO

---

## Evaluation Metrics
- **Classification**:
    - Accuracy, Precision, Recall, F1-score
    - ROC-AUC
- **Segmentation**:
    - Dice coefficient
    - Intersection over Union (IoU)
- **Detection**:
    - Mean Average Precision (mAP)
    - Sensitivity & Specificity

---

## Sample Python Program
Below is a **sample CNN program** to classify medical images (tumor vs. normal) using `TensorFlow` and `Keras`.

```python
# Import Libraries
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Data Preprocessing
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

train_data = train_datagen.flow_from_directory(
    'dataset/',  # Folder containing 'tumor' and 'normal' subfolders
    target_size=(128, 128),
    batch_size=32,
    class_mode='binary',
    subset='training'
)

val_data = train_datagen.flow_from_directory(
    'dataset/',
    target_size=(128, 128),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)

# Build CNN Model
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Conv2D(128, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')  # Binary classification
])

# Compile Model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train Model
history = model.fit(train_data, validation_data=val_data, epochs=10)

# Evaluate Model
loss, accuracy = model.evaluate(val_data)
print(f'Validation Accuracy: {accuracy*100:.2f}%')
