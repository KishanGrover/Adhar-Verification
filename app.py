import os
import urllib.request
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
import cv2
from wand.image import Image
UPLOAD_FOLDER = ''
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.route('/', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message' : 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        global abcc
        abcc=filename
        resp = jsonify({'message' : 'File successfully uploaded'})
        if filename.endswith('.pdf'):
            
            with Image(filename=filename) as img:
        

                with img.convert('png') as converted:
                    converted.save(filename="converted.jpeg")
                    inputdoc=cv2.imread("converted.jpeg")
        else:
            inputdoc=cv2.imread(filename)
            #img3 = cv2.imread(inputdoc)
        #inputdoc=cv2.imread(filename)
        adh=ans(inputdoc)
        vi=Validate(adh)
        resp.status_code = 201
        adhar=jsonify({'1':adh
                      },{'2':vi})

        return adhar
    else:
        resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp
def ans(inputdoc):
    #!/usr/bin/env python
# coding: utf-8

# In[17]:


#For extracting info from adhaar card for now we are only extracting adhaar number using tesseract python
    import time
    start=time.time()
    #import cv2
    import numpy as np
    import pytesseract
    import re
    #from wand.image import Image
    #pytesseract.pytesseract.tesseract_cmd=path/to/tesseract
    #inputdoc=input("Please Input Img/Pdf Of Adhar\n")
    print("Please Wait Till We Are Verifying")


    #img3 = cv2.imread(inputdoc)
    img3=inputdoc
        #print(type(img3))


    rgb_planes = cv2.split(img3)
    result_planes = []
    result_norm_planes = []
    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones((10, 10), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        norm_img = cv2.normalize(diff_img, None, alpha=0, beta=250, norm_type=cv2.NORM_MINMAX,
                                                     dtype=cv2.CV_8UC1)
        result_planes.append(diff_img)
        result_norm_planes.append(norm_img)

    result = cv2.merge(result_planes)
    result_norm = cv2.merge(result_norm_planes)
    dst = cv2.fastNlMeansDenoisingColored(result_norm, None, 10, 10, 7, 11)             # removing noise from image

    text = pytesseract.image_to_string(dst,lang="eng+ben+ta").upper().replace(" ", "")


    number = str(re.findall(r"[0-9]{11,12}", text)).replace("]", "").replace("[","").replace("'", "")
    #print(number)
    a=number




    if len(a)==0:
        for i in range(0,360,10):
            with Image(filename =abcc) as img:
                with img.clone() as rotated:
        # rotate image using rotate() function
                    rotated.rotate(i)
                    rotated.save(filename ="new.png")
                img3 = cv2.imread("new.png")
                rgb_planes = cv2.split(img3)
                result_planes = []
                result_norm_planes = []
                for plane in rgb_planes:
                    dilated_img = cv2.dilate(plane, np.ones((10, 10), np.uint8))
                    bg_img = cv2.medianBlur(dilated_img, 21)
                    diff_img = 255 - cv2.absdiff(plane, bg_img)
                    norm_img = cv2.normalize(diff_img, None, alpha=0, beta=250, norm_type=cv2.NORM_MINMAX,
                                                            dtype=cv2.CV_8UC1)
                    result_planes.append(diff_img)
                    result_norm_planes.append(norm_img)

                result = cv2.merge(result_planes)
                result_norm = cv2.merge(result_norm_planes)
                dst = cv2.fastNlMeansDenoisingColored(result_norm, None, 10, 10, 7, 11)             # removing noise from image

                text = pytesseract.image_to_string(dst,lang="eng+ben+ta").upper().replace(" ", "")


                number = str(re.findall(r"[0-9]{11,12}", text)).replace("]", "").replace("[","").replace("'", "")
                a=number
            if len(a)!=0:
                break
    if len(a)==0 or len(a)!=12:
        return "please upload doc correctly "
    else:

        b=""
        for i in number:
            if len(b)==12:
                break
            else:
                b=b+i
        #type(b)
        aadhar_number_int_type=int(b)
        #type(aadhar_number_int_type)
    #print("Adhar Number Is:\n",number)
    #this is our main algo verhoff algo for verify checksum last digit of adhaar number which will verify the adhar number via some checks example permutation and combinations and give us and result in 
    mult = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 0, 6, 7, 8, 9, 5], [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
            [3, 4, 0, 1, 2, 8, 9, 5, 6, 7], [4, 0, 1, 2, 3, 9, 5, 6, 7, 8], [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
            [6, 5, 9, 8, 7, 1, 0, 4, 3, 2], [7, 6, 5, 9, 8, 2, 1, 0, 4, 3], [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
    perm = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 5, 7, 6, 2, 8, 3, 0, 9, 4], [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
            [8, 9, 1, 6, 0, 4, 3, 5, 2, 7], [9, 4, 5, 3, 1, 2, 6, 8, 7, 0], [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
            [2, 7, 9, 3, 8, 0, 6, 4, 1, 5], [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]]
    return b

def Validate(adh):
    
    
    mult = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 0, 6, 7, 8, 9, 5], [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
            [3, 4, 0, 1, 2, 8, 9, 5, 6, 7], [4, 0, 1, 2, 3, 9, 5, 6, 7, 8], [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
            [6, 5, 9, 8, 7, 1, 0, 4, 3, 2], [7, 6, 5, 9, 8, 2, 1, 0, 4, 3], [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
    perm = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 5, 7, 6, 2, 8, 3, 0, 9, 4], [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
            [8, 9, 1, 6, 0, 4, 3, 5, 2, 7], [9, 4, 5, 3, 1, 2, 6, 8, 7, 0], [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
            [2, 7, 9, 3, 8, 0, 6, 4, 1, 5], [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]]
    try:
        i = len(adh)
        j = 0
        x = 0
        

        while i > 0:
            i -= 1
            x = mult[x][perm[(j % 8)][int(adh[i])]]
            j += 1
        if x == 0:
            return 'Adhar Number Is Valid '
        else:
            return 'Adhar Number Is Invalid'

    except ValueError:
        return 'Adhar Number Is Invalid '
    except IndexError:
        return 'Adhar Number Is Invalid '

    
    while len(adh)!=0:
        if (len(adh) == 12 and adh.isdigit()):
            
            Validate(adh)
            break
        else:
            return 'Adhar Number Is Invalid'
            break
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5025, debug = True)
