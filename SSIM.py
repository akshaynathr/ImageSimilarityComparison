import numpy as np
import cv2
#from matplotlib import pyplot as plt
from skimage.measure import structural_similarity as ssim



def match(imfil1,imfil2):
	img1=cv2.imread(imfil1)
        (h,w)=img1.shape[:2]
        print("height=")
        print(h)
        print("width=")
        print(w)
        img2=cv2.imread(imfil2)
        resized=cv2.resize(img2,(w,h))
        (h1,w1)=resized.shape[:2]
        print("height=")
        print(h1)
        print("height=")
        print(w1)
        img1=cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2=cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        return ssim(img1,img2)



