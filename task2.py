import numpy as np
import matplotlib.pyplot as plt

def rescale_to_hu(dataset):
    """Linearly rescales raw stored pixel values to Hounsfield Units."""
    raw_pixels = dataset.pixel_array.astype(np.float64)
    slope = float(getattr(dataset, "RescaleSlope", 1.0))
    intercept = float(getattr(dataset, "RescaleIntercept", 0.0))
    return (raw_pixels * slope) + intercept

def apply_windowing(image_hu, center, width):
    """Clips an HU image to a window range and normalizes to 8-bit grayscale."""
    img_min = center - (width / 2.0)
    img_max = center + (width / 2.0)
    clipped = np.clip(image_hu, img_min, img_max)
    normalized = ((clipped - img_min) / (img_max - img_min)) * 255.0
    return normalized.astype(np.uint8)

hu_image = rescale_to_hu(ds)

# Common CT Diagnostic Windows:
windows = {
    "Soft Tissue Window (C:40, W:400)": (40, 400),
    "Bone Window (C:500, W:2000)": (500, 2000),
    "Lung Window (C:-600, W:1500)": (-600, 1500)
}

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for ax, (title, (c, w)) in zip(axes, windows.items()):
    ax.imshow(apply_windowing(hu_image, c, w), cmap="gray")
    ax.set_title(title)
    ax.axis("off")

plt.tight_layout()
plt.show()
