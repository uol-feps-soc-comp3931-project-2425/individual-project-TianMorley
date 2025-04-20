#  Project Files Overview

This repository contains all files developed locally that contributed to the project.

###  Core Scripts

1. **`noise.py`**  
   Adds Gaussian noise to images.

2. **`lowres.py`**  
   Downsamples images to simulate lower resolution.

3. **`filecount.py`**  
   Used for validating image counts after different preprocessing steps.

4. **`foldersplit.py`**  
   Splits the original dataset into training/validation/test splits for the project.



###  GitHub Actions

There are additional folders (e.g., `.github/workflows/`, `actionfiles/`) with their own `README` files. These contain automation scripts and workflows used to preprocess the data through GitHub Actions.

In summary, these workflows handle:
- Downloading the dataset from Hugging Face
- Running the preprocessing scripts (`noise.py`, `lowres.py`)
- Uploading the processed datasets back to Hugging Face

