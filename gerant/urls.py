from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="gerant_home"),
    path('forgot', views.forgot, name="gerant_forgot"),
    path('deconnexion', views.deconnexion, name="gerant_logout"),
    path('connexion', views.connected, name="gerant_login"),
]