from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse 

# Create your views here.

def insert_topic(request):
    ETFO=Topicform()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=Topicform(request.POST)
        if TFDO.is_valid():
            tno=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tno)[0]
            TO.save()
            return HttpResponse('data submitted')
            #return HttpResponse(str(TFDO.cleaned_data))  #to display the data in dictionary
        else:
            return HttpResponse('data is invalid')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=Webpagesform()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=Webpagesform(request.POST)
        if WFDO.is_valid():
            tno=WFDO.cleaned_data['topic_name']
            na=WFDO.cleaned_data['name']
            ur=WFDO.cleaned_data['url']
            WO=Webpages.objects.get_or_create(topic_name=tno,name=na,Url=ur)[0]
            WO.save()
            return HttpResponse('data submitted')
        else:
            return HttpResponse('data invalid')
    return render(request,'insert_webpage.html',d)


def insert_AccessRecords(request):
    EAFO=AccessRecordsform()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessRecordsform(request.POST)
        if AFDO.is_valid():
            na=AFDO.cleaned_data['name']
            da=AFDO.cleaned_data['date']
            au=AFDO.cleaned_data['author']
            AR=AccessRecords.objects.get_or_create(name=na,date=da,author=au)[0]
            AR.save()
            return HttpResponse('data submitted')
        else:
            return HttpResponse('data invalid')
    return render(request,'insert_AccessRecords.html',d)