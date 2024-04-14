#!/bin/bash
chmod +x file_cd.sh
# Create three folders: folder_name_1, folder_name_2, folder_name_3
mkdir folder_name_1 folder_name_2 folder_name_3

# Navigate into folder_name_1
cd folder_name_1 || exit

# Create three subfolders: Foldname1, Foldname2, Foldname3
mkdir Foldname1 Foldname2 Foldname3

# Delete Foldname2 and Foldname3
rm -r Foldname2 Foldname3

echo "Script completed successfully."

