#!/bin/bash

# Directory containing the images
DIR="/var/www/html/projects/topline/topline2/assets/img/whatsapp"

# Change to the directory
cd "$DIR" || exit

# Counter for sequential numbering
COUNT=1

# Process each JPEG file (case insensitive)
for file in $(ls | grep -i '\.jpeg$' | sort); do
    # New filename
    newname="img${COUNT}.jpeg"
    
    # Handle potential name conflicts
    while [ -e "$newname" ]; do
        COUNT=$((COUNT + 1))
        newname="img${COUNT}.jpeg"
    done
    
    # Rename the file
    mv -- "$file" "$newname"
    echo "Renamed: $file -> $newname"
    COUNT=$((COUNT + 1))
done

echo "Renamed $((COUNT - 1)) images."
