from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="admin_home"),
    path('forgot', views.forgot, name="admin_forgot"),
]