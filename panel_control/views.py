from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
@login_required
def PanelPagina(request):
    return render(request, "Panel.html")
def logoute(request):
    logout(request)
    return redirect("/accounts/login/?next=/")