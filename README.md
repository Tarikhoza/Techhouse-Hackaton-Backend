# Techhouse-Hackaton-Backend
This script is a Python web application using Flask and some computer vision libraries to perform image segmentation on an input image of a plank to identify and mask defects. This script, the frontend and the ML modell got as the 1.place at the Techhouse Mobilathon Hackaton 2021 for the technical challenge.

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

Connect to the server with the browser:

    localhost:8000

# Here are some example outputs from the model:
<img src="collage.jpeg">

Most of the AI training and research was done by my Friends 
<a href="https://github.com/hal3e">@hal3e</a>,
<a href="https://github.com/MujkicA">@MujkicA</a> and
<a href="https://github.com/enizimus">@enizimus</a>


Here is a video of the frontend written by <a href="https://github.com/Salka1988">@Salka1988</a>:

<img src="frontend.gif">

The frontend and the ML training scripts are not the part of this repository. If you are interested how the code looks like please contact the other team members.

At last here is a image of the whole team that participated on the hackaton.

<img src="hackaton_winner.jpeg">

