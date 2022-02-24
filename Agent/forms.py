
from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields=['Name','mobile','email','City','State','Whatsappmobile','GST_NUM','lead_ref','Demat_account']
		widgets = {
			'Name' : forms.TextInput(attrs={'class':'form-control my-2','required':'required','placeholder':"Name Of client"}),
			'Whatsappmobile': forms.TextInput(attrs={'class':'form-control my-2','id':'mobile1','required':'required', 'placeholder':" Whatsapp Number of client",'maxlength':10,'minlength':10,'onchange':"check2(this.value)"}),
            'mobile' : forms.TextInput(attrs={'class':'form-control my-2','id':'mobile','required':'required', 'placeholder':"Mobile Number of client",'maxlength':"10",'minlength':"10",'onchange':"check(this.value)"}),
			'email': forms.TextInput(attrs={'class':'form-control my-2','required':'required', 'placeholder':"Email id of client"}),
            'City' : forms.TextInput(attrs={'class':'form-control my-2','required':'required', 'placeholder':"City of client "}),
			'State' : forms.Select(attrs={'class':'form-control my-2','required':'required', 'placeholder':" State of client"}),
            'GST_NUM':forms.TextInput(attrs={'class':'form-control my-2','required':'required', 'placeholder':" GST number of client "}),
			'Demat_account':forms.TextInput(attrs={'class':'form-control my-2','required':'required','placeholder':"Name of demat account (ex.angle) write NAN if not having ac"}),
            'lead_ref':forms.Select(attrs={'class':'form-control my-2','required':'required', 'placeholder':"reference",'onchange':"display(this.value)", 'id':"id_lead_ref"}),
		}

class CustomerForm_update(forms.ModelForm):
	class Meta:
		model = Customer
		fields=['mobile','email','City','State','Whatsappmobile','GST_NUM','lead_ref','Demat_account']
		widgets = {
			'mobile' : forms.TextInput(attrs={'class':'form-control my-2','id':'mobile','required':'required','onchange':"check(this.value)"}),
			'email': forms.EmailInput(attrs={'class':'form-control my-2','required':'required'}),
            'Whatsappmobile' : forms.TextInput(attrs={'class':'form-control my-2','id':'mobile1','required':'required','maxlength':10,'minlength':10,'onchange':"check2(this.value)"}),
            'City' : forms.TextInput(attrs={'class':'form-control my-2','required':'required'}),
			'State' : forms.Select(attrs={'class':'form-control my-2','required':'required'}),
            'GST_NUM':forms.TextInput(attrs={'class':'form-control my-2','required':'required'}),
			'Demat_account':forms.TextInput(attrs={'class':'form-control my-2','required':'required'}),
            'lead_ref':forms.Select(attrs={'class':'form-control my-2','required':'required','onchange':"display(this.value)", 'id':"id_lead_ref"}),
		}

class Service_Taken_Form(forms.ModelForm):
	class Meta:
		model = Services_taken
		fields=['Name','Start_date','GST','payment_reference_number','payment_mode','Service']
		widgets = {
			'Name' : forms.Select(attrs={'class':'form-control   my-2','required':'required'}),
            'Start_date' :DateInput(attrs={'class':'form-control   my-2','required':'required'}),
            'Service' : forms.Select(attrs={'class':'form-control   my-2','required':'required'}),
            'payment_reference_number' : forms.TextInput(attrs={'class':'form-control   my-2','required':'required','placeholder':"Add Payment reference number"}),
			'payment_mode':forms.Select(attrs={'class':'form-control   my-2','required':'required'}),
			'GST': forms.NumberInput(attrs={'class':'form-control   my-2','required':'required', 'placeholder':"Add Persent of GST 0-100"}),

		}

class Service_Taken_Form_update(forms.ModelForm):
	class Meta:
		model = Services_taken
		fields=['Start_date','GST','payment_reference_number','payment_mode']
		widgets = {
			'Start_date' :DateInput(attrs={'class':'form-control   my-2','required':'required'}),
            
            'payment_reference_number' : forms.TextInput(attrs={'class':'form-control   my-2','required':'required','placeholder':"Add Payment reference number"}),
			'payment_mode':forms.Select(attrs={'class':'form-control   my-2','required':'required'}),
			'GST': forms.NumberInput(attrs={'class':'form-control   my-2','required':'required', 'placeholder':"Add Persent of GST 0-100"}),
			
		}

class Services_Form_new(forms.ModelForm):
	class Meta:
		model = Services
		fields=['Service_Name','Charges']
		widgets = {
			'Service_Name' : forms.TextInput(attrs={'class':'form-control my-2','required':'required'}),
            'Charges':forms.NumberInput(attrs={'class':'form-control  my-2','required':'required'}),
            
		}

class Services_Form(forms.ModelForm):
	class Meta:
		model = Services
		fields=['Service_Name','Charges','Duration_Service']
		widgets = {
			'Service_Name' : forms.TextInput(attrs={'class':'form-control my-2','required':'required'}),
			'Duration_Service':forms.TextInput(attrs={'class':'form-control my-2','required':'required','placeholder':"Add in the format days hours:min (if only days keep hours:min as 00:00) "}),
            'Charges':forms.NumberInput(attrs={'class':'form-control  my-2','required':'required'}),
            
		}


class AgentForm(forms.ModelForm):
	class Meta:
		model = Agent
		fields=['Agent_user','mobile']
		widgets = {
            'mobile':forms.NumberInput(attrs={'class':'form-control  my-2','required':'required'}),
		}



class Services_request_Form(forms.ModelForm):
	class Meta:
		model = Services_taken_request
		fields=['Service','Name']
		widgets = {
			'Service' : forms.Select(attrs={'class':'form-control  my-2','required':'required'}),
            'Name' : forms.Select(attrs={'class':'form-control  my-2','required':'required'}),
            
		}


class Service_trial_Taken_Form(forms.ModelForm):
	class Meta:
		model = Services_taken
		fields=['Start_date','End_date']
		widgets = {
            'Start_date' :DateInput(attrs={'class':'form-control my-2','required':'required'}),
            'End_date' : DateInput(attrs={'class':'form-control my-2','required':'required'}),

		}