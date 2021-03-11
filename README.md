# HTR_CalamariOCR
![](Images/Trascription_1.png) <br/>
 <br/>
Handwritten Text Recognition using Calamari OCR framework.
## Table of Contents  
- [About the Project](#1)  
  - [Built with](#2)
- [Getting Started](#3)
  - [Prerequsites](#4)
  - [Installation](#5)
  - [Usage](#6)
# About the Project <a name="1"/>
The aim of this work is to replicate the training and testing  pipeline of a neural network about the problem of HTR. <br/>
This process is intended to demonstrate the efficiency of the Calamari OCR framework used for the model training and testing phases.<br/>
The training starts with the creation of the Ground Truth formed by segmented Text-lines in .png format and Transcriptions in associated text files. After the training of the neural network, the ability of the model in the HTR task is tested.
 

For more information, read the paper located in repo root.
# Built with <a name="2"/>
- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [Calamari OCR](https://github.com/Calamari-OCR/calamari)
# Getting Started <a name="3"/>
To run this program you need to install some specific libraries version required by Calamari OCR, install the framework and clone the git repo for src code.
### Prerequisites <a name="4"/>
The python 3.8.7 version of python3 is required to install Calamari OCR Framework.

Calamari requires a specific version of tensorflow to work with and some specific version of this python library, these are all the dependecies neded to work with Calamari OCR 2.0.1

- tensorflow = 2.3.2
- tfaip = 1.0.1
- h5py = 2.10.0
- numpy = 1.18.5

### Installation <a name="5"/>
To install the package without a virtual environment simply run:
```sh
pip install calamari_ocr
```

To install the package from its source, download the source code and run
```sh
python setup.py install
```
Then download all dependecies.
To download the source code check the [Calamari OCR](https://github.com/Calamari-OCR/calamari) repo. <br/>

### Usage <a name="6"/>
To create Ground Truth required by Calamari OCR you need to download from [IAM Database](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database) the datasets. Inside the datasets you will find the .png for each text lines of the document and the corresponding trascriptions in a xml file.  <br/>
To create the Ground Truth download src/ code and run the method in ```Parser.py ```. <br/>
After this run the the following lines from command line to compute the training, prediction and evaluate:
```sh
calamari-train --files your_images.*.png
```
Note, that calamari expects that each image file (.png) has a corresponding ground truth text file (.gt.txt) at the same location with the same base name. Required also by the evaluation step.
```sh
calamari-predict --checkpoint path_to_model.ckpt --files your_images.*.png
```
```sh
calamari-eval --gt *.gt.txt
```
Calamari OCR also presents the possibility of early stopping during training, providing a validation set. Many other training options can be found on the repo [Calamari OCR](https://github.com/Calamari-OCR/calamari). <br/>
In the src/ directory you can find the following files:
- ```Parser.py ``` : Creates the g Truth and manages the files within it
- ```Utilities.py ``` : Utilities methods and creation of Confusion Matrix
- ```Lines_Detector.py ``` : Image preprocessing and simple line segmentation
# Authors
- **Lorenzo Gianassi**
- **Francesco Gigli**
# Acknowledgments
Data and Document Mining Project © Course held by Professor [Simone Marinai](https://www.unifi.it/p-doc2-2013-200006-M-3f2a3d2f3b3030-0.html) - Computer Engineering Master Degree @[University of Florence](https://www.unifi.it/changelang-eng.html)

