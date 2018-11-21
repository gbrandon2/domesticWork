#from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse


#def index(request):
    #return HttpResponse("<h1> hola  mundo ")

from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.index),
    path('home/Signin', views.post),
    path('home/postWork', views.postWork),
    path('home/login', views.postLogIn),
    path('home/ShowWorks', views.ShowWorks),
    path('home/logOut', views.logOut),
    path('home/User', views.User),
    path('home/ShowWorks/filters', views.queryfilters),
    path('home/<int:id>',views.workDetails),
    path('home/delete', views.delete),
    path('home/update', views.sendToUpdateView),
    path('home/updateWork', views.updateWork),
    path('home/User/mywork/<int:id>',views.Applicant),
]
