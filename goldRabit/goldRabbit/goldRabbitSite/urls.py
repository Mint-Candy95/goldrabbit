from django.urls import path

from . import views

app_name = 'goldRabbiSite'
urlpatterns = [
    path('', views.goldrabbit_main, name='main'),
    path('reservate/',views.goldrabbit_reservate, name="reservate"),
    path('notify/', views.goldrabbit_notification, name="notify"),
    path('myreserved/', views.goldrabbit_myreserved, name="myreserved"),
    path('contact/', views.goldrabbit_contact, name="contact"),
    path('howto/', views.goldrabbit_howto, name="howto"),
    path('album/', views.goldrabbit_album, name="album")
]