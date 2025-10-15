# Ultrasound DICOM — Quick Guide
> A concise technical reference on handling, storing, and working with ultrasound DICOM data.

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**  

## Table of contents
1. [Introduction](#introduction)
2. [DICOM basics for ultrasound](#dicom-basics-for-ultrasound)
3. [Important DICOM attributes (common for US)](#important-dicom-attributes-common-for-us)
4. [Multiframe (CINE) and compound objects](#multiframe-cine-and-compound-objects)
5. [Structured Reporting (DICOM SR) for ultrasound](#structured-reporting-dicom-sr-for-ultrasound)
6. [Transfer syntaxes & compression considerations](#transfer-syntaxes--compression-considerations)
7. [Interoperability & PACS integration](#interoperability--pacs-integration)
8. [De-identification & privacy checklist](#de-identification--privacy-checklist)
9. [Common tools & libraries](#common-tools--libraries)
10. [Practical examples (pydicom snippets)](#practical-examples-pydicom-snippets)
11. [QA checklist & best practices](#qa-checklist--best-practices)
12. [References & further reading](#references--further-reading)

## Introduction
Ultrasound (modality `US`) DICOM files store both single-frame images and multiframe cine loops, plus metadata required for clinical use and PACS workflows. Ultrasound has modality-specific metadata (probe info, acquisition settings, measurements) and often uses DICOM Structured Reporting (SR) to record measurements and annotations.

## DICOM basics for ultrasound
- **Modality**: `US` (Ultrasound).
- **Instances**: can be single-frame images (JPEG/RAW) or **multiframe** (cine) encapsulating many frames in one DICOM object.
- **Presentation states**: annotations and overlays may be stored as Presentation State objects or burned-in to pixel data.
- **SR**: Measurement results and exam reports can be encoded as DICOM SR (eg. TID 1500 templates or cardiology-specific SR templates).

## Important DICOM attributes (common for US)
- (0008,0060) Modality (`US`)
- (0010,0010) PatientName (PHI — de-id as needed)
- (0008,0020) StudyDate (YYYYMMDD)
- (0008,1030) StudyDescription (Exam name)
- (0008,0060) Manufacturer (Probe vendor)
- (0018,5100) PatientPosition (e.g. SUPINE)
- (0028,0010) Rows (Image height)
- (0028,0011) Columns (Image width)
- (0028,0002) SamplesPerPixel (1-grayscale or 3-RGB)
- (7FE0,0010) PixelData (Encoded pixel frames)
- (0020,000D) StudyInstanceUID
- (0020,000E) SeriesInstanceUID

Include modality-specific private tags from vendors when needed; these vary and are vendor-specific.

## Multiframe (CINE) and compound objects
- Multiframe DICOM stores many frames in a single instance using frame functional groups and per-frame functional group sequences.
- For ultrasound cine loops, check `NumberOfFrames`, `FrameTime`, and per-frame `FrameDelay` details.
- Consider storing long cine as multiple series if file/transfer size becomes unwieldy.

## Structured Reporting (DICOM SR) for ultrasound
- Use SR to encode measurements (lengths, areas, volumes) and observations in a machine-readable way.
- Cardiology and OB/GYN often use standardized templates (e.g., IHE or manufacturer templates).
- SR objects reference images by `ReferencedImageSequence` to tie measurements to frames.

## Transfer syntaxes & compression considerations
- Lossless (`JPEG-LS`, `JPEG2000 Lossless`) recommended for diagnostic images.
- Some ultrasound workflows use lossy compression (JPEG) for storage savings — ensure clinical policy permits it.
- When exchanging with PACS, verify supported transfer syntaxes and negotiate implicit/explicit VR and byte order.

## Interoperability & PACS integration
- Verify `SCP/SCU` roles when pushing to PACS: verify Study/Series UIDs, Accession Number mapping, and patient demographics.
- Use DICOM C-STORE to send images and C-FIND/C-MOVE for retrieval.
- Consider DICOMweb (WADO-RS, QIDO-RS, STOW-RS) for modern REST-based integrations.

## De-identification & privacy checklist
- Remove or replace patient-identifying tags (PatientName, PatientID, DOB, InstitutionName) according to policy.
- Carefully handle burned-in annotations — optical character recognition may be required to identify PHI in pixels.
- Maintain a mapping table for re-identification if required by study workflows.

## Common tools & libraries
- **pydicom** — read/write/manipulate DICOM in Python.
- **GDCM** / **dcmtk** — C++ libraries and command-line tools (dcmj2pnm, dcmdump).
- **Orthanc** — lightweight PACS with DICOMweb support.
- **OHIF Viewer** — web viewer that supports ultrasound cine viewing with DICOMweb.
- **ImageJ/FIJI** — generic image analysis; plugins exist for DICOM.

## Practical examples (pydicom snippets)
```python
# Read basic DICOM and inspect
import pydicom
ds = pydicom.dcmread('ultrasound.dcm')
print(ds.Modality, ds.StudyDate, getattr(ds, 'NumberOfFrames', 1))

# Access pixel array (requires numpy)
arr = ds.pixel_array  # may raise if compressed; use pydicom + GDCM/JPEG2000 support
print(arr.shape)

# Save first frame as PNG
from PIL import Image
frame0 = ds.pixel_array[0]
Image.fromarray(frame0).save('frame0.png')
```

## QA checklist & best practices
- Confirm modality tag == `US` and `ManufacturerModelName` matches expected device.
- Validate `NumberOfFrames`, `FrameTime`, and image orientation when reconstructing cine.
- Check SR references to ensure measurements link to correct image frames.
- Use lossless compression for diagnostic archiving unless policy allows otherwise.

## References & further reading
- DICOM Standard (Part 3 - Information Object Definitions, Part 6 - Data Dictionary, Part 8 - Network Services)
- pydicom documentation
- Orthanc documentation (for PACS integration)
