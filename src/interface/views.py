from django.shortcuts import render
from src.users.models import DataUser
# Create your views here.
def index(request):
    
    
    dataUser = DataUser.objects.all()
    contexto = {'dataUser' : dataUser}
    return render(request, 'index.html', contexto)



def editProfile(request):
    return render(request, "edit-profile.html" , {})
