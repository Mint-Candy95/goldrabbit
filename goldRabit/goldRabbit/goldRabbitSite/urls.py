from django.urls import path

from . import views

app_name = 'goldRabbiSite'
urlpatterns = [
    path('', views.goldrabbit_main, name='main'),
    path('reservate/',views.goldrabbit_reservate, name="reservate"),
    path('reservate_noti/',views.goldrabbit_reservate_noti, name="reservate_noti"),
    path('notify/', views.goldrabbit_notification, name="notify"),
    path('notify/<int:noti_num>', views.goldrabbit_notificationDetail, name="notify"),
    path('myreserved/', views.goldrabbit_myreserved, name="myreserved"),
    path('myreservedResult/', views.goldrabbit_myreservedResult, name="myreservedResult"),
    path('contact/', views.goldrabbit_contact, name="contact"),
    path('howto/', views.goldrabbit_howto, name="howto"),
    path('album/', views.goldrabbit_album, name="album"),
    path('admin/', views.goldrabbit_admin, name="admin"),
    path('adminLogin/', views.goldrabbit_adminLogin, name="adminLogin"),
    
]