from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="admin_home"),
    path('forgot', views.forgot, name="admin_forgot"),
    path('deconnexion', views.deconnexion, name="admin_logout"),
    path('connexion', views.connected, name="admin_login"),
]