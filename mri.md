# Magnetic Resonance Imaging (MRI)

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**  

## 1. Introduction
Magnetic Resonance Imaging (MRI) is a **non-invasive imaging technique** used to visualize detailed internal structures of the body. It provides high-contrast images of soft tissues, making it a critical tool in **neurology, musculoskeletal imaging, and oncology**.
MRI uses **strong magnetic fields** and **radiofrequency (RF) pulses** to excite hydrogen nuclei (protons) in the body and detect the resulting signals.

## 2. Basic Principle of MRI

### 2.1 Nuclear Magnetic Resonance (NMR)
MRI is based on the **Nuclear Magnetic Resonance (NMR)** phenomenon, where atomic nuclei with unpaired protons or neutrons (like hydrogen) absorb and re-emit electromagnetic radiation when placed in a magnetic field.
### 2.2 Proton Alignment
When a patient is placed inside the MRI scanner:
- Protons align either **parallel** or **antiparallel** to the main magnetic field (**B₀**).
- The majority align parallel, creating a **net magnetization vector (M₀)**.
### 2.3 Radiofrequency (RF) Excitation
An **RF pulse** at the **Larmor frequency** is applied, tipping the net magnetization away from the longitudinal axis.
\[
\omega = \gamma B_0
\]
where:
- \( \omega \) = Larmor frequency  
- \( \gamma \) = gyromagnetic ratio (42.58 MHz/T for hydrogen)  
- \( B_0 \) = magnetic field strength (in Tesla)

### 2.4 Relaxation Processes
After the RF pulse is turned off, protons return to equilibrium through:
- **T1 Relaxation (Spin-Lattice):** recovery of longitudinal magnetization  
- **T2 Relaxation (Spin-Spin):** decay of transverse magnetization  

## 3. Image Formation
### 3.1 Spatial Encoding
Spatial information is encoded using **magnetic field gradients**:
- **Slice Selection Gradient (Gz)** determines the imaging slice.  
- **Frequency Encoding Gradient (Gx)** maps signal along one axis.  
- **Phase Encoding Gradient (Gy)** maps the orthogonal axis.
### 3.2 K-Space
All signal data are stored in **k-space**, a frequency domain representation.  
Applying the **Fourier Transform (FT)** converts k-space data into the final image.

## 4. MRI Parameters
| Parameter | Description | Controls |
|------------|--------------|-----------|
| TR (Repetition Time) | Time between successive RF pulses | T1 contrast |
| TE (Echo Time) | Time between RF pulse and signal readout | T2 contrast |
| Flip Angle | Angle of rotation of M₀ due to RF pulse | Signal intensity |
| FOV (Field of View) | Spatial coverage of the image | Image size |

## 5. Types of MRI Sequences
### 5.1 Spin Echo (SE)
The most common sequence for T1, T2, and PD-weighted images.
### 5.2 Gradient Echo (GRE)
Faster imaging sequence with shorter TR and TE values.
### 5.3 Inversion Recovery (IR)
Used for better tissue contrast, e.g., **FLAIR (Fluid Attenuated Inversion Recovery)** for brain imaging.

## 6. MRI Contrast Weighting
| Contrast Type | TR | TE | Highlights |
|----------------|----|----|-------------|
| T1-weighted | Short | Short | Fat, anatomy |
| T2-weighted | Long | Long | Fluid, pathology |
| PD-weighted | Long | Short | Proton density differences |

## 7. MRI Safety
### 7.1 Magnetic Field Hazards
- Projectile risk from ferromagnetic materials  
- Interference with **pacemakers or implants**
### 7.2 RF and Gradient Field Hazards
- **RF heating** (SAR limits)
- **Peripheral nerve stimulation**
### 7.3 Acoustic Noise
- Use of **ear protection** recommended due to gradient switching.

## 8. Advanced MRI Techniques
| Technique | Purpose |
|------------|----------|
| fMRI (Functional MRI) | Measures brain activity via blood oxygenation (BOLD) |
| DWI (Diffusion Weighted Imaging) | Detects diffusion of water molecules, useful in stroke imaging |
| DTI (Diffusion Tensor Imaging) | Maps white matter tracts |
| MRS (Magnetic Resonance Spectroscopy) | Analyzes chemical composition |
| MR Angiography (MRA) | Visualizes blood vessels |

## 9. Clinical Applications
- **Neurology:** Brain tumors, stroke, multiple sclerosis  
- **Cardiology:** Myocardial viability, perfusion studies  
- **Musculoskeletal:** Ligament tears, spinal discs  
- **Oncology:** Tumor detection and characterization

## 10. Summary
MRI provides superior soft-tissue contrast without ionizing radiation.  
Understanding **physics principles**, **sequence parameters**, and **safety guidelines** ensures optimal imaging and patient care.

## 11. References
1. Bushberg, J.T. et al. *The Essential Physics of Medical Imaging*. Lippincott Williams & Wilkins.  
2. Haacke, E.M. et al. *Magnetic Resonance Imaging: Physical Principles and Sequence Design.* Wiley.  
3. McRobbie, D.W. et al. *MRI from Picture to Proton.* Cambridge University Press.
