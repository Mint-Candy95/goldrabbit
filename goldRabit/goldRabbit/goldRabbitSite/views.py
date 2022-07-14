from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Reserved, Notification
from django.core.paginator import Paginator

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

def goldrabbit_reservate(request) :
    
    context = {
        
    }
    return render(request, 'goldRabbitSite/reservate.html', context)

def goldrabbit_notification(request) :
    page = request.GET.get('page', '1')
    notifyList = Notification.objects.order_by('-noti_date').values()
    paginator = Paginator(notifyList, 10)
    page_obj = paginator.get_page(page)

    context = {
        'notifyList' : page_obj
    }
    return render(request, 'goldRabbitSite/notification.html', context)
    
def goldrabbit_notificationDetail(request,noti_num) :
    
    notify = Notification.objects.get(id=noti_num)
    context = {
        'notify' : notify
    }
    return render(request, 'goldRabbitSite/notification_detail.html', context)

def goldrabbit_myreserved(request) :
    
    context = {
        
    }
    return render(request, 'goldRabbitSite/myReserve.html', context)

def goldrabbit_contact(request) :
    
    context = {
        
    }
    return render(request, 'goldRabbitSite/contact.html', context)

def goldrabbit_howto(request) :
    
    context = {
        
    }
    return render(request, 'goldRabbitSite/howto.html', context)

def goldrabbit_album(request) :
    
    context = {
        
    }
    return render(request, 'goldRabbitSite/album.html', context)