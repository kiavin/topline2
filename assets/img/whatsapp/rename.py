import os
import re
from pathlib import Path

# Directory containing the images
directory = "/var/www/html/projects/topline/topline2/assets/img/whatsapp"

# Get all WhatsApp JPEG files and sort them by timestamp
def get_sorted_whatsapp_images(directory):
    files = []
    for f in os.listdir(directory):
        if f.lower().endswith('.jpeg') and f.startswith('WhatsApp Image'):
            # Extract timestamp for sorting
            date_part = re.search(r'(\d{4}-\d{2}-\d{2}) at (\d+\.\d+\.\d+)', f)
            if date_part:
                files.append((date_part.group(1) + date_part.group(2).replace('.', ''), f))
    
    # Sort by timestamp then by filename (for duplicates)
    files.sort(key=lambda x: x[0])
    return [f[1] for f in files]

image_files = get_sorted_whatsapp_images(directory)

# Rename sequentially
for index, filename in enumerate(image_files, start=1):
    old_path = os.path.join(directory, filename)
    new_filename = f"img{index}.jpeg"
    new_path = os.path.join(directory, new_filename)
    
    # Ensure no overwrite
    while os.path.exists(new_path):
        index += 1
        new_filename = f"img{index}.jpeg"
        new_path = os.path.join(directory, new_filename)
    
    os.rename(old_path, new_path)
    print(f"Renamed: '{filename}' → '{new_filename}'")

print(f"Successfully renamed {len(image_files)} WhatsApp images.")
