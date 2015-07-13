from imgSearch import descriptor
import glob
import argparse

import cv2

#ap=argparse.ArgumentParser()
#ap.add_argument("-d","--dataset",required=True, help="Path to the directory that contains images to be indexed")

#ap.add_argument("-i","--index",required=True,help = "Path to computed index stored")

#args=vars(ap.parse_args())

def index(Dataset):
    indexfile='index.csv'

    dataset=Dataset

    cd=descriptor((8,12,3))

    output=open(indexfile,"w")


    for imagePath in glob.glob(dataset+"*.jpg"):
        imageID=imagePath[imagePath.rfind("/")+1:]
        image=cv2.imread(imagePath)


        features=cd.describe(image)

        features=[str(f) for f in features]

        output.write("%s,%s\n" % (imageID,",".join(features) ) )



    for imagePath in glob.glob(dataset+"*.png"):
        imageID=imagePath[imagePath.rfind("/")+1:]
        image=cv2.imread(imagePath)


        features=cd.describe(image)

        features=[str(f) for f in features]

        output.write("%s,%s\n" % (imageID,",".join(features) ) )


    output.close()

