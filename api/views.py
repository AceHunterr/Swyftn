import hashlib
import requests
from PIL import Image
import imagehash
from io import BytesIO
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import ImageData
from .serializers import ImageDataSerializer

class ImageHashCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        image_url = request.data.get('image_url')
        if not image_url:
            return Response({"error": "Image URL is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:

            response = requests.get(image_url)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
            md5_hash = hashlib.md5(response.content).hexdigest()
            phash = str(imagehash.phash(img))
            image_data = ImageData.objects.create(
                image_url=image_url,
                md5_hash=md5_hash,
                phash=phash
            )

            serializer = ImageDataSerializer(image_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ImageDataListCreateAPIView(ListCreateAPIView):
    queryset = ImageData.objects.all()
    serializer_class = ImageDataSerializer

class ImageDataRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ImageData.objects.all()
    serializer_class = ImageDataSerializer
