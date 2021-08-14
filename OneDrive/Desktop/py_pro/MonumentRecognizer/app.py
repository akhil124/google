from flask import Flask, render_template, request, redirect, url_for
from wikipedia.wikipedia import summary
from prediction import recognizer
from wiki import give_details
import os
from imageData import getImageData
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
        res, url, plot,video= recognizer(uploaded_file.filename)
        summary = give_details(res).split('.')
        os.remove(uploaded_file.filename)
    images=getImageData(res[:3].lower())
    return render_template("Home.html",res=res,details=summary,images=images, url = url,plot=plot,video=video)

if __name__ == '__main__':
   app.run(debug = True)