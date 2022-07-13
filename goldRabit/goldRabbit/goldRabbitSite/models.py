from django.db import models

class Reserved(models.Model) :
    reserved_name = models.CharField(max_length=30)
    reserved_date = models.CharField(max_length=12)
    reserved_pwd = models.CharField(max_length=30)
    reserved_start = models.IntegerField()
    reserved_end = models.IntegerField()
    reserved_person = models.IntegerField(default=1, null=False)
    reserved_price = models.IntegerField(default=20000, null=False)
    reserved_status = models.CharField(max_length=10, default='wait', null=False)
    reserved_unknown = models.BooleanField(default=False)
    
    def __str__(self) :
        show = str(self.reserved_name)+" "+str(self.reserved_start)
        return show
    
class Notification(models.Model) :
    noti_title = models.CharField(max_length=50)
    noti_contents = models.CharField(max_length=2000)
    noti_date = models.CharField(max_length= 20)
    
    def __str__(self) :
        return self.noti_title