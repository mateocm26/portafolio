from django.shortcuts import render, redirect
from src.users.forms import UserForm
from src.main.forms import EducationForm
from src.users.models import DataUser
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def login(request):
    return render(request, "login.html" , {})


def datauser_list(request):
    dataUser = DataUser.objects.all()
    contexto = {'dataUser' : dataUser}
    return render(request, 'index.html', contexto)

	

def user_register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('usuarios:registrar')
    else:
        form = UserForm()
    return render(request, 'user_register.html', {'form': form})

