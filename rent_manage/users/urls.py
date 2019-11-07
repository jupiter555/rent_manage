from django.conf.urls import url
from . import views

urlpatterns = [

    #http:127.0.0.1:8000/users/register
    url(r'^register$',views.register),
    #http:127.0.0.1:8000/users/login
    url(r'^login$',views.login)
]