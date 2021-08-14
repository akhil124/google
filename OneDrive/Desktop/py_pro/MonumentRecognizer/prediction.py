from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from labels import label
from urls import url
from monumentMap import wmap
from video import video

model=load_model("C:/Users/akhil/OneDrive/Desktop/py_pro/MonumentRecognizer/model.h5")

def recognizer(filename):

    img_width, img_height = 224,224

    img = image.load_img(filename, target_size=(img_width, img_height))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    classes = model.predict(x)
    arr = classes[0].tolist()
    ind = arr.index(max(arr))
    print(label[ind])
    return (label[ind], url[ind],wmap[ind],video[ind])

