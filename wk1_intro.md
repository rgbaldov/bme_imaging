# 📑 Introduction to Biomedical Imaging & DICOM  
*CT/MRI Visualization in Python*  
---

## 🧪 1. Biomedical Imaging Overview  
- **Modalities:** X-ray, CT, MRI, Ultrasound, PET  
- **Applications:** diagnosis, surgical planning, disease monitoring  
- **Key Idea:** Images are digitized for storage, sharing, and AI analysis  
---

## 📂 2. What is DICOM?  
- **Digital Imaging and Communications in Medicine** standard  
- Stores both:  
  - **Image data** (CT/MRI slices)  
  - **Metadata** (patient info, modality, slice position)  
- Used in hospitals, PACS, and research labs  
---

## 🗂️ 3. DICOM File Structure  
- **Header:** metadata (patient ID, study date, scanner settings)  
- **Pixel data:** actual medical image  
- **Series of slices:** combined into 3D volume  
---

## 🐍 4. Python Tools for DICOM  
- `pydicom` → read metadata & images  
- `matplotlib` → visualize slices  
- `SimpleITK` / `nibabel` → handle 3D volumes  
---

## 🖼️ 5. Sample Code: Load & Display CT/MRI Slice  

```python
import pydicom
import matplotlib.pyplot as plt

# Load a DICOM file
dcm = pydicom.dcmread("sample.dcm")

# Show metadata
print(dcm.PatientName, dcm.Modality, dcm.StudyDate)

# Display the image
plt.imshow(dcm.pixel_array, cmap='gray')
plt.title("CT/MRI Slice")
plt.axis("off")
plt.show()
