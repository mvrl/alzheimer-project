# Dynamic Image for AD MRI Classification
This is the PyTorch implementation of the ECCV 2020 workshop paper "Dynamic Image for 3D MRI Image Alzheimer's Disease Classification". [[paper]](https://arxiv.org/abs/2012.00119)

**Authors:** Xin Xing, Gongbo Liang, Hunter Blanton, M. Usman Rafique, Chris Wang, Ai-Ling Lin, and Nathan Jacobs

The dynamic image Python script is adapted from [tcvrick/dynamic-images-for-action-recognition](https://github.com/tcvrick/dynamic-images-for-action-recognition/).

Official Dynamic Image repository: [hbilen/dynamic-image-nets](https://github.com/hbilen/dynamic-image-nets).

**Corresponding author:** Xin Xing (xtremexing@gmail.com)

The dataset is collected from [ADNI](https://adni.loni.usc.edu/), which is a public website. Here is the [link](https://drive.google.com/drive/folders/1BrJKf7Zy-_TYVPXOl58icR4aOeC-vOY9?usp=drive_link) to the data used in our work.

## Citation

If you find this work useful, please cite:

```bibtex
@misc{xing2020dynamic,
  title         = {Dynamic Image for 3D MRI Image Alzheimer's Disease Classification},
  author        = {Xin Xing and Gongbo Liang and Hunter Blanton and M. Usman Rafique and Chris Wang and Ai-Ling Lin and Nathan Jacobs},
  year          = {2020},
  eprint        = {2012.00119},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CV},
  url           = {https://arxiv.org/abs/2012.00119}
}
```

## Environment Setup

### Option A — Conda (recommended)

```bash
conda env create -f environment.yml
conda activate alzheimer-project
```

### Option B — pip

```bash
pip install -r requirements.txt
```

> **Note:** For GPU support, install PyTorch with the appropriate CUDA toolkit from [pytorch.org](https://pytorch.org/get-started/locally/) before running the commands above.

## Prerequisites
* [Python 3.8+](https://www.python.org/)
* [PyTorch ≥ 1.7](https://pytorch.org/)
* [torchvision ≥ 0.8](https://pytorch.org/vision/)
* [NumPy](https://numpy.org/)
* [scikit-learn](https://scikit-learn.org/)
* [tqdm](https://tqdm.github.io/)
* [Matplotlib](https://matplotlib.org/)
* [OpenCV (opencv-python)](https://pypi.org/project/opencv-python/)
* [NiBabel](https://nipy.org/nibabel/)
* [SimpleITK](https://simpleitk.org/)

## MRI Image Samples
![MRI samples](https://raw.githubusercontent.com/mvrl/alzheimer-project/master/Dynamic%2BAttention%20for%20AD%20MRI%20classification/imgs/MRI_samples.png)

## Workflow
![Workflow](https://raw.githubusercontent.com/mvrl/alzheimer-project/master/Dynamic%2BAttention%20for%20AD%20MRI%20classification/imgs/workflow.png)

## Data
Please save the MRI `.npy` data into `CN` and `AD` folders, respectively. You can use `ADNI2_MRI_AD_niiData.ipynb` (or `ADNI2_MRI_CN_niiData.ipynb`) to convert `.nii` files to `.npy`.

## Implementation

The first step is train/test file splitting. We use 5-fold cross-validation. Run `train_test_files_split.ipynb` to randomly split the data into 5 folds (remember to update your data path). The expected folder layout is shown below:

![Data layout](https://raw.githubusercontent.com/mvrl/alzheimer-project/master/Dynamic%2BAttention%20for%20AD%20MRI%20classification/imgs/data.png)

Then run `Dynamic_image_Vgg11.ipynb`. Remember to update `LABEL_PATH` to your local data path:

```python
LABEL_PATH = '/path/to/your/Preprocessed/ADNI2_MRI'
```

## Results

![Results table](https://raw.githubusercontent.com/mvrl/alzheimer-project/master/Dynamic%2BAttention%20for%20AD%20MRI%20classification/imgs/result.png)

![Runtime comparison](https://raw.githubusercontent.com/mvrl/alzheimer-project/master/Dynamic%2BAttention%20for%20AD%20MRI%20classification/imgs/time.png)
