# Individual Project - Tian Morley

## Repository Structure

### `.github/workflows/`
Contains GitHub Actions YAML files used for automating tests, preprocessing, and training pipelines. 

### `Local_development/`
Scripts and utilities that were developed and tested locally. This includes core data processing scripts such as noise injection, resolution adjustment, and dataset splitting. These were the foundation for validating preprocessing pipelines prior to their use in cloud-based training.

### `VMambaTM/`
Contains the implementation and configuration of the **VMambaTM** model architecture. 

### `actionfiles/`
Linux-adapted versions of selected scripts from the `Local_development/` folder, tailored specifically for execution within GitHub Actions workflows. These ensure compatibility across OS environments.

##  Documentation

Further details about the design, rationale, and technical decisions are provided in the accompanying report. Each folder also includes its own `README.md` for specific documentation and usage.

##  Usage

To clone the repository and begin working:
```bash
git clone https://github.com/uol-feps-soc-comp3931-project-2425/individual-project-TianMorley.git
