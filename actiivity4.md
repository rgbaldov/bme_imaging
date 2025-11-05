# Activity 4: Programming with HU using Lung CT Slice

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**  

## Introduction
Computed Tomography (CT) images store pixel values in **Hounsfield Units (HU)**.  
HU allows identification of tissue density:
- Air ≈ -1000 HU  
- Fat ≈ -120 to -60 HU  
- Soft tissue ≈ 20 to 80 HU  
- Bone ≈ 200 to 2000 HU  

In this activity, you will work with a real structured HU dataset from a lung CT slice and write Python code to classify tissues based on HU values.

### Activity Files (Required)
| File | Description |
|------|-------------|
| `lung_hu_slice.npy` | HU matrix of a Lung CT slice |
| `HU_CT_activity.ipynb` | Starter notebook |

## Learning Objectives
After this lab, you should be able to:
1. Load medical image HU data using python.  
2. Visualize CT HU values using matplotlib.  
3. Interpret pixel HU values in relation to real tissues.  
4. Apply conditional logic to classify approximate tissue type based on HU.

## Materials Needed
- Python (Jupyter Notebook / Colab)  
- numpy  
- matplotlib  

## Procedure
1. Load the HU lung slice (`.npy` file) into python using numpy.  
2. Display the HU slice using `imshow`.  
3. Create a function that accepts HU value and returns the most likely tissue category.  
4. Let the user click a coordinate (or manually input x,y pixel) → show HU + classification.  
5. Plot a histogram of HU values.  
6. Observe which range of HU values dominate lung CT slice.

## Programming Tasks
1. Load dataset → `np.load("lung_hu_slice.npy")`
2. Print image shape and min/max HU.
3. Visualize the HU matrix with matplotlib.
4. Write `classify_tissue(hu)` that returns one of:
   - “Air”
   - “Fat”
   - “Soft Tissue”
   - “Bone”
5. Ask user to enter pixel coordinate (row, column), read HU at that location, classify it.
6. Generate HU histogram of entire slice.

## Expected Output
- Image visualization (grayscale)
- HU histogram graph  
- Text classification of user selected HU value  
- Short notes on what type of HU dominates lung region and why.

## Submission Format
Submit the `.ipynb` file with:
- Screenshots of image + histogram  
- 2–3 paragraph reflection:  
  - What did you learn about HU meaning?  
  - Why is HU critical in medical AI / segmentation / diagnostics?  
  - Which tissue category is most dominant in lung CT?
