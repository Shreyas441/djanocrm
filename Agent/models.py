from django.db import models
from django.db import models
from administrator.models import Services,Agent
from django.contrib.auth.models import User
# Create your models here.
request_CHOICES=(
	('Pending','Pending'),
	('Rejected','Rejected'),
	('Approved','Approved'),

)

CHOICES=(
	('Client','Client'),
	('Lead','Lead'),
    ('Free','Free'),
	
)
CHOICE_Ref=	(
    ('Website','Website'),
	('Social Media','Social Media'),
	('Marketing','Marketing'),
    ('Other','Other'),
)
CHOICE_Ref1=	(
    ('Gpay','Gpay'),
	('Bank Transfer','Bank Transfer'),
	('Paytm','Paytm'),
    ('Online Transfer',' Online Transfer'),
    ('Cash','Cash'),
    ('Other','Other'),
)

state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50,null=True, blank=True)
    mobile = models.CharField(max_length=10,null=True, blank=True)
    Whatsappmobile = models.CharField(max_length=10,null=True, blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    City=models.CharField(max_length=50,null=True, blank=True)
    State=models.CharField(choices=state_choices,max_length=50,null=True, blank=True)
    GST_NUM=models.CharField(max_length=15,null=True, blank=True)
    lead_status=models.CharField(choices = CHOICES,max_length=10,default='Lead')
    Agent_Name=models.ForeignKey(Agent,on_delete=models.SET_NULL,related_name='agent_name',null=True, blank=True)
    lead_ref=models.CharField(choices = CHOICE_Ref,max_length=15,default='Social Media')
    Demat_account=models.CharField(max_length=40,null=True, blank=True)
    lead_ref_extra=models.CharField(max_length=50,null=True, blank=True)
    def __str__(self):
        id_f=str(self.Name+"["+(str(self.id))+"]")
        return id_f


class Services_taken(models.Model):
    id = models.AutoField(primary_key=True)
    Name=models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='customer_name')
    Service=models.ForeignKey(Services, on_delete=models.CASCADE,related_name='Service_name')
    Start_date=models.DateField(null=True, blank=True)
    End_date=models.DateField(null=True, blank=True)
    GST=models.IntegerField(null=True, blank=True)
    days_left=models.DurationField(null=True, blank=True)
    Tot_payement=models.IntegerField(null=True, blank=True)
    payment_reference_number=models.CharField(max_length=125)
    payment_mode=models.CharField(choices = CHOICE_Ref1,max_length=50,default='Other')
    def __str__(self):
        id_s=str(self.Name.Name+ " [ "+self.Service.Service_Name+"("+(str(self.id))+") ]")
        return id_s


class Services_taken_request(models.Model):
    id = models.AutoField(primary_key=True)
    Service=models.ForeignKey(Services, on_delete=models.CASCADE,related_name='Service_name_request')
    status=models.CharField(choices = request_CHOICES,max_length=15,default='Pending')
    Name=models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='customer_name_request')
    def __str__(self):
        id_s=str(self.Name.Name+ " [ "+self.Service.Service_Name+"("+(str(self.id))+") ]")
        return id_s
    