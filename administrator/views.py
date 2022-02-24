from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth,Group
from django.contrib.auth import  authenticate,login,logout
from .models import Agent,Services
from django.contrib import messages
from administrator.decorator import *
from Agent.models import Customer,Services_taken,Services_taken_request
from Agent.forms import Services_Form,Service_Taken_Form,CustomerForm,Service_trial_Taken_Form,CustomerForm_update,Service_Taken_Form_update,Services_Form_new
from datetime import datetime,timedelta
from django.core.paginator import Paginator,EmptyPage


#Home Page Function 	
def home(request):
	return render(request,'administrator/Home.html')

def logout_view(request):
	logout(request)
	return redirect('home')

#Administrator Home Page Function
@allowed_users(allowed_roles=['Administrator'])
@authenticated_user 
def administrator_home(request):
	Services_s=Services.objects.all().count()
	Customer_a=Customer.objects.filter(lead_status="Client")
	Customer_b=Customer.objects.filter(lead_status="Free")
	t=Customer.objects.filter(lead_status="Lead")
	total_Lead=t.count()+Customer_b.count()
	total_client=Customer_a.count()
	Services_taken_request_a=Services_taken_request.objects.all().count()
	context = {'Services_s':Services_s,'total_Lead':total_Lead,
	'total_client':total_client,'Services_taken_request_a':Services_taken_request_a}
	return render(request,'administrator/Administrator_home.html',context)


#Administrator Service sale report Function
@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def service_sales(request):
	Services_s=Services.objects.all().order_by('id')
	Page_n=request.GET.get('Services_s',1)
	Services_s_view=Paginator(Services_s,10)
	try:
		page=Services_s_view.page(Page_n)
		for i in page:
			Services_taken_s=Services_taken.objects.filter(Service=i)
			i.Sales_count=Services_taken_s.count()
			i.save()
	except EmptyPage:
		page=Services_s_view.page(1)
	context = {'Services_s':page}
	return render(request,'administrator/Administrator_service_sales.html',context)

#saled Services details Function
@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def service_sales_report(request):
	Services_takenc=Services_taken.objects.all().order_by('id')
	Page_n=request.GET.get('Services_takenc',1)
	Services_takenc_view=Paginator(Services_takenc,10)
	try:
		page=Services_takenc_view.page(Page_n)
		a = datetime.now().date()
		for j in page:
			date_format = "%Y-%m-%d"
			b = datetime.strptime(str(j.End_date), date_format)
			a = datetime.strptime(str(datetime.now().date()), date_format)
			diff = b-a
			j.days_left=diff
			j.save()
	except EmptyPage:
		page=Services_takenc_view.page(1)
	context = {'Services_takenc':page}
	return render(request,'administrator/Administrator_service_sales_report.html',context)


#Agent Performance details Function
@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def Agent_report(request):
	Agents_b=Agent.objects.all().order_by('id')
	Page_n=request.GET.get('Agents_b',1)
	Agents_b_view=Paginator(Agents_b,10)
	try:
		page=Agents_b_view.page(Page_n)
		for Agents_a in page:
			c=0
			Customer_a=Customer.objects.filter(Agent_Name=Agents_a)
			for m in Customer_a:
				Services_taken_s=Services_taken.objects.filter(Name=m)
				c=c+Services_taken_s.count()
			Agents_a.Client_count=Customer_a.count()
			Agents_a.Sales_count=c
			Agents_a.save()
	except EmptyPage:
		page=Agents_b_view.page(1)
	context = {'Agents_b':page}
	return render(request,'administrator/Administrator_Agent_report.html',context)


#Service Request details
@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def Services_taken_request_details(request):
	Services_taken_request_b=Services_taken_request.objects.all().order_by('id')
	Page_n=request.GET.get('Services_taken_request_b',1)
	Services_taken_request_view=Paginator(Services_taken_request_b,10)
	try:
		page=Services_taken_request_view.page(Page_n)
	except EmptyPage:
		page=Services_taken_request_view.page(1)

	context = {'Services_taken_request_b':page}
	return render(request,'administrator/Administrator_Services_taken_request.html',context)


#Leads Details
@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def Lead_details(request):
	total_Lead=Customer.objects.filter(lead_status="Lead").order_by('id')
	Page_n=request.GET.get('total_Lead',1)
	total_Lead_view=Paginator(total_Lead,10)
	try:
		page=total_Lead_view.page(Page_n)

	except EmptyPage:
		page=total_Lead_view.page(1)
	
	context = {'total_Lead':page}
	
	return render(request,'administrator/Administrator_Lead.html',context)

#Leads on trial Details
@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def Trail_details(request):
	total_Free=Customer.objects.filter(lead_status="Free").order_by('id')
	Page_n=request.GET.get('total_Free',1)
	total_Free_view=Paginator(total_Free,10)
	try:
		page=total_Free_view.page(Page_n)

	except EmptyPage:
		page=total_Free_view.page(1)
	
	context = {'total_Free':page}
	return render(request,'administrator/Administrator_Free.html',context)

#Client details function
@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def Client_details(request):
	total_Client=Customer.objects.filter(lead_status="Client")
	Page_n=request.GET.get('total_Client',1)
	total_Client_view=Paginator(total_Client,10)
	try:
		page=total_Client_view.page(Page_n)

	except EmptyPage:
		page=total_Client_view.page(1)

	
	context = {'total_Client':page}
	return render(request,'administrator/Administrator_Client.html',context)

#Client Update function
@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def administrator_client_Update(request,pk):
	Customer_c=Customer.objects.get(id=pk)
	form=CustomerForm_update(instance=Customer_c)
	if request.method == 'POST':
		State1 = request.POST['State1']
		client_a=form.save(commit=False)
		client_a.lead_ref_extra=State1
		client_a.save()
		form=CustomerForm_update(request.POST,instance=Customer_c)
		if form.is_valid():
			form.save()
			messages.info(request,'Client Updated')
			return redirect('administrator_home')
	context = {'form':form,'Customer_c':Customer_c}
	return render(request, 'administrator/administrator_client_Update.html', context)


#Client Update function
@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def administrator_client_delete(request,pk):
	Customer_c=Customer.objects.get(id=pk)
	if request.method == "POST":
		Customer_c.delete()
		messages.info(request,'Client Deleted')
		return redirect("administrator_home")
	context = {'Customer_c':Customer_c}
	return render(request, 'administrator/administrator_client_delete.html', context)



@allowed_users(allowed_roles=['Administrator'])
def Agent_Signup(request):
	if request.method == 'POST':
		username = request.POST['username1'] 
		first_name = request.POST['First_name']
		last_name = request.POST['Last_name']
		email = request.POST['Email']
		password1 = request.POST['password']
		password2 = request.POST['password2']
		Mobile = request.POST['Mobile']
		if password1==password2:
			if User.objects.filter(username=username).exists():
				return render(request,'administrator/Agent_Signup.html',{'i':'user already exsist'})
			else:
				users = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
				group = Group.objects.get(name= 'Agent')
				group.user_set.add(users)
				users.save()
				users_a = User.objects.get(username=username)
				Agent_n=Agent(Agent_user=users_a,mobile=Mobile,Client_count=0,Sales_count=0)
				Agent_n.save()
				return redirect('administrator_home')
		else:
			return render(request,'administrator/Agent_Signup.html',{'i':'Passwords are not same'})
	else:
		return render(request,'administrator/Agent_Signup.html')

def administrator_login(request):
	if request.method=='POST':
		username = request.POST['usernames']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request, user)
			return redirect('administrator_home')
		else:
			return render(request,'administrator/administrator_Signin.html',{'i':'Invalid username or Password'})

	else:
		return render(request,'administrator/administrator_Signin.html')


def administrator_Signup(request):
	if request.method == 'POST':
		first_name = request.POST['First_name']
		last_name = request.POST['Last_name']
		username = request.POST['username']
		email = request.POST['Email']
		password1 = request.POST['password']
		password2 = request.POST['password2']
		if password1==password2:
			if User.objects.filter(username=username).exists():
				return render(request,'administrator/administrator_Signup.html',{'i':'user already exsist'})
			else:
				users = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
				group = Group.objects.get(name='Administrator')
				group.user_set.add(users)
				users.save()
				return redirect('administrator_home')
		return render(request,'administrator/administrator_Signup.html',{'i':'Passwords are not same'})
	else:
		return render(request,'administrator/administrator_Signup.html')

#Service Add Function
@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def service_add(request):
	form=Services_Form()
	if request.method == 'POST':
		form=Services_Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('administrator_home')
		else:
			return render(request, 'administrator/administrator_service_add.html', {'i':'somthing went wrong'})
	context = {'form':form}
	return render(request, 'administrator/administrator_service_add.html', context)


#Service Update Function
@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def service_update(request,pk):
	service_u=Services.objects.get(id=pk)
	form=Services_Form(instance=service_u)
	if request.method == 'POST':
		form=Services_Form(request.POST,instance=service_u)
		if form.is_valid():
			form.save()
			return redirect('administrator_home')
	context = {'form':form}
	return render(request, 'administrator/administrator_service.html', context)

#Service Delete Function
@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def service_delete(request,pk):
	Services_delete= Services.objects.get(id=pk)
	if request.method == "POST":
		Services_delete.delete()
		return redirect("administrator_home")
	context = {'Services_delete':Services_delete}
	return render(request, 'administrator/administrator_service_delete.html', context)

#approve trial Function
@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def approve_trial(request,pk):
	Services_taken_request_a=Services_taken_request.objects.get(id=pk)
	form=Service_trial_Taken_Form()
	if request.method == "POST":
		form=Service_trial_Taken_Form(request.POST)
		Services_taken_request_add=form.save(commit=False)
		Services_taken_request_add.Tot_payement=0
		Services_taken_request_add.Name=Services_taken_request_a.Name
		client=Services_taken_request_add.Name
		if(client.lead_status=='Lead'):
			client.lead_status='Free'
		Services_taken_request_add.Service=Services_taken_request_a.Service
		client.save()
		Services_taken_request_a.status='Approved'
		Services_taken_request_a.save()
		Services_taken_request_add.save()
		messages.info(request,'trial Approved')
		return redirect('administrator_home')
	context = {'form':form,'Services_taken_request_a':Services_taken_request_a}
	return render(request, 'administrator/Administartor_service_request.html', context)

#Service Request Delete Function 			
@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def Delete_trial(request,pk):
	Services_taken_request_a=Services_taken_request.objects.get(id=pk)
	if request.method == "POST":
		Services_taken_request_a.delete()
		messages.info(request,'trial not Approved')
		return redirect('administrator_home')
	context = {'Services_taken_request_a':Services_taken_request_a}
	return render(request, 'administrator/Administartor_service_request_delete.html', context)


#Service Request Rejection Function 	
@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def Reject_trial(request,pk):
	Services_taken_request_a=Services_taken_request.objects.get(id=pk)
	if request.method == "POST":
		Services_taken_request_a.status='Rejected'
		Services_taken_request_a.save()

		messages.info(request,'trial Rejected')
		return redirect('administrator_home')
	context = {'Services_taken_request_a':Services_taken_request_a}
	return render(request, 'administrator/Administartor_service_request_Reject.html', context)

# Saled service Add Function
@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def admin_Service_taken_add(request):
	form=Service_Taken_Form()
	if request.method == 'POST':
		form=Service_Taken_Form(request.POST)
		if form.is_valid():
			Services_taken_add=form.save(commit=False)
			Services_taken_add.Tot_payement=(Services_taken_add.Service.Charges+(Services_taken_add.Service.Charges*(Services_taken_add.GST/100)))
			Related_customer=Services_taken_add.Name
			Related_customer.lead_status='Client'
			Services_taken_add.End_date=Services_taken_add.Start_date+Services_taken_add.Service.Duration_Service
			Related_customer.save()
			Services_taken_add.save()
			messages.info(request,'Service saled added')
			return redirect('administrator_home')
	context = {'form':form}
	return render(request, 'administrator/admin_Service_taken_add.html', context)

# Saled service Update Function
@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def admin_Service_taken_Update(request,pk):
	Services_taken_c=Services_taken.objects.get(id=pk)
	form=Service_Taken_Form_update(instance=Services_taken_c)
	if request.method == 'POST':
		form=Service_Taken_Form_update(request.POST,instance=Services_taken_c)
		if form.is_valid():
			Services_taken_add=form.save(commit=False)
			Services_taken_add.Tot_payement=Services_taken_add.Service.Charges+(Services_taken_add.Service.Charges*(Services_taken_add.GST/100))
			Services_taken_add.End_date=Services_taken_add.Start_date+Services_taken_add.Service.Duration_Service
			Services_taken_add.save()
			messages.info(request,'Service Updated')
			return redirect('administrator_home')
	context = {'form':form,'Services_taken_c':Services_taken_c}
	return render(request, 'administrator/admin_Service_taken_Update.html', context)


# Saled service delete Function
@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def admin_Service_taken_delete(request,pk):
	Services_taken_d=Services_taken.objects.get(id=pk)
	if request.method == "POST":
		service_count=Services_taken_d.Name
		Services_taken_d.delete()
		a=Services_taken.objects.filter(Name=service_count).count()
		if(a==0):
			service_count.lead_status='Lead'
			service_count.save()
		messages.info(request,'Service delete')
		return redirect("administrator_home")
	context = {'Services_taken_d':Services_taken_d}
	return render(request, 'administrator/admin_service_delete.html', context)



def validate_username(request):
	if request.method == 'GET':
		users = list(User.objects.values_list('username', flat=True)) 
		username = {'usernames':users}
		return JsonResponse(username)

# Analysis
@allowed_users(allowed_roles=['Administrator'])
@authenticated_user	
def Revenue(request):
	Services_taken_s=Services_taken.objects.all()
	Customer_a=Customer.objects.filter(lead_ref="Website").count()
	Customer_b=Customer.objects.filter(lead_ref="Social Media").count()
	Customer_c=Customer.objects.filter(lead_ref="Marketing").count()
	Customer_d=Customer.objects.filter(lead_ref="Other").count()
	a = datetime.now().date()
	b=datetime.now().date() - timedelta(7)
	c=datetime.now().date() - timedelta(30)
	d=datetime.now().date() - timedelta(365)
	mounth_revenue=week_revenue=Year_revenue=total_revenue=Gpay_count=Other_count=paytm_count=bank_count=online_count=0
	for n in Services_taken_s:
		if(b<n.Start_date<=a):
			week_revenue=week_revenue+n.Service.Charges
		if(c<n.Start_date<=a):
			mounth_revenue=mounth_revenue+n.Service.Charges
		if(d<n.Start_date<=a):
			Year_revenue=Year_revenue+n.Service.Charges
		if(n.payment_mode=="Gpay"):
			Gpay_count=Gpay_count+1
		elif(n.payment_mode=="Bank Transfer"):
			bank_count=bank_count+1
		elif (n.payment_mode=="Paytm"):
			paytm_count=paytm_count+1
		elif (n.payment_mode=="Online Transfer"):
			online_count=online_count+1
		elif (n.payment_mode=="Other"):
			Other_count=Other_count+1
		total_revenue=total_revenue+n.Service.Charges
	context = {'mounth_revenue':mounth_revenue,'week_revenue':week_revenue,'Year_revenue':Year_revenue,'total_revenue':total_revenue,
	'Gpay_count':Gpay_count,'Other_count':Other_count,'paytm_count':paytm_count,'bank_count':bank_count,'online_count':online_count,
	'Customer_a':Customer_a ,'Customer_b':Customer_b,'Customer_c':Customer_c,'Customer_d':Customer_d}
	return render(request, 'administrator/Administartor_Revenue.html', context)
		

