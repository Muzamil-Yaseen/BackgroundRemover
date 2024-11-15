import os
import io
import subprocess
from rembg import remove
from PIL import Image
from concurrent.futures import ThreadPoolExecutor, as_completed

# Ensure required directories exist
input_folder = 'input_images'
output_folder = 'output_images'
os.makedirs(input_folder, exist_ok=True)  # Create input_images if it doesn't exist
os.makedirs(output_folder, exist_ok=True)  # Create output_images if it doesn't exist

# Install required libraries if they are not present
def install_missing_packages():
    try:
        import rembg
        from PIL import Image
    except ImportError:
        subprocess.check_call(["pip", "install", "rembg", "Pillow"])

install_missing_packages()

# Process a single image to remove the background and save it with the specified format
def process_image(filename, output_format="png", quality=100):
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + f".{output_format}")

    try:
        with open(input_path, 'rb') as input_file:
            img = Image.open(input_file)
            img = remove(img)  # Remove background

            if img.mode != 'RGBA':
                img = img.convert("RGBA")

            img.save(output_path, format=output_format.upper(), quality=quality)
            print(f"Processed {filename} -> {output_path}")
    except Exception as e:
        print(f"Failed to process {filename}: {e}")

# Batch processing function to process all images in the input directory
def process_all_images(batch_size=10, output_format="png", quality=100):
    supported_extensions = (".jpg", ".jpeg", ".png", ".webp", ".tiff", ".bmp")
    images_to_process = [f for f in os.listdir(input_folder) if f.lower().endswith(supported_extensions)]

    for i in range(0, len(images_to_process), batch_size):
        batch = images_to_process[i:i + batch_size]
        print(f"Processing batch {i // batch_size + 1} / {(len(images_to_process) + batch_size - 1) // batch_size}...")

        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = {executor.submit(process_image, filename, output_format, quality): filename for filename in batch}

            for future in as_completed(futures):
                future.result()  # Ensures any exceptions are raised

    print("Processing completed!")

# Run the batch processing function
process_all_images()
