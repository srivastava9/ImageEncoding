from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
import hashlib
from .serializers import ImageSerializer
from .models import ImageModel


class ImageUpload(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Image = ImageModel(**serializer.validated_data)
            encoded_string = Image.get_base64()
            md5_hash = hashlib.md5.digest().encode(encoded_string).strip()
            return Response({
                "md5-hash": md5_hash,
                "encoded": encoded_string
            }, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
