from imgSearch import descriptor
import math
from searcher import Searcher
import os
import argparse
#from SSIM import *
import cv2


def matcher(Dataset,Query):
    dataset='uploads'

    query_image=Query
    
    index='index.csv'
    
    res=0
    res1=0

    cd=descriptor((8,12,3))

    query=cv2.imread(query_image)

    gray=cv2.cvtColor(query,cv2.COLOR_BGR2GRAY)
    cv2.imwrite('grey.jpg',gray)

    query_grey=cv2.imread('grey.jpg')


    features=cd.describe(query)

    features_grey=cd.describe(query_grey)

    searcher=Searcher(index)
    results=searcher.search(features)
    results_grey=searcher.search(features_grey)


    #cv2.imshow("Query",query)

    for (score,resultID) in results:
        result=cv2.imread(dataset+resultID)
        #m=match(query_image,dataset+resultID)
        #cv2.imshow("Result",result)
        print(resultID)
        if score < 7.95:
            print(score)
            t=math.floor(score)
            res=100-t
            print(100-t)
        else:
            print(score)
            t=math.floor(score)
            res=t
            print(t+t)
            #cv2.waitKey(0)


    print("---------------grey---------------")
    for (score,resultID) in results_grey:
        result=cv2.imread(dataset+resultID)
        #cv2.imshow("Result",result)
        print(resultID)
        if score < 7.95:
            print(score)
            t=math.floor(score)
            res1=100-t
            print(100-t)
        else:
            print(score)
            t=math.floor(score)
            res1=t
            print(t+t)
            #cv2.waitKey(0)
    return (res,res1) 

