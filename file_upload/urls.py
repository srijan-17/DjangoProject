from django.urls import path
from . import views
from .views import file_upload_view

urlpatterns = [
    path('', views.file_upload_view, name='file_upload'),
]
