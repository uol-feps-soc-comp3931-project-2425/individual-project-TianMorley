This folder includes two GitHub Actions workflows to automate dataset preprocessing:

run.yaml
→ Runs noiselinux.py to add Gaussian noise to all images in the dataset and uploads the result to Hugging Face (gauss_imagewoof).

lowresrun.yaml
→ Runs lowres_linux.py to downsample (simulate low resolution) images and uploads the processed dataset to Hugging Face (lowres_imagewoof).

Both of the workflows download the original dataset which is uploaded to my personal google drive.
These workflows are triggered manually from the Actions tab and use a Hugging Face token stored as HF_TOKEN in repository secrets.
