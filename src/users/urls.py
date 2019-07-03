
from django.conf.urls import url
from src.users.views import *

urlpatterns = [
    url(r'^$', user_register, name='registrar'),
    url(r'^listar$', datauser_list, name='listar'),
]
