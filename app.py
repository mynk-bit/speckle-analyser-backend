from flask import Flask, request, jsonify, send_from_directory
from PIL import Image
import os 
import shutil, sys
from fujji import myfunc
# from gd import myfunc
# from lasca import myfunc



import time, datetime, calendar

app = Flask(__name__)


@app.route("/process", methods=["POST"])
def process_image():
    files = request.files.getlist('image')
    print(len(files))
    # for file in files:
    #     print(file)
    date = datetime.datetime.utcnow()
    tmp = calendar.timegm(date.utctimetuple())
    filename = f'{tmp}' 
    outputfiles  = myfunc(files, filename) 
    print(outputfiles)     
    image_path = "C:/Users/mkpas/Desktop/Flask/"
    # if os.path.exists(image_path):
    #     shutil.rmtree(image_path)
    # if not os.path.exists(image_path):
    #     os.mkdir(image_path)

    # print (len(files))
    # mylist =  []
    # myImg = []
    # i = 1;
    # for file in files:
    #     file.save(f'{image_path}/{i}.bmp')
    #     i = i+1
    #     img = Image.open(file.stream)
    #     file.save(f'{image_path}/{i+1}.bmp')
    #     myImg.append(img)   
    #     mylist.append([img.width, img.height])   
    # print(mylist)  
    
    return send_from_directory(image_path,filename+'.bmp', as_attachment=True)

    # return jsonify({'msg': 'success'})

if __name__ == "__main__":
    app.run(debug=True)