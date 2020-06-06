from django.urls import path
from .views import ImageUpload
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("add/", ImageUpload.as_view(), name="Image Uplaod")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
