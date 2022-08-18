from django.urls import path
from ella import views

urlpatterns = [
    path('', views.ella, name='ella'),
]