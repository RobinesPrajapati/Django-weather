from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('1/', views.fetch_weather_and_forecast, name='fetch_weather_and_forecast')
]