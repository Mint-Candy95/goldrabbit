from django.urls import path

from . import views

app_name = 'goldRabbiSite'
urlpatterns = [
    path('', views.goldrabbit_main, name='main'),
    path('reserved/',views.goldrabbit_reserved_page1, name="reservation"),
    path('reserved2/', views.goldrabbit_reserved_page2, name="reservation2"),
    path('myreserved/', views.goldrabbit_myreserved, name="myreserved")
]