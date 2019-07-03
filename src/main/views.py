from django.shortcuts import render, redirect
from src.main.forms import *

# Create your views here.


def login(request):
    return render(request, "login.html" , {})


