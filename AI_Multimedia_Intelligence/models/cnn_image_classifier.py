from PIL import Image
import numpy as np

def run_cnn(image_path):
    img = Image.open(image_path).resize((64, 64))
    arr = np.array(img).mean()  # Simulate grayscale processing
    if arr > 100:
        return "Class: Bright Image"
    else:
        return "Class: Dark Image"
