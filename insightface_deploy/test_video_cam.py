import face_model
import argparse
from cv2 import cv2
import sys
import numpy as np

from pathlib import Path
from multiprocessing import Process, Pipe,Value,Array
import insightface
import urllib
import urllib.request
import matplotlib.pyplot as plt
import mxnet.ndarray as nd
#from mtcnn.mtcnn import MTCNN


parser = argparse.ArgumentParser(description='face model test')
# general
parser.add_argument('--image-size', default='112,112', help='')
parser.add_argument('--model', default='G:/insightface_deploy/models/model-MobileFaceNet-arc/model,100', help='path to load model.')
parser.add_argument('--ga-model', default='G:/insightface_deploy/models/model-MobileFaceNet-arc/model,50', help='path to load model.')
parser.add_argument('--cpu', default=0, type=int, help='cpu id')
parser.add_argument('--det', default=0, type=int, help='mtcnn option, 1 means using R+O, 0 means detect from begining')
parser.add_argument('--flip', default=0, type=int, help='whether do lr flip aug')
parser.add_argument('--threshold', default=1.24, type=float, help='ver dist threshold')
args = parser.parse_args()

model = face_model.FaceModel(args)

#_________________Base______________________________
img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face2\\photo39.bmp')
img = model.get_input(img)
f1 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face3\\photo81.bmp')
img = model.get_input(img)
f2 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face4\\photo16.bmp')
img = model.get_input(img)
f3 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face5\\1.jpg')
img = model.get_input(img)
f4 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face6\\photo2.bmp')
img = model.get_input(img)
f5 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face19\\photo12.bmp')
img = model.get_input(img)
f6 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face18\\photo11.bmp')
img = model.get_input(img)
f7 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face20\\photo13.bmp')
img = model.get_input(img)
f8 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face8\\photo2.bmp')
img = model.get_input(img)
f9 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face7\\photo1.bmp')
img = model.get_input(img)
f10 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face9\\photo3.bmp')
img = model.get_input(img)
f11 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face10\\photo4.bmp')
img = model.get_input(img)
f12 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face11\\photo5.bmp')
img = model.get_input(img)
f13 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face12\\photo6.bmp')
img = model.get_input(img)
f14 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face13\\photo14.bmp')
img = model.get_input(img)
f15 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face14\\photo7.bmp')
img = model.get_input(img)
f16 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face15\\photo8.bmp')
img = model.get_input(img)
f17 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face16\\photo9.bmp')
img = model.get_input(img)
f18 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face17\\photo10.bmp')
img = model.get_input(img)
f19 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face21\\113.jpg')
img = model.get_input(img)
f20 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face1\\photo42.bmp')
img = model.get_input(img)
f21 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face22\\photo5.bmp')
img = model.get_input(img)
f22 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face23\\433.jpg')
img = model.get_input(img)
f23 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face24\\photo6.bmp')
img = model.get_input(img)
f24 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face25\\photo7.bmp')
img = model.get_input(img)
f25 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face26\\photo8.bmp')
img = model.get_input(img)
f26 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face27\\photo10.bmp')
img = model.get_input(img)
f27 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face28\\photo9.bmp')
img = model.get_input(img)
f28 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face29\\photo11.bmp')
img = model.get_input(img)
f29 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face30\\photo12.bmp')
img = model.get_input(img)
f30 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face31\\photo13.bmp')
img = model.get_input(img)
f31 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face32\\photo15.bmp')
img = model.get_input(img)
f32 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face101\\photo1.jpg')  
img = model.get_input(img)
f33 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face34\\photo16.bmp')
img = model.get_input(img)
f34 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face35\\photo17.bmp')
img = model.get_input(img)
f35 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face36\\photo18.bmp')
img = model.get_input(img)
f36 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face37\\photo19.bmp')
img = model.get_input(img)
f37 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face38\\photo20.bmp')
img = model.get_input(img)
f38 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face39\\photo21.bmp')
img = model.get_input(img)
f39 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face40\\photo22.bmp')
img = model.get_input(img)
f40 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face41\\photo23.bmp')
img = model.get_input(img)
f41 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face42\\9162.jpg')
img = model.get_input(img)
f42 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face43\\10119.jpg')
img = model.get_input(img)
f43 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face44\\10337.jpg')
img = model.get_input(img)
f44 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face45\\10400.jpg')
img = model.get_input(img)
f45 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face46\\10448.jpg')
img = model.get_input(img)
f46 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face47\\11040.jpg')
img = model.get_input(img)
f47 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face48\\10559.jpg')
img = model.get_input(img)
f48 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face49\\11136.jpg')
img = model.get_input(img)
f49 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face50\\11723.jpg')
img = model.get_input(img)
f50 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face51\\photo2.bmp')
img = model.get_input(img)
f51 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face52\\photo6.bmp')
img = model.get_input(img)
f52 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face53\\photo3.bmp')
img = model.get_input(img)
f53 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face54\\photo4.bmp')
img = model.get_input(img)
f54 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face55\\photo5.bmp')
img = model.get_input(img)
f55 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face56\\photo7.bmp')
img = model.get_input(img)
f56 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face57\\photo8.bmp')
img = model.get_input(img)
f57 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face58\\photo9.bmp')
img = model.get_input(img)
f58 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face59\\photo10.bmp')
img = model.get_input(img)
f59 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face60\\photo11.bmp')
img = model.get_input(img)
f60 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face61\\photo12.bmp')
img = model.get_input(img)
f61 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face62\\photo13.bmp')
img = model.get_input(img)
f62 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face63\\photo14.bmp')
img = model.get_input(img)
f63 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face64\\photo15.bmp')
img = model.get_input(img)
f64 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face65\\photo16.bmp')
img = model.get_input(img)
f65 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face66\\photo17.bmp')
img = model.get_input(img)
f66 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face67\\photo18.bmp')
img = model.get_input(img)
f67 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face68\\photo19.bmp')
img = model.get_input(img)
f68 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face69\\photo20.bmp')
img = model.get_input(img)
f69 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face70\\photo21.bmp')
img = model.get_input(img)
f70 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face71\\photo22.bmp')
img = model.get_input(img)
f71 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face72\\photo23.bmp')
img = model.get_input(img)
f72 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face73\\photo24.bmp')
img = model.get_input(img)
f73 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face74\\photo4.bmp')
img = model.get_input(img)
f74 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face75\\photo26.bmp')
img = model.get_input(img)
f75 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face76\\photo27.bmp')
img = model.get_input(img)
f76 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face77\\photo28.bmp')
img = model.get_input(img)
f77 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face78\\photo29.bmp')
img = model.get_input(img)
f78 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face79\\photo30.bmp')
img = model.get_input(img)
f79 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face80\\photo31.bmp')
img = model.get_input(img)
f80 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face81\\photo32.bmp')
img = model.get_input(img)
f81 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face82\\photo33.bmp')
img = model.get_input(img)
f82 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face83\\photo34.bmp')
img = model.get_input(img)
f83 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face84\\photo35.bmp')
img = model.get_input(img)
f84 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face85\\photo36.bmp')
img = model.get_input(img)
f85 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face86\\photo37.bmp')
img = model.get_input(img)
f86 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face87\\photo38.bmp')
img = model.get_input(img)
f87 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face88\\photo39.bmp')
img = model.get_input(img)
f88 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face89\\photo40.bmp')
img = model.get_input(img)
f89 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face90\\photo41.bmp')
img = model.get_input(img)
f90 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face91\\photo42.bmp')
img = model.get_input(img)
f91 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face92\\photo43.jpg')
img = model.get_input(img)
f92 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face93\\photo44.bmp')
img = model.get_input(img)
f93 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face94\\photo45.bmp')
img = model.get_input(img)
f94 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face95\\photo46.bmp')
img = model.get_input(img)
f95 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face96\\photo47.bmp')
img = model.get_input(img)
f96 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face97\\photo48.bmp')
img = model.get_input(img)
f97 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face98\\photo3.bmp')
img = model.get_input(img)
f98 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face99\\photo2.bmp')
img = model.get_input(img)
f99 = model.get_feature(img)

img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face100\\photo1.bmp')
img = model.get_input(img)
f100 = model.get_feature(img)



"""
# compare distance between two faces 
dist = np.sum(np.square(f1-f2)) # Ecludian distance
print(dist)
sim = np.dot(f1, f2.T) # Cosine Similarity
print(sim)

#feature_txt.close()
#sys.exit(0)
#diff = np.subtract(source_feature, target_feature)
#dist = np.sum(np.square(diff),1)
"""
#_________________ temp___________________________________________________________________________________________________________________

#img = cv2.imread('C:\\Users\\haanvision\\source\\repos\\InsightFace\\InsightFace\\test2.jpg')
model1 = insightface.app.FaceAnalysis()

ctx_id = -1

model1.prepare(ctx_id = ctx_id, nms=0.4)  # This means that all predicted bounding boxes that have an Intersection Over Union IOU ...
                                          # value greater than 0.4 with respect to the best bounding boxes will be removed.

################################################################
# Analysis faces in this image
 # font 
font = cv2.FONT_HERSHEY_SIMPLEX    #*
#faces = model1.get(img)            #*
#mtcnn = MTCNN()
#print('mtcnn loaded')

cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FPS, 30)            # ______________________________________________check here ________________

while cap.isOpened():
    isSuccess,frame = cap.read()
    if isSuccess:            
        try:

            #image = Image.fromarray(frame)
            faces = model1.get(frame)
            for idx, face in enumerate(faces):
              #print("Face [%d]:"%idx)
              #print("\tage:%d"%(face.age))
              gender = 'Male'
              if face.gender==0:
                gender = 'Female'
              #print("\tgender:%s"%(gender))
              #print("\tembedding shape:%s"%face.embedding.shape)
              #print("\tbbox:%s"%(face.bbox.astype(np.int).flatten()))
              #print("\tlandmark:%s"%(face.landmark.astype(np.int).flatten()))
             
              x,y,w,h = (face.bbox.astype(np.int).flatten())
              start_pt = (x,y)
              end_pt = (w,h)
              crop_img = frame[y:h, x:w]
              #cv2.imshow("crop%d:"%idx, crop_img)
              #cv2.waitKey(0)
              # if too small face then ignore the feature extraction 
              h1,w1,c=crop_img.shape
              if h1>50:
                  if w1>50:
                        img_ = model.get_input(crop_img)
                        f_test = model.get_feature(img_)
                        
                        #_______________________face compare________________________

                        dist = np.sum(np.square(f_test-f1)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Harris" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)
           
                        dist = np.sum(np.square(f_test-f2)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "O-in" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f3)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Mingu" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f4)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Mr.Lee" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f5)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Sepideh" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)



                        dist = np.sum(np.square(f_test-f6)) # Ecludian distance
                        print(dist)
                        if dist<1.3:
                             confidence=100-dist
                             cv2.putText(frame, "Kochanie" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f7)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Raul" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f8)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Eric" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f9)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Maxim" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f10)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Suchit" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f11)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Sunga Ah" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f12)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Jung" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f13)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Hana" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)
  
                        dist = np.sum(np.square(f_test-f14)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Shisa" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f15)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Liho" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f16)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Jung Ah" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f17)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Sung" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f18)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Hidi" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f19)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Ahmed" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f20)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Hong" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f21)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Hee-Song" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f22)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Mattias" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f23)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Rafael" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f24)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Santiago" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f25)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Yo-Saeng" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f26)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Kheldov" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f27)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Jacob" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f28)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Kevin" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f29)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Nu-wool" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f30)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "본화형" ,(x,y-5), font,   # ~~~~~~~~~~~~~~~~_________________________check korean language 
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        
                        dist = np.sum(np.square(f_test-f31)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Sam" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f32)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Dereje" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                                                                                    

                        dist = np.sum(np.square(f_test-f33)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Paul" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                             
                        dist = np.sum(np.square(f_test-f34)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Karen" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f35)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Abdullah" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f36)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Abu-Bakr" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f37)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Young-Jun" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                      
                        dist = np.sum(np.square(f_test-f38)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Saem" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        
                        dist = np.sum(np.square(f_test-f39)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Young-Lo" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        
                        dist = np.sum(np.square(f_test-f40)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Hyung-Jae" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f41)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Jae-Hun" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f42)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Shereen" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f43)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Suzan" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f44)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Monica" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f45)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "soso" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f46)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Hakeem" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f47)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Raj" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f48)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Albert" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f49)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Mona" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f50)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Liza" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f51)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Rolando" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f52)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Cansu" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        
                        dist = np.sum(np.square(f_test-f53)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Feruza" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f54)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Tuan" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)
                        
                             
                        dist = np.sum(np.square(f_test-f55)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Yoosef" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)
                        
                       
                        dist = np.sum(np.square(f_test-f56)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Liso's mom" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f57)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Coner" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f58)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Kal" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f59)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Mom" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                       
                        dist = np.sum(np.square(f_test-f60)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Mia" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f61)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Rolie" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f62)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Lilia" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f62)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Lilia" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f63)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "JB" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f64)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Hwang" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f65)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Houng-Tae" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        
                        dist = np.sum(np.square(f_test-f65)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Houng-Tae" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f66)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Sheida" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        
                        dist = np.sum(np.square(f_test-f67)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Joonas" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        
                        dist = np.sum(np.square(f_test-f67)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Joonas" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f68)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Irene" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f69)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Joost" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f70)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Shadi" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f71)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Ku_mo_Nim" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f72)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Josef" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f73)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Alin" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f74)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Dave" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f75)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Akram" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        
                        dist = np.sum(np.square(f_test-f76)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Ali" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        
                        dist = np.sum(np.square(f_test-f77)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Steven" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        
                        dist = np.sum(np.square(f_test-f78)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "kim-baksa" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f79)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Tiko" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f80)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Eva" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f81)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Clare" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f82)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Leonardo" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f83)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Lara" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f83)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Lara" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f84)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Yonna" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f85)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Kassea" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f85)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Clonia" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f86)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Avo" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f87)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Harvy" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f88)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Brain" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f89)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "John" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)

                        dist = np.sum(np.square(f_test-f90)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Abel" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f91)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Aiko_Husband" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f92)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Aiko" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f93)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Ashraf" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f94)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Abrahim" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f95)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Baseem" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f96)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Kaila" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f97)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Christie" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f98)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Jongo" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)



                        dist = np.sum(np.square(f_test-f99)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Jae_Young" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)


                        dist = np.sum(np.square(f_test-f100)) # Ecludian distance
                        print(dist)
                        if dist<1.1:
                             confidence=100-dist
                             cv2.putText(frame, "Alessandro" ,(x,y-5), font,  
                                         0.6, (0, 0, 255) , 1, cv2.LINE_AA)
                             cv2.putText(frame, 'score = %f'%confidence ,(x,y-25), font,  
                                         0.5, (50, 50, 255) , 1, cv2.LINE_AA)



              cv2.rectangle(frame,start_pt,end_pt, (0, 255, 0), 2)
 
              cv2.putText(frame, gender, (x,y+20), font,  
                               0.5, (255, 255, 0) , 1, cv2.LINE_AA) 
              cv2.putText(frame, "age:%d"%(face.age),(x,h+10), font,  
                               0.5, (255, 0, 0) , 1, cv2.LINE_AA) 

              #cv2.putText(img, "Face [%d]:"%idx ,(x,y-5), font,  
                              #1, (0, 0, 255) , 1, cv2.LINE_AA)
              x1,y1,x2,y2,x3,y3,x4,y4,x5,y5=(face.landmark.astype(np.int).flatten())
              cv2.circle(frame, (x1, y1), 2, (255, 0, 255), -1) # 1
              cv2.circle(frame, (x2, y2), 2, (255, 0, 255), -1) # 2
              cv2.circle(frame, (x3, y3), 2, (255, 0, 255), -1) # 3
              cv2.circle(frame, (x4, y4), 2, (255, 0, 255), -1) # 4
              cv2.circle(frame, (x5, y5), 2, (255, 0, 255), -1) # 5

              print("")


        except:
            print('detect error')       
       
        cv2.imshow('face Capture', frame)
 

    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cap.release()
if args.save:
    video_writer.release()
cv2.destroyAllWindows()  


"""
# show result
# org 
org = (20, 20) 
# fontScale 
fontScale = 1
# Blue color in BGR 
color = (255, 0, 0) 
# Line thickness of 2 px 
thickness = 2 
image = cv2.putText(img, 'Output Results', org, font,  
                    fontScale, color, thickness, cv2.LINE_AA) 
cv2.imshow("out", img)
cv2.waitKey(0)
"""
#_________________________________________________________________________________________________________________________
"""

####___________________ class 1_________________________
img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face2\\photo3.bmp')
img = model.get_input(img)

# features to be saved in the txt file 
feature_txt = open('features_ArcFace.txt', 'w')

f1 = model.get_feature(img)
print(f1[0:10])

for i in range(0, len(f1)):
    feature_txt.write(str(f1[i]) + ' ')
feature_txt.write('\n')

i=0
img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face2\\photo55.bmp')
img = model.get_input(img)


f1 = model.get_feature(img)
#print(f1)

for i in range(0, len(f1)):
    feature_txt.write(str(f1[i]) + ' ')
feature_txt.write('\n')

i=0
img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face2\\photo39.bmp')
img = model.get_input(img)


f1 = model.get_feature(img)
#print(f1)

for i in range(0, len(f1)):
    feature_txt.write(str(f1[i]) + ' ')
feature_txt.write('\n')



    gender, age = model.get_ga(img)

    if gender==0:
        gender = 'Female'
  
    if gender==1:
        gender = 'Male'

    print(gender)
    print(age)


####___________________ class 2_________________________
img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face1\\photo41.bmp')
#cv2.imshow('show',img1)
#cv2.waitKey(0)

img = model.get_input(img)
f1 = model.get_feature(img)
print(f1[0:10])

for i in range(0, len(f1)):
    feature_txt.write(str(f1[i]) + ' ')
feature_txt.write('\n')

i=0
img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face1\\photo63.bmp')
img = model.get_input(img)


f1 = model.get_feature(img)
#print(f1)

for i in range(0, len(f1)):
    feature_txt.write(str(f1[i]) + ' ')
feature_txt.write('\n')

i=0
img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face1\\photo42.bmp')
img = model.get_input(img)


f1 = model.get_feature(img)
#print(f1)

for i in range(0, len(f1)):
    feature_txt.write(str(f1[i]) + ' ')
feature_txt.write('\n')

gender, age = model.get_ga(img)

if gender==0:
    gender = 'Female'
  
if gender==1:
    gender = 'Male'

print(gender)
print(age)



####___________________ class 3_________________________
img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face3\\photo70.bmp')
#cv2.imshow('show',img1)
#cv2.waitKey(0)

img = model.get_input(img)
f1 = model.get_feature(img)
print(f1[0:10])

for i in range(0, len(f1)):
    feature_txt.write(str(f1[i]) + ' ')
feature_txt.write('\n')

i=0
img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face3\\photo81.bmp')
img = model.get_input(img)


f1 = model.get_feature(img)
#print(f1)

for i in range(0, len(f1)):
    feature_txt.write(str(f1[i]) + ' ')
feature_txt.write('\n')

i=0
img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face3\\photo98.bmp')
img = model.get_input(img)


f1 = model.get_feature(img)
#print(f1)

for i in range(0, len(f1)):
    feature_txt.write(str(f1[i]) + ' ')
feature_txt.write('\n')


####___________________ class 4_________________________
img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face4\\photo15.bmp')
#cv2.imshow('show',img1)
#cv2.waitKey(0)

img = model.get_input(img)
f1 = model.get_feature(img)
print(f1[0:10])

for i in range(0, len(f1)):
    feature_txt.write(str(f1[i]) + ' ')
feature_txt.write('\n')

i=0
img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face4\\photo16.bmp')
img = model.get_input(img)


f1 = model.get_feature(img)
#print(f1)

for i in range(0, len(f1)):
    feature_txt.write(str(f1[i]) + ' ')
feature_txt.write('\n')

i=0
img = cv2.imread('G:\\INSIGHTFACE_ROOT\\deploy\\data\\face1\\photo42.bmp')
img = model.get_input(img)


f1 = model.get_feature(img)
#print(f1)

for i in range(0, len(f1)):
    feature_txt.write(str(f1[i]) + ' ')
feature_txt.write('\n')
#____________________________________________________________________
"""