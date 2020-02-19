import sys
import os
from PIL import Image

# Grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#  Check is new/ folder exists, if not create it (make directory)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop to pokedex,
# Convert images to png, /Use splitext() method of os module
# Save into the new folder.
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_file_ext = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_file_ext}.png', 'png')
