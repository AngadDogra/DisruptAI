from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('alerts/', views.alerts, name="alerts"),
    path('map/', views.map, name="map"),
    path('settings/', views.settings, name="settings"),
]
