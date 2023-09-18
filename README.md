# Techhouse-Hackaton-Backend
This script is a Python web application using Flask and some computer vision libraries to perform image segmentation on an input image of a plank to identify and mask defects.

# How to use
Install a conda enviroment with python3.8

    conda create -n gutes_holz python=3.8 anaconda

Acivate the conda enviroment with

    conda activate gutes_holz

Install the dependences with:

    pip install -r requirements.txt

Install Segmentation-Models with:

    pip install -U segmentation-models

Start Flask server with:

    python App.py

# Here are some example outputs from the model:
## 1. Input
<img src="static/images/img2.jpg">

## 1. Output
<img src="static/images/mask-img2.jpg">

## 2. Input
<img src="static/images/example1.jpeg">

## 2. Output
<img src="static/images/mask-example1.jpeg">

## 3. Input
<img src="static/images/example2.jpeg">

## 3. Output
<img src="static/images/mask-example2.jpeg">

