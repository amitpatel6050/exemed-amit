from django.http import HttpResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


from .forms import Contact_usForm
from .forms import Employee_regForm
from .models import Contact_us
from .models import Employee_reg
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
import datetime
from django.http import JsonResponse
import random
from django.conf import settings
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from mysite import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
# from .models import User_rgp, Rgp_entry
from django.utils import timezone


# relative import of forms
# Create your views here.


def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def findia(request):
	return render(request,'findia.html')

def celebration(request):
	return render(request,'celebration-new.html')

def career(request):
	return render(request,'career.html')

def brand(request):
	return render(request,'brands.html')  
	
def therapies(request):
	return render(request,'therapies.html')

def client(request):
	return render(request,'client.html')

def api(request):
	return render(request,'api.html')

# def contact_us(request):
# 	return render(request,'contact-us.html')

def fd(request):
	return render (request,'r&d.html')

def reg_form(request):
	return render (request,'reg_form.html')

def management(request):
	return render (request,'management.html')

def core_value(request):
	return render (request,'core_value.html')

def facilities(request):
	return render (request,'facilities.html')

def global_presence(request):
	return render (request,'global_presence.html')
	
@csrf_exempt
def contact_us(request):
	if request.method=="POST":
		Contact_us.objects.create(
			name=request.POST['name'],
			company=request.POST['company'],
			country=request.POST['country'],
			city=request.POST['city'],
			email=request.POST['email'],
			mobile=request.POST['mobile'],
			Desc=request.POST['desc']
    	)
		msg = "Thank you for registration"
		return render(request, 'contact-us.html', {'msg': msg})
	else:
		msg = ""
		return render(request, 'contact-us.html', {'msg': msg})


	
@csrf_exempt
def employee_reg(request):
	if request.method=="POST":
		Employee_reg.objects.create(
			name=request.POST['name'],
			cp=request.POST['cp'],
			ce=request.POST['ce'],
			dp=request.POST['dp'],
			email=request.POST['email'],
			mobile=request.POST['mobile'],
			resume=request.POST['resume']
    	)
		msg = "Thank you for registration"
		return render(request, 'reg_form.html', {'msg': msg})
	else:
		msg = ""
		return render(request, 'reg_form.html', {'msg': msg})

