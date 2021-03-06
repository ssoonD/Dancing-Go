# from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .test import test
import base64

# Create your views here.
@api_view(['POST'])
def upload_image(request):
   videoImage, webcamImage = request.data['images']
   videoRealImage = base64.b64decode(videoImage[22:])
   webcamRealImage = base64.b64decode(webcamImage[22:])
   userId = request.data['userid']
   # image = base64Image.encode()
   # print(image)
   videoImageName = 'videoImage_'+userId+'.jpg'
   webcamImageName = 'webcamImage_'+userId+'.jpg'
   with open(videoImageName, "wb") as f:
      f.write(videoRealImage)
   with open(webcamImageName, "wb") as f:
      f.write(webcamRealImage)
   videoSkeleton = test(videoImageName)
   webCamSkeleton = test(webcamImageName)


   result_json = { 'skeletons': [videoSkeleton, webCamSkeleton] }
   return JsonResponse(result_json)

@api_view(['GET'])
def sample(request):
   print('HELLO')
   print(request)
   result_json = { 'result': 'ok' }
   return JsonResponse(result_json)