'''
Основное приложение. Отсюда прыгаем в приложение Home-страницы (MainApp)
'''

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from django_summernote import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MainApp.urls')),
    path('summernote/', include('django_summernote.urls')),
] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #подрубаем именно СЮДА строки для работы со статикой
