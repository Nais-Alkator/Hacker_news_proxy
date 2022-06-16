from django.contrib import admin
from django.urls import path, include
from proxy import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_main_page),
    path('download_page/', views.download_page, name='download_page')
]