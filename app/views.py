from django.shortcuts import render
from app.forms import *
from app.forms import TopicForm
from django.http import HttpResponse


# Create your views here.

def insert_topic(request):
    EDTO=TopicForm()
    d={"EDTO":EDTO}
    if request.method=="POST":
        DTO=TopicForm(request.POST)
        if DTO.is_valid():
            DTO.save()
            TOD=Topic.objects.all()
            d={'TOD':TOD}
            return render(request,'display_topic.html',d)
        else:
            return HttpResponse('<h1>invalid data </h1>')
    return render(request,'insert_topic.html',d)



def insert_webpage(request):
    EDWO=WebpageForm()
    d={"EDWO":EDWO}
    if request.method=="POST":
        DWO=WebpageForm(request.POST)
        if DWO.is_valid():
            DWO.save()
            WOD=Webpage.objects.all()
            d={'WOD':WOD}
            return render(request,'display_webpage.html',d)
        else:
            return HttpResponse('<h1>invalid data </h1>')
    return render(request,'insert_webpage.html',d)



