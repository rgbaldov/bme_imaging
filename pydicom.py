import pydicom
from pydicom.data import get_testdata_file

# Load the verified built-in CT slice
filepath = get_testdata_file("CT_small.dcm")

ds = pydicom.dcmread(filepath)
print(f"File successfully loaded from: {filepath}")
