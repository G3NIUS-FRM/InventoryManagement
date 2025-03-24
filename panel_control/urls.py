from django.urls import path
from . import views
urlpatterns=[
    path('',views.PanelPagina, name="panel_control"),
    path('login/',views.logoute, name="logoute"),


]