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
    context = {
        'init_date' : init_date
    }
    return render(request, 'goldRabbitSite/reservate.html', context)

def goldrabbit_reservate_noti(request) :
    if request.method == 'POST' :
        name = request.POST.get('username')        
        pwd = request.POST.get('password')        
        date = request.POST.get('date')        
        start = request.POST.get('start')        
        end = request.POST.get('end')        
        cost = request.POST.get('cost')        
        anony = request.POST.get('anony')
        person = request.POST.get('people_num')
        Reserved.objects.create(reserved_name=name, reserved_date=date, reserved_pwd=pwd, reserved_start = start,
                                reserved_end = end, reserved_price = cost,reserved_status='wait',reserved_unknown=anony,
                                reserved_person=person)

    context = {
        'nickname' : name, 'pwd':pwd
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
    if request.method == "POST" :
        return goldrabbit_myreservedResult(request)

    return render(request, 'goldRabbitSite/myReserve.html',)

def goldrabbit_myreservedResult(request) :
    reserv_list = None
    if request.method == 'POST' :
        nick = request.POST.get('nickname')
        pwd = request.POST.get('pwd')
        
        reserv_list = Reserved.objects.all().filter(reserved_name=nick, reserved_pwd = pwd).values()
    if len(reserv_list) == 0 :
        context = {
            'msg' : '일치하는 정보가 없습니다.'
        }
        return render(request, 'goldRabbitSite/myReserve.html',context)

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

def success(request) :
    reserv_id = request.POST.get('id')
    reserv = Reserved.objects.get(id=reserv_id)
    reserv.reserved_status = 'success'
    reserv.save()
    return goldrabbit_main(request)

def wait(request) :
    reserv_id = request.POST.get('id')
    reserv = Reserved.objects.get(id=reserv_id)
    reserv.reserved_status = 'wait'
    reserv.save()
    return goldrabbit_main(request)

def delete(request) :
    reserv_id = request.POST.get('id')
    reserv = Reserved.objects.get(id=reserv_id)
    reserv.delete()
    return goldrabbit_main(request)