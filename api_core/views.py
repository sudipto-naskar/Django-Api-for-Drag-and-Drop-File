from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import medicineSerializer
from .models import *
import cv2 as cv
import numpy as np
from PIL import Image
import os

from rest_framework.decorators import api_view
from rest_framework.response import Response

from keras.models import load_model

MODEL = load_model('./savedModel/model.h5')
class_li = ['Blight', 'Common Rust', 'Gray Leaf Spot', 'Healthy']

def preProcess(img):
    img = cv.resize(img,(224,224))
    img_expand = np.expand_dims(img,axis = 0)
    img_expand = img_expand/255

    return img_expand


def imgPredict(img):
    preds = MODEL.predict(preProcess(img))
    return class_li[np.argmax(preds)]

def tempImageSaver(img):
    with img.open() as file:

        image = Image.open(file)
        format = image.format

        path = f'./temp_image/temp_image.{format.lower()}'

        image.save(path)

        return path


@api_view(['POST','GET'])
def ImageUpload(request):
    data = request.data

    print(data)
    
    img = data['image']

    path = tempImageSaver(img)

    cv_img = cv.imread(path)
    medicine_genre = imgPredict(cv_img)

    medicine_obj = medicines.objects.filter(medicine_genre=medicine_genre)
    
    serializer = medicineSerializer(medicine_obj,many = True)

    os.remove(path)

    return Response({'status':200,'disease':medicine_genre,'data':serializer.data})

