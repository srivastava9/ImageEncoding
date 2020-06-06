from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
import hashlib
import base64
from Crypto.Cipher import AES
from .serializers import ImageSerializer
from .models import ImageModel


def AES_Encrypt(text):
    key = "aditya12345698gf"
    IV = 16 * '\x00'
    mode = AES.MODE_CBC
    encryptor = AES.new(key, mode, IV=IV)
    text = text+"+000000000000"
    cypertext = base64.b64encode(encryptor.encrypt(text))
    return cypertext


class ImageUpload(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Image = ImageModel(**serializer.validated_data)
            Image.save()
            encoded_string = Image.get_base64()
            md5_hash = hashlib.md5(b'%s' % (encoded_string))

            # .digest().encode(encoded_string).strip()
            hash_encoded = md5_hash.hexdigest()
            timestr = Image.get_time()
            AES_enc = AES_Encrypt(timestr)
            return Response({
                "AES_encryption_timestamp": AES_enc,
                "md5-hash": hash_encoded,
                "base64_encoded": encoded_string
            }, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
