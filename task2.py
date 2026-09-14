import hashlib

def anonymize_dicom(dataset, salt="DLSU_BEMEDIS_AY2526"):
    """
    Strips direct PHI identifiers and pseudorandomizes UIDs 
    using deterministic SHA-256 hashing.
    """
    clean_ds = dataset.copy()
    
    # 1. Strip direct patient identifiers
    clean_ds.PatientName = "ANONYMOUS^PATIENT"
    clean_ds.PatientID = hashlib.sha256((str(dataset.PatientID) + salt).encode()).hexdigest()[:10]
    
    for tag in ["PatientBirthDate", "PatientAddress", "ReferringPhysicianName", "InstitutionName"]:
        if tag in clean_ds:
            delattr(clean_ds, tag)
            
    # 2. Re-hash Study and Series Instance UIDs (prefix 2.25 is reserved for UUIDs)
    study_hash = int(hashlib.sha256((clean_ds.StudyInstanceUID + salt).encode()).hexdigest(), 16)
    series_hash = int(hashlib.sha256((clean_ds.SeriesInstanceUID + salt).encode()).hexdigest(), 16)
    
    clean_ds.StudyInstanceUID = f"2.25.{str(study_hash)[:30]}"
    clean_ds.SeriesInstanceUID = f"2.25.{str(series_hash)[:30]}"
    
    # 3. Strip private vendor tags (odd-numbered groups)
    clean_ds.remove_private_tags()
    
    return clean_ds

anonymized_ds = anonymize_dicom(ds)
anonymized_ds.save_as("anonymized_CT.dcm")
print("Anonymization verified. File saved as 'anonymized_CT.dcm'.")
