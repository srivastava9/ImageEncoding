from django.contrib import admin
from image.models import ImageModel
# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    list_display = ("img", "created_at")


admin.site.register(ImageModel, ImageAdmin)
