# Hounsfield Units (HU)

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**  

## What are Hounsfield Units?

Hounsfield Units (HU) are a standardized numerical scale used in **Computed Tomography (CT)** to represent the density of tissues based on how much the X-ray beam is attenuated when it passes through the body.

Every pixel in a CT image has an HU value.

## Why do we need HU?

- To quantify tissue density
- To compare tissue values across different scanners and protocols
- To differentiate tissues (bone vs fat vs soft tissue vs fluid)
- To help detect pathology (edema, hemorrhage, calcification, lesions)

## Formula

\[
HU = \frac{\mu_{tissue} - \mu_{water}}{\mu_{water} - \mu_{air}} \times 1000
\]

Where:
- μ = attenuation coefficient
- Water HU = **0**
- Air HU = **-1000**

## Typical Hounsfield Ranges

| Tissue / Material | HU Range |
|------------------|-----------|
| Air | -1000 |
| Lung | -700 to -500 |
| Fat | -120 to -80 |
| Water | 0 |
| Soft tissue | +20 to +60 |
| Muscle | +40 |
| Blood (fresh) | +60 |
| Bone | +700 to +3000 |
| Metal / contrast | >2000 |

## Clinical Use Cases

| Clinical Example | How HU Helps |
|------------------|--------------|
| Stroke CT | Differentiate ischemic vs hemorrhagic stroke (blood higher HU) |
| Oncology | Detect calcified lesion vs soft tumor |
| Lung CT | COPD emphysema quantification uses HU thresholds |
| Kidney | Differentiate cyst (<20 HU) vs solid tumor (>30 HU) |
| Bone density | Osteoporosis evaluation, cortical bone HU analysis |

## Why HU is powerful in Analytics + ML / AI

- Converts imaging into **quantitative structured data**
- Used as features for segmentation, clustering, classification
- Enables reproducible threshold-based image masks (ex. bone threshold >300 HU)

### Example pipeline

1. Determine HU thresholds  
2. Segment target organ/tissue  
3. Extract radiomics features  
4. Train model for classification / detection

---

## Summary

Hounsfield Units turn CT grayscale into **true measurable values**.  
They are critical for objective radiologic interpretation, quantitative imaging, automated segmentation, and AI-based diagnostic systems.
