from tkinter import E
from flask import Flask, request, jsonify, send_from_directory
from PIL import Image
import os 
import shutil, sys
from fujji import myfujji
from gd import mygd
from lasca import mylasca
import time, datetime, calendar

app = Flask(__name__)


@app.route("/process", methods=["POST"])
def process_image():
    methodName = request.args.get("method", default='fujji', type=str)
    files = request.files.getlist('image')
    print(len(files))
    # for file in files:
    #     print(file)
    date = datetime.datetime.utcnow()
    tmp = calendar.timegm(date.utctimetuple())
    filename = f'{tmp}' 
    if methodName == 'fujji':
        outputfiles  = myfujji(files, filename) 
    elif methodName == 'lasca':
        outputfiles  = mylasca(files, filename) 
    else:
        outputfiles  = mygd(files, filename)    
    print(outputfiles)     
    image_path = "C:/Users/mkpas/Desktop/speckle-analyser-backend/"
   
    return send_from_directory(image_path,filename+'.bmp', as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)