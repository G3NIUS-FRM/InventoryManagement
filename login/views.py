from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import *
from django.contrib.auth.models import User, Group
# Create your views here.
@login_required

def obtener(request):
    nombre=request.user
    return render(request,"home.html",{"nombre":nombre})
def logoute(request):
    logout(request)
    return redirect("/")
def registro(request):
    if request.method == "POST":
        nombre=request.POST.get("first_name")
        apellido=request.POST.get("last_name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POST.get("password")
        repass=request.POST.get("rePassword")
        confiNombre=User.objects.filter(username=username)
        confiEmail=User.objects.filter(email=email)
        if not confiNombre and password == repass and not confiEmail:
            usuario=User.objects.create_user(username=username, password=password, email=email, )
            usuario.first_name=nombre
            usuario.last_name=apellido
            grupo=Group.objects.get(name="clients")
            usuario.groups.add(grupo)
            usuario.save()
            print("usuario insertado")
            return redirect("/accounts/login/?next=/")
    return render(request,"registro.html")
def login_back(request):
    return redirect("/accounts/login/?next=/")