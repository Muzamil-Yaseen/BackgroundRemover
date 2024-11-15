# BackgroundRemover

This repository offers a Python-based tool for batch removing backgrounds from images using the `rembg` library and `Pillow`. The script processes images stored in the `input_images` folder, saving the background-free versions in the `output_images` folder. It is designed to streamline the process of background removal across multiple image formats.

## Features:
- **Batch Processing**: Handles images in batches to improve performance with multithreaded execution for faster processing.
- **Format Flexibility**: Supports various image formats (JPEG, PNG, TIFF, BMP, and WebP) and provides options for customized output formats.
- **Automatic Dependency Management**: Checks for and installs missing packages (`rembg` and `Pillow`), ensuring hassle-free setup.
- **Quality Control**: Offers adjustable quality settings for output images, particularly beneficial for lossy formats like JPEG.

## Folder and File Structure:
- **input_images/**: Folder for images that need background removal.
- **output_images/**: Folder where processed, background-free images are saved.
- **BGremove.py**: Primary Python script for background removal operations.
- **requirements.txt**: List of required dependencies. Run `pip install -r requirements.txt` for a manual installation of dependencies if needed.

## Installation

### Clone the Repository

To clone this repository, run the following command:

```bash
git clone https://github.com/Muzamil-Yaseen/BackgroundRemover.git

```
To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt

```


