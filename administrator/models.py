from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Services(models.Model):
    id = models.AutoField(primary_key=True)
    Service_Name=models.CharField(max_length=50,null=True, blank=True)
    Sales_count=models.IntegerField(null=True, blank=True)
    Duration_Service=models.DurationField(null=True, blank=True)
    Charges=models.IntegerField(null=True, blank=True)
    def __str__(self):
        id_f=str(self.Service_Name+"["+(str(self.Charges))+"]")
        return id_f


class Agent(models.Model):
    id=models.AutoField(primary_key=True)
    Agent_user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='Agent')
    mobile = models.CharField(max_length=12,null=True, blank=True)
    Sales_count=models.IntegerField(null=True, blank=True)
    Client_count=models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.Agent_user.username