import os
import numpy as np
from flask import Flask, flash, request, redirect, url_for,render_template,jsonify
from werkzeug.utils import secure_filename
import cv2
import base64
import json
from io import BytesIO
import requests
import tensorflow as tf
import tensorflow.keras as keras
#from tensorflow import keras
import segmentation_models as sm

sm.set_framework("tf.keras")
sm.framework()
BACKBONE = 'resnet50'

preprocess_input = sm.get_preprocessing(BACKBONE)

activation = 'sigmoid'


model = sm.Unet(BACKBONE,input_shape=(160,480,3), classes=1, activation=activation)


model.load_weights('best_model.h5')

# Check its architecture
model.summary()



def predict(image):
    old=image
    image=cv2.resize(image,(480,160))
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    image=np.expand_dims(image,axis=0)
    mask=model.predict(image)[0]
    mask=cv2.resize(mask,(old.shape[0],old.shape[1]))

    return mask
#predict(os.path.join(os.getcwd(),"static","images","w.jpg"))




UPLOAD_FOLDER = '/images/'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

UPLOAD_FOLDER="static/images/"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'the random string'



@app.route("/")
def landing():
    return render_template('index.html')

@app.route("/results/<string:filename>")
def results(filename):
    return render_template("results.html", file=filename)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST','OPTIONS'])
def upload_file():
    if (request.method == 'POST') or (request.method =='OPTIONS'):
        # check if the post request has the file part
        print(request.files)
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            img = cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            mask = predict(img)



            (thresh, mask) = cv2.threshold(mask, 0.5, 1, cv2.THRESH_BINARY)
            #mask[mask>=0.5]=1.0
            #mask[mask<0.5]=0.0
            #mask=(mask*-1)+1
            #mask=(mask*255).astype(img.dtype)
            #mask=np.dstack([mask]*3)

            mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2RGB)
            mask=cv2.resize(mask,(img.shape[1],img.shape[0]))
            mask=mask*255
            print(mask.shape,np.max(mask))

            print(img.shape,np.max(img))
            colored_img=cv2.addWeighted(mask, 1, img, 1, 0, mask,dtype=cv2.CV_32F)



            cv2.imwrite(os.path.join(app.config['UPLOAD_FOLDER'], "mask-"+filename),mask)
            return redirect(url_for('results' ,filename=file.filename))
    return render_template("upload.html")




app.run(debug=True, host="0.0.0.0",port=8000)

