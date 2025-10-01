# Advanced DICOM Python Exercises

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**  

This document provides advanced exercises for working with DICOM images using Python. It covers pixel value conversion, 3D reconstruction, ROI measurement, anonymization, and radiomics.

## **Exercise 1 – Convert Pixel Data to Hounsfield Units (HU)**
Essential for CT images where raw pixel values must be rescaled.

```python
import pydicom
import matplotlib.pyplot as plt

# Load CT DICOM slice
ds = pydicom.dcmread("ct_slice.dcm")

# Extract pixel data
img = ds.pixel_array.astype(float)

# Convert to Hounsfield Units
intercept = ds.RescaleIntercept
slope = ds.RescaleSlope
hu_img = img * slope + intercept

# Plot different windowing (lung, soft tissue, bone)
def window_image(img, center, width):
    img_min = center - width // 2
    img_max = center + width // 2
    img_windowed = img.copy()
    img_windowed[img_windowed < img_min] = img_min
    img_windowed[img_windowed > img_max] = img_max
    return img_windowed

plt.figure(figsize=(12,4))
plt.subplot(1,3,1); plt.imshow(window_image(hu_img, -600, 1500), cmap="gray"); plt.title("Lung")
plt.subplot(1,3,2); plt.imshow(window_image(hu_img, 40, 400), cmap="gray"); plt.title("Soft Tissue")
plt.subplot(1,3,3); plt.imshow(window_image(hu_img, 500, 2000), cmap="gray"); plt.title("Bone")
plt.show()
```

## **Exercise 2 – 3D Volume Reconstruction from Series**
Stack multiple DICOM slices into a 3D array.

```python
import os
import numpy as np
import pydicom
import matplotlib.pyplot as plt

# Folder with DICOM series
folder = "CT_series/"
files = [pydicom.dcmread(os.path.join(folder, f)) for f in os.listdir(folder)]

# Sort slices by ImagePositionPatient (z-axis)
files.sort(key=lambda x: float(x.ImagePositionPatient[2]))

# Stack into 3D volume
volume = np.stack([f.pixel_array for f in files], axis=0)

print("Volume shape:", volume.shape)

# Show axial, coronal, sagittal slice
plt.figure(figsize=(12,4))
plt.subplot(1,3,1); plt.imshow(volume[volume.shape[0]//2,:,:], cmap="gray"); plt.title("Axial")
plt.subplot(1,3,2); plt.imshow(volume[:,volume.shape[1]//2,:], cmap="gray"); plt.title("Coronal")
plt.subplot(1,3,3); plt.imshow(volume[:,:,volume.shape[2]//2], cmap="gray"); plt.title("Sagittal")
plt.show()
```

## **Exercise 3 – ROI Measurement in cm²**
Draw a rectangle ROI and measure mean HU + area.

```python
import cv2
import numpy as np
import math

# Load a CT slice
ds = pydicom.dcmread("ct_slice.dcm")
img = ds.pixel_array.astype(float) * ds.RescaleSlope + ds.RescaleIntercept
img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
clone = img.copy()

# Pixel spacing (mm per pixel) → convert to cm
px_spacing = [float(x) for x in ds.PixelSpacing]
px_area_cm2 = (px_spacing[0]/10) * (px_spacing[1]/10)

roi_pts = []
def draw_roi(event, x, y, flags, param):
    global roi_pts, img
    if event == cv2.EVENT_LBUTTONDOWN:
        roi_pts = [(x,y)]
    elif event == cv2.EVENT_LBUTTONUP:
        roi_pts.append((x,y))
        x0,y0 = roi_pts[0]
        cv2.rectangle(img, roi_pts[0], roi_pts[1], (255,0,0), 2)
        
        # Crop ROI
        roi = clone[min(y0,y):max(y0,y), min(x0,x):max(x0,x)]
        
        # Mean HU
        mean_val = np.mean(roi)
        
        # Area
        h, w = roi.shape
        area_cm2 = h*w*px_area_cm2
        
        cv2.putText(img, f"HU: {mean_val:.1f}, Area: {area_cm2:.2f} cm^2",
                    (x0, y0-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
        cv2.imshow("DICOM ROI", img)

cv2.imshow("DICOM ROI", img)
cv2.setMouseCallback("DICOM ROI", draw_roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## **Exercise 4 – DICOM Anonymization**
Remove PHI and save new file.

```python
import pydicom

ds = pydicom.dcmread("patient.dcm")

# Remove sensitive tags
tags_to_remove = ["PatientName", "PatientID", "PatientBirthDate", "PatientSex"]
for tag in tags_to_remove:
    if tag in ds:
        ds.data_element(tag).value = "ANONYMIZED"

ds.save_as("anonymized.dcm")
```

## **Exercise 5 – Radiomics Feature Extraction**
Using `pyradiomics` for texture features.

```python
from radiomics import featureextractor

# Extract features
extractor = featureextractor.RadiomicsFeatureExtractor()
features = extractor.execute("ct_slice.dcm", "roi_mask.nii.gz")

# Print a few
for k,v in list(features.items())[:10]:
    print(k, v)
```
