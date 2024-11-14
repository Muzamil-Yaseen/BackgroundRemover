# BackgroundRemover
This repository provides a Python-based tool for batch removing backgrounds from images using the rembg library and Pillow. The script automatically processes images in the input_images folder and saves the output in output_images, allowing for streamlined background removal in a variety of formats.
# Features:
Batch Processing: Processes images in batches to optimize performance, with multithreading for faster processing.
Format Flexibility: Supports various input formats (JPEG, PNG, TIFF, BMP, and WebP) and outputs images in customizable formats.
Automatic Dependency Management: Checks and installs any missing packages (rembg and Pillow), ensuring a smooth setup.
Quality Control: Allows adjustment of output quality, especially useful for lossy formats like JPEG.
# Folder and File Structure:
# input_images/: Place images here that need background removal processing.
# output_images/: Processed images with backgrounds removed will be saved here.
# BGremove.py: Main Python script for background removal.
# requirements.txt: Lists dependencies. You can run pip install -r requirements.txt for manual installation if needed.
