from django.shortcuts import render
from app.models import *
# Create your views here.
def display_topic(request):
    LoT=Topic.objects.all()
    d={'topics':LoT}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    #LOW=Webpage.objects.all()
    #LOW=Webpage.objects.filter(topic_name='Cricket')
    #LOW=Webpage.objects.get(topic_name='Hocky')
    LOW=Webpage.objects.filter(name='Rohit')
    LOW=Webpage.objects.filter(name='Suresh Raina')
    LOW=Webpage.objects.exclude(topic_name='Hocky')
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.order_by('name')
    LOW=Webpage.objects.order_by('topic_name')
    LOW=Webpage.objects.all()[1:3:]
    LOW=Webpage.objects.all().order_by('name')
    LOW=Webpage.objects.all().order_by('-name')
    
    d={'webpages':LOW}
    return render(request,'display_webpage.html',d)

def display_accessrecords(request):
    LOA=AccessRecords.objects.all()
    LOA=AccessRecords.objects.filter(date__gt='2023-03-05')
    LOA=AccessRecords.objects.filter(date__lt='2023-04-05')
    LOA=AccessRecords.objects.filter(date__gte='2023-03-05')
    LOA=AccessRecords.objects.filter(date__lte='2023-03-05')
    d={'records':LOA}
    return render(request,'display_accessrecords.html',d)




