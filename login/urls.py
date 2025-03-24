from django.urls import path
from . import views
urlpatterns=[

    path("",views.obtener, name="loggeado"),
    path("salir/",views.logoute, name="salir"),
    path("registro/", views.registro, name="registro"),
    path("back_login/",views.login_back, name="back_login")
    
]