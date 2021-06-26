from PIL import Image
import io
import base64

def getImageData(monument):
    li=[]
    for i in range(3):
        im = Image.open("C:/Users/akhil/OneDrive/Desktop/py_pro/MonumentRecognizer/images/"+monument+"/"+monument+str(i+1)+".jpg")
        data = io.BytesIO()
        im.save(data, "JPEG")
        encoded_img_data = base64.b64encode(data.getvalue())
        img_data=encoded_img_data.decode('utf-8')
        li.append(img_data)
    return li	