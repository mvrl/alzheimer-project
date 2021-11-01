# Dynamic image for AD MRI classification
This is the Pytorch implementation of the ECCV 2020 worshop paper "Dynamic Image for 3D MRI Image Alzheimer's Disease Classification". [paper](https://arxiv.org/abs/2012.00119)

Authors:Xin Xing, Gongbo Liang, Hunter Blanton, M. Usman Rafique, Chris Wang, Ai-Ling Lin, and Nathan Jacobs 

The dynamic image python script is refered by [this](https://github.com/tcvrick/dynamic-images-for-action-recognition/).

Offical Dynamic image link is [here](https://github.com/hbilen/dynamic-image-nets).

Corresponding author: Xin Xing (xxi242@g.uky.edu)

## Prerequisites
* [Python3](https://www.python.org/)
* [Pytorch](https://pytorch.org/)
* [NiBabel](https://nipy.org/nibabel/)


## MRI image samples:
![](https://github.com/UkyVision/alzheimer-project/blob/master/Dynamic%2BAttention%20for%20AD%20MRI%20classification/imgs/MRI_samples.png)

## Workflow:
![](https://github.com/UkyVision/alzheimer-project/blob/master/Dynamic%2BAttention%20for%20AD%20MRI%20classification/imgs/workflow.png)

## Data:
Please save the MRI ".npy" data into CN and AD folders, respectively. You can use the "ADNI2_MRI_AD_niiData.ipynb" to convert the ".nii" file to ".npy" file.


## Implementation:
The first operation is train-test files spliting. We are working on the 5-fold cross validation. So we use the "train_test_files_split.ipynb" to randomly split the 
data into 5 folders (Remember to change your data path). As following: 

![](https://github.com/UkyVision/alzheimer-project/blob/master/Dynamic%2BAttention%20for%20AD%20MRI%20classification/imgs/data.png)

Then we can conduct the "Dynamic_image_Vgg11.ipynb" (Remember to change <font color="red">LABEL_PATH = '/data/scratch/xxing/adni_dl/Preprocessed/ADNI2_MRI'</font> to your data path). 

## Results:

![](https://github.com/UkyVision/alzheimer-project/blob/master/Dynamic%2BAttention%20for%20AD%20MRI%20classification/imgs/result.png)

![](https://github.com/UkyVision/alzheimer-project/blob/master/Dynamic%2BAttention%20for%20AD%20MRI%20classification/imgs/time.png)
