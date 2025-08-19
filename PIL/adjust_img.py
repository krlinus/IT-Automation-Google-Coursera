#!/usr/bin/env python3
import os, sys
from PIL import Image

def make_edits(input_file, output_dir):
    """
    Adjusts an image by rotating, resizing, and converting it to JPEG format.
    Saves the adjusted image to the specified output directory.
    
    Args:
        input_file (str): Path to the input image file.
        output_dir (str): Path to the directory where adjusted images will be saved.
    
    Raises:
        Exception: If the input file cannot be opened or processed.
    """
    
    with Image.open(input_file) as im:
        im = im.rotate(-90)
        im = im.resize((128, 128))
        im = im.convert("RGB")
        base_filename = os.path.basename(input_file)
        im.save(os.path.join(output_dir, base_filename.split('.')[0] + '.jpeg'))

def drive_edits(input_dir, output_dir):
    """
    validates the input and output directories.
    Sets up call to make_edits for each image in the input directory.

    Args:
        input_dir (str): Path to the directory containing input images.
        output_dir (str): Path to the directory where adjusted images will be saved.
    """
    if not os.path.exists(input_dir):
        raise ValueError(f"Input directory '{input_dir}' does not exist.")
    
    if len(os.listdir(input_dir)) <= 2:
        print(f"Input directory '{input_dir}' is empty")
        return
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
            
    for filename in os.listdir(input_dir):
        if filename[0] == '.':
            continue
        
        try:
            make_edits(os.path.join(input_dir,filename), output_dir)
        except Exception as e:
            print(f"Failed to process {filename}: {e}")
            sys.exit(1)
         

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <input_dir> <output_dir>")
        sys.exit(1)
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    try:
        drive_edits(input_dir, output_dir)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    print("Image processing completed successfully.")
