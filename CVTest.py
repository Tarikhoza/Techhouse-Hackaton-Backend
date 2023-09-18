import numpy as np
import cv2
import tensorflow as tf
import tensorflow.keras as keras
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






vid = cv2.VideoCapture(0)
while(True):
    ret, img = vid.read()
    mask=predict(img)
    (thresh, mask) = cv2.threshold(mask, 0.5, 1, cv2.THRESH_BINARY)
    mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2RGB)
    mask=cv2.resize(mask,(img.shape[1],img.shape[0]))
    mask=mask*255
    mask=mask*[0,0,255]
    colored_img=cv2.addWeighted(mask, 1, img, 1, 0, mask,dtype=cv2.CV_8U)
    cv2.imshow('diff', colored_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
