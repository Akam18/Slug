from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]

#  он должен только так писат а не то сломается , мы должны вытаскивать из settinga
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Если есть хоть один фото, мы должны сделать это
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)