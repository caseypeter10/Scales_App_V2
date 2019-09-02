from django.urls import path

from . import views

app_name = 'scales_app'

urlpatterns = [
    path('SelectBoard', views.SelectBoard, name='SelectBoard'),
    path('GenBoard', views.GenBoard, name='GenBoard'),
               ]