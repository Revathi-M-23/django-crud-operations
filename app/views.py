from django.shortcuts import render
from app.models import *
# Create your views here.
def display_topic(request):
    LoT=Topic.objects.all()
    d={'topics':LoT}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    LOW=Webpage.objects.all()
    d={'webpages':LOW}
    return render(request,'display_webpage.html',d)
def display_accessrecords(request):
    LOA=AccessRecords.objects.all()
    d={'records':LOA}
    return render(request,'display_accessrecords.html',d)




