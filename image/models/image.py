import os
from django.db import models
from image.models import TimestampedModel
import base64
from django.conf import settings


def image_as_base64(image_file, format='png'):
    """
    :param `image_file` for the complete path of image.
    :param `format` is format for image, eg: `png` or `jpg`.
    """
    # if not os.path.isfile(image_file):
    #     return ""
    print(image_file, "aditya")
    encoded_string = ''
    with open(image_file, 'rb') as img_f:
        encoded_string = base64.b64encode(img_f.read())
    return encoded_string


class ImageModel(TimestampedModel):
    img = models.ImageField(verbose_name="Image", upload_to="")

    def get_base64(self, *args, **kwargs):
        return image_as_base64(self.img.path)

    def get_time(self, *args, **kwargs):
        print(super().get_created_time(), "aditya time")
      # return super().get_created_time

    class Meta:
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.img.name
