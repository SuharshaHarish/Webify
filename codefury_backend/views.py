from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import RegistrationForm,EmployeeForm,CompanyForm
from django.forms.models import inlineformset_factory
from .models import Employee,Company
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash

def home(request): 
    print(request.user)
    if request.user.is_authenticated:
        if Employee.objects.filter(user = request.user).exists():
            user = Employee.objects.get(user = request.user)
            args={'user':user,'nuser':request.user }
            print(user.points)
        else:
            args={'user':None,'nuser':request.user }
    else:
        args={'user':None ,'nuser':request.user}
    return render(request,'codefury_backend/home.html',args)

def login_redirect(request):
    if request.user:
        if Company.objects.filter(user = request.user).exists():
            return redirect(reverse('codefury_backend:candidate_search'))
        if Employee.objects.filter(user = request.user).exists():
            return redirect(reverse('codefury_backend:job_search'))

def employee_register(request):
    
    if request.method == 'POST':
        userform = RegistrationForm(request.POST)
        employeeform = EmployeeForm(request.POST)
        # reg_form = RegistrationForm(request.POST)
        if userform.is_valid() and employeeform.is_valid() :
            form1 = userform.save()
            form2 = employeeform.save()
            # if registerFormset.is_valid():
            #     registerFormset.save()
            return redirect(reverse('codefury_backend:login'))
    else:
        userform = RegistrationForm()
        employeeform = EmployeeForm()
    args = {'form1':userform, 'form2':employeeform}

    return render(request,'codefury_backend/reg_form.html',args)

def company_register(request):
    
    if request.method == 'POST':
        userform = RegistrationForm(request.POST)
        companyform = CompanyForm(request.POST)
        # reg_form = RegistrationForm(request.POST)
        if userform.is_valid() and companyform.is_valid() :
            form1 = userform.save()
            form2 = companyform.save()
            # if registerFormset.is_valid():
            #     registerFormset.save()
            return redirect(reverse('codefury_backend:login'))
    else:
        userform = RegistrationForm()
        companyform = CompanyForm()
    args = {'form1':userform, 'form2':companyform}

    return render(request,'codefury_backend/reg_form.html',args)

def job_search(request):

    # if request.method == 'GET':
    # args = {'form':JobSearchForm}
    if request.method == 'POST':
       form = request.POST
       if form:         
        
        request.session['job_type'] = form["job_type"]
        request.session['job_location'] = form["job_location"]
        return redirect(reverse('codefury_backend:jobs_list'))
    
    return render(request,'codefury_backend/job_search.html')
    
def jobs_list(request):

    
    if request.session.has_key('job_location') and  request.session.has_key('job_type'):
        job_type = request.session['job_type']
        location = request.session['job_location']
        jobs = Company.objects.filter(job_type=job_type,job_location=location)
    print(jobs)
    args={'jobs':jobs}
    return render(request,'codefury_backend/jobs_list.html',args)

def candidate_search(request):

    # if request.method == 'GET':
    # args = {'form':JobSearchForm}
    if request.method == 'POST':
       form = request.POST
       if form:         
        
        request.session['working_hours'] = form["working_hours"]
        request.session['job_location'] = form["job_location"]
        return redirect(reverse('codefury_backend:candidates_list'))
    
    return render(request,'codefury_backend/candidate_search.html')
    
def candidates_list(request):

    
    if request.session.has_key('job_location') and  request.session.has_key('working_hours'):
        
        if request.session['working_hours'] == 'Full Time':
            working_hours = 'F'
        else:
            working_hours = 'P'
        location = request.session['job_location']
        candidates = Employee.objects.filter(working_hours=working_hours,living_location=location).order_by('-points')
    args={'candidates':candidates}
    return render(request,'codefury_backend/candidates_list.html',args)