
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth,Group
from django.contrib.auth import  authenticate,login,logout
from django.contrib import messages
from administrator.decorator import *
from administrator.models import Agent,Services
from Agent.forms import Services_Form,Service_Taken_Form,CustomerForm,CustomerForm_update,Services_request_Form,Service_Taken_Form_update
from .models import Customer,Services_taken,Services_taken_request
from datetime import datetime
from django.core.paginator import Paginator,EmptyPage

#Agent Dashboard Function 
@allowed_users(allowed_roles=['Agent'])
@authenticated_user
def Agent_home(request):
	users=request.user
	Agents_a=Agent.objects.get(Agent_user=users)
	Customer_a=Customer.objects.filter(Agent_Name=Agents_a)
	Customer_a_b=Customer.objects.filter(Agent_Name=Agents_a,lead_status="Lead").count()
	Customer_a_c=Customer.objects.filter(Agent_Name=Agents_a,lead_status="Free").count()
	c=0
	for m in Customer_a:
		Services_taken_s=Services_taken.objects.filter(Name=m)
		c=c+Services_taken_s.count()
	Agents_a.Client_count=Customer_a.count()
	Agents_a.Sales_count=c
	Agents_a.save()
	context = {'Customer_a_b':Customer_a_b,'Customer_a_c':Customer_a_c,'Agents_a':Agents_a}
	return render(request,'Agent/Agent_home.html',context)

#Agent's Lead Showing Function 
@allowed_users(allowed_roles=['Agent'])
@authenticated_user
def Agent_Lead(request):
	users=request.user
	Agents_a=Agent.objects.get(Agent_user=users)
	Customer_lead=Customer.objects.filter(Agent_Name=Agents_a,lead_status="Lead").order_by('id')
	Page_n=request.GET.get('Customer_lead',1)
	Customer_lead_view=Paginator(Customer_lead,10)
	try:
		page=Customer_lead_view.page(Page_n)
	except EmptyPage:
		page=Customer_lead_view.page(1)
	context = {'Customer_lead':page}
	return render(request,'Agent/Agent_Lead.html',context)
	

#Agent's Lead With Trial Showing Function
@allowed_users(allowed_roles=['Agent'])
@authenticated_user
def Agent_Lead_trail(request):
	users=request.user
	Agents_a=Agent.objects.get(Agent_user=users)
	Customer_Trial=Customer.objects.filter(Agent_Name=Agents_a,lead_status="Free").order_by('id')
	Page_n=request.GET.get('Customer_Trial',1)
	Customer_Trial_view=Paginator(Customer_Trial,10)
	try:
		page=Customer_Trial_view.page(Page_n)
	except EmptyPage:
		page=Customer_Trial_view.page(1)
	context = {'Customer_Trial':page}
	return render(request,'Agent/Agent_Free.html',context)

#Agent's Leads Trial services Showing Function
@allowed_users(allowed_roles=['Agent'])
@authenticated_user
def Agent_trail(request):
	users=request.user
	Agents_a=Agent.objects.get(Agent_user=users)
	Customer_a_b=Customer.objects.filter(Agent_Name=Agents_a,lead_status="Free")
	Services_takenc=Services_taken.objects.filter(Name__id__in=Customer_a_b.all()).order_by('id')
	Page_n=request.GET.get('Services_takenc',1)
	Services_takenc_view=Paginator(Services_takenc,10)
	try:
		page=Services_takenc_view.page(Page_n)
		a = datetime.now().date()
		for i in page:
			date_format = "%Y-%m-%d"
			b = datetime.strptime(str(i.End_date), date_format)
			a = datetime.strptime(str(datetime.now().date()), date_format)
			diff = b-a
			i.days_left=diff
			i.save()
	except EmptyPage:
		page=Services_takenc_view.page(1)
	context = {'Services_takenc':page}
	return render(request,'Agent/Agent_trail.html',context)


#Agent's Leads Trial requests Showing Function
@allowed_users(allowed_roles=['Agent'])
@authenticated_user
def Agent_trail_request(request):
	users=request.user
	Agents_a=Agent.objects.get(Agent_user=users)
	Customer_a=Customer.objects.filter(Agent_Name=Agents_a)
	Services_taken_request_a=Services_taken_request.objects.filter(Name__id__in=Customer_a.all()).order_by('id')
	Page_n=request.GET.get('Services_taken_request_a',1)
	Services_taken_request_a_view=Paginator(Services_taken_request_a,10)
	try:
		page=Services_taken_request_a_view.page(Page_n)
	except EmptyPage:
		page=Services_taken_request_a_view.page(1)
	context = {'Services_taken_request_a':page}
	return render(request,'Agent/Agent_trail_request.html',context)
	
def Agent_login(request):
	if request.method == 'POST':
		username = request.POST['usernames']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request, user)
			return redirect('Agent_home')
		else:
			return render(request,'Agent/Agent_Signin.html',{'i':'Invalid username or Password'})

	else:
		return render(request,'Agent/Agent_Signin.html')


#Customer Addition Form
@allowed_users(allowed_roles=['Agent'])
@authenticated_user
def client_add(request):
	form=CustomerForm()
	users=request.user
	Agents_a=Agent.objects.get(Agent_user=users)
	if request.method == 'POST':
		State1 = request.POST['State1']
		form=CustomerForm(request.POST)
		if form.is_valid():
			client_a=form.save(commit=False)
			m=client_a.mobile
			mw=client_a.Whatsappmobile
			if Customer.objects.filter(mobile=m).exists():
				messages.info(request,'Phone number already exists')
				return redirect('Agent_home')
			elif Customer.objects.filter(Whatsappmobile=mw).exists():
				messages.info(request,'Phone number already exists')
				return redirect('Agent_home')
			else:
				client_a.Agent_Name=Agents_a
				client_a.lead_ref_extra=State1
				client_a.save()
				messages.info(request,'Client Added')
				return redirect('Agent_home')
	context = {'form':form}
	return render(request, 'Agent/Client_add.html', context)

#Customer Update Form
@allowed_users(allowed_roles=['Agent'])
@authenticated_user
def client_Update(request,pk):
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
		
			return redirect('Agent_home')
	context = {'form':form,'Customer_c':Customer_c}
	return render(request, 'Agent/client_Update.html', context)

#Customer Delete Funtion
@allowed_users(allowed_roles=['Agent'])
@authenticated_user
def client_Delete(request,pk):
	Customer_c=Customer.objects.get(id=pk)
	if request.method == "POST":
		Customer_c.delete()
		messages.info(request,'Client Deleted')
		return redirect("Agent_home")
	context = {'Customer_c':Customer_c}
	return render(request, 'Agent/Agent_client_delete.html', context)

#Service saled Add Function 
@allowed_users(allowed_roles=['Agent'])
@authenticated_user
def Service_taken_add(request):
	form=Service_Taken_Form()
	if request.method == 'POST':
		form=Service_Taken_Form(request.POST)
		if form.is_valid():
			Services_taken_add=form.save(commit=False)
			Services_taken_add.Tot_payement=(Services_taken_add.Service.Charges+(Services_taken_add.Service.Charges*(Services_taken_add.GST/100)))
			Related_customer=Services_taken_add.Name
			Services_taken_add.Name.lead_status='Client'
			Services_taken_add.End_date=Services_taken_add.Start_date+Services_taken_add.Service.Duration_Service
			print(Services_taken_add.End_date)
			Related_customer.save()
			Services_taken_add.save()
			messages.info(request,'Service saled added')
			return redirect('Agent_home')
	context = {'form':form}
	return render(request, 'Agent/Service_taken_add.html', context)

#Service saled Update Function 
@allowed_users(allowed_roles=['Agent'])
@authenticated_user
def Service_taken_Update(request,pk):
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
			return redirect('Agent_home')
	context = {'form':form,'Services_taken_c':Services_taken_c}
	return render(request, 'Agent/Service_taken_Update.html', context)

#Service saled delete Function 
@allowed_users(allowed_roles=['Agent'])
@authenticated_user
def Service_taken_delete(request,pk):
	Services_taken_d=Services_taken.objects.get(id=pk)
	if request.method == "POST":
		service_count=Services_taken_d.Name
		Services_taken_d.delete()
		a=Services_taken.objects.filter(Name=service_count).count()
		if(a==0):
			service_count.lead_status='Lead'
			service_count.save()
		
		messages.info(request,'Service delete')
		return redirect("Agent_home")
	context = {'Services_taken_d':Services_taken_d}
	return render(request, 'Agent/Agent_service_delete.html', context)

#Service Request Add Function 	
@allowed_users(allowed_roles=['Agent'])
@authenticated_user
def Service_taken_request(request):
	form=Services_request_Form()
	if request.method == 'POST':
		form=Services_request_Form(request.POST)
		if form.is_valid():
			form.save()
			messages.info(request,'Service requested')
			return redirect('Agent_home')
	context = {'form':form}
	return render(request, 'Agent/Service_taken_request.html', context)
	
	



