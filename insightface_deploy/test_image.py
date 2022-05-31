
from insightface_deploy import face_model
import argparse
from cv2 import cv2, imshow
import sys
import numpy as np

from pathlib import Path
from multiprocessing import Process, Pipe,Value,Array
import insightface
import urllib
import urllib.request
import matplotlib.pyplot as plt
import mxnet.ndarray as nd
import os
#from mtcnn.mtcnn import MTCNN

#import boto3 


#s3 = boto3.client('s3') 

#s3.download_file('hannstorage','face0.bmp','G:\\INSIGHTFACE_ROOT\\deploy\\face0.bmp') 

def init():
    parser = argparse.ArgumentParser(description='face model test')
    parser.add_argument('--image-size', default='112,112', help='')
    parser.add_argument('--model', default='C:/Users/Leesojung/work/community/insightface_deploy/models/model-MobileFaceNet-arc/model,100', help='path to load model.')
    parser.add_argument('--ga-model', default='C:/Users/Leesojung/work/community/insightface_deploy/models/model-MobileFaceNet-arc/model,50', help='path to load model.')
    parser.add_argument('--cpu', default=0, type=int, help='cpu id')
    parser.add_argument('--det', default=0, type=int, help='mtcnn option, 1 means using R+O, 0 means detect from begining')
    parser.add_argument('--flip', default=0, type=int, help='whether do lr flip aug')
    parser.add_argument('--threshold', default=1.24, type=float, help='ver dist threshold')
    args = parser.parse_args([])
    # Face detection Model:

    model = face_model.FaceModel(args)
    #____________________________Base______________________________

    folder = 'C:\\Users\\Leesojung\\work\\community\\media\\result\\'
    images = []

    f = []
    file_name = []
    file_list = os.listdir(folder)
    for file in file_list:
        if file.count(".") == 1:
            name = file.split('.')[0]
            file_name.append(name)
        else:
            for k in range(len(file)-1,0,-1):
                if file[k]=='.':
                    file_name.append(file[:k])
                    break

    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if images is not None:
            images.append(img)
        img = model.get_input(img)
        f.append(model.get_feature(img))
        
            


    #______________________________________face_recognition_model_____________________________________________________________________

    model1 = insightface.app.FaceAnalysis()
    ctx_id = -1

    model1.prepare(ctx_id = ctx_id, nms=0.4)  # This means that all predicted bounding boxes that have an Intersection Over Union IOU ...
    return model, model1, f                                     # value greater than 0.4 with respect to the best bounding boxes will be removed.
    ################################################################
# Analysis faces in this image
def check(model,model1,f,file_path):
    frame = cv2.imread('C:/Users/Leesojung/work/community/media/result/'+str(file_path))
    # frame = cv2.imread('C:/Users/Leesojung/work/community/media/result/test.bmp')


    if os.path.isfile('C:/Users/Leesojung/work/community/media/result/'+str(file_path)):
       os.remove('C:/Users/Leesojung/work/community/media/result/'+str(file_path))
    folder = 'C:\\Users\\Leesojung\\work\\community\\media\\result\\'
    images = []
    print(file_path)

    file_name = []
    file_list = os.listdir(folder)
    for file in file_list:
        if file.count(".") == 1:
            name = file.split('.')[0]
            file_name.append(name)

        else:
            for k in range(len(file)-1,0,-1):
                if file[k]=='.':
                    file_name.append(file[:k])
                    print(file_name)
                    break


    font = cv2.FONT_HERSHEY_SIMPLEX
    print(font)    #*                           #__________________________________________Test image______________________________________


    # frame = cv2.resize(frame,(1080, 780)) #1080 780

    faces = model1.get(frame)
    for idx, face in enumerate(faces):
        x, y, w, h = (face.bbox.astype(np.int).flatten())
        start_pt = (x,y)
        end_pt = (w,h)
        crop_img = frame[y:h, x:w]
        h1, w1, c = crop_img.shape
        if h1>50:
            print('h1>50')
            if w1>50:
                print('w1>50')
                img_ = model.get_input(crop_img)
                print("get_input")
                f_test = model.get_feature(img_)
                print("get_")
                for i in range(0, len(f)):
                    if np.sum(np.square(f_test-f[i])) < 0.9: # Ecludian distance
                        print("success")
                        dd = i
                        print(file_name[dd])
                        return "1", file_name[dd]
                    else:
                       print('fail')                   
    return "0","None"
