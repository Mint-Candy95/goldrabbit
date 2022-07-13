from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Reserved, User, Notification

import json

def goldrabbit_main(request) :
    reservedList = list(Reserved.objects.all().values())
    reservJson = json.dumps(reservedList)
    
    notiList = list(Notification.objects.all().values())
    notiJson = json.dumps(notiList)
    context = {
        'reservedList' : reservJson,
        'notiList' : notiJson,
        'recent_noti' : Notification.objects.order_by('-noti_date')[:1].values()
    }
    
    return render(request, 'goldRabbitSite/goldrabbit_main.html', context)

def goldrabbit_reserved_page1(request) :
    return HttpResponse("page1")

def goldrabbit_reserved_page2(request) :
    return HttpResponse("page2")

def goldrabbit_myreserved(request) :
    return HttpResponse("page3")