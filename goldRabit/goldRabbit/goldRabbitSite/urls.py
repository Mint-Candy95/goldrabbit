from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'goldRabbiSite'
urlpatterns = [
    path('', views.goldrabbit_main, name='main'),
    path('success', views.success, name='success'),
    path('wait', views.wait, name='wait'),
    path('delete', views.delete, name='delete'),
    path('reservate/',views.goldrabbit_reservate, name="reservate"),
    path('reservate_noti/',views.goldrabbit_reservate_noti, name="reservate_noti"),
    path('notify/', views.goldrabbit_notification, name="notify"),
    path('notify/<int:noti_num>', views.goldrabbit_notificationDetail, name="notify"),
    path('myreserved/', views.goldrabbit_myreserved, name="myreserved"),
    path('myreservedResult/', views.goldrabbit_myreservedResult, name="myreservedResult"),
    path('contact/', views.goldrabbit_contact, name="contact"),
    path('howto/', views.goldrabbit_howto, name="howto"),
    path('album/', views.goldrabbit_album, name="album"),
    path('admin/', auth_views.LoginView.as_view(template_name="goldRabbitSite/admin.html"), name="admin"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    
]
