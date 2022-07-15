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
    init_date = request.POST.get('select_date')
    print(request.POST)
    context = {
        'init_date' : init_date
    }
    return render(request, 'goldRabbitSite/reservate.html', context)

def goldrabbit_reservate_noti(request) :
    if request.method == 'POST' :
        ##todo
        pass
        

    context = {

    }
    return render(request, 'goldRabbitSite/reservate_noti.html', context)

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

def goldrabbit_myreservedResult(request) :
    reserv_list = None
    if request.method == 'POST' :
        nick = request.POST.get('nickname')
        pwd = request.POST.get('pwd')
        
        reserv_list = Reserved.objects.all().filter(reserved_name=nick, reserved_pwd = pwd).values()
        print(reserv_list)
    context = {
        'reserv_list' : reserv_list
    }
    return render(request, 'goldRabbitSite/myReserveResult.html', context)

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

def goldrabbit_admin(request) :
    if request=='GET' :
        
        return render(request, 'goldRabbitSite/adminLogin.html')
    if request.POST.get('pwd') != 'lovey3618' :
        context = {
            'msg' : '비밀번호가 일치하지 않습니다냥.'
        } 
        return render(request, 'goldRabbitSite/adminLogin.html', context)
    
    reservedList = list(Reserved.objects.all().values())
    reservJson = json.dumps(reservedList)
    
    notiList = list(Notification.objects.all().values())
    notiJson = json.dumps(notiList)
    context = {
        'reservedList' : reservJson,
        'notiList' : notiJson,
        'recent_noti' : Notification.objects.order_by('-noti_date')[:1].values()
    }
    return render(request, 'goldRabbitSite/admin.html', context)

def goldrabbit_adminLogin(request) :
    
    context = {
        
    }
    return render(request, 'goldRabbitSite/adminLogin.html', context)