from django.urls import path
from . import views

urlpatterns = [
    path('', views.latest_news, name='latest_news'),
]
