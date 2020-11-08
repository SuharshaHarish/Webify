from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Employee,Company

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'email',
        )

        # help_texts = {
        #     'username': None,
        #     'password': None,
        # }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def save(self,commit=True):
        user = super(RegistrationForm,self).save(commit=False)
        user.email = self.cleaned_data['email']


        if commit:
            user.save()

            return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget= forms.TextInput(attrs={'class':'my_username'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'class':'my_password'}))

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = (
            'phone_no',
            'referer_username',
            'education',
            'adhaar_number',
            'salary_expected',
            'experience',
            'living_location',
            'previous_job',
            'skills',
            'languages_known',
            'working_hours',
            'shift',         
        )

    def save(self,commit=True):
        profile = super(EmployeeForm,self).save(commit=False)
        profile.phone_no = self.cleaned_data['phone_no']
        profile.education = self.cleaned_data['education']
        profile.adhaar_number = self.cleaned_data['adhaar_number']
        profile.salary_expected = self.cleaned_data['salary_expected']
        profile.experience = self.cleaned_data['experience']
        profile.living_location = self.cleaned_data['living_location']
        profile.previous_job = self.cleaned_data['previous_job']
        profile.skills = self.cleaned_data['skills']
        profile.languages_known = self.cleaned_data['languages_known']
        profile.working_hours = self.cleaned_data['working_hours']        
        profile.shift = self.cleaned_data['shift']
        profile.referer_username = self.cleaned_data['referer_username']
        if profile.referer_username != "''":
            if Employee.objects.get(user=User.objects.get(username=profile.referer_username))!= None:     
                ref_profile = Employee.objects.get(user=User.objects.get(username=profile.referer_username))
                ref_profile.points = ref_profile.points + 10 
                ref_profile.save()
                if ref_profile.points >= 50:
                    ref_profile.recommended_user = True
                    ref_profile.save()
        id = User.objects.latest('date_joined')
        profile.user = id


        if commit:
            profile.save()


            return profile

class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = (
            'company_name',
            'job_type',
            'jobs_number',
            'salary',
            'minimum_qualification',
            'minimum_experience',
            'languages_required',
            'job_location',
            'job_hours',
            'job_shift'         
        )

    def save(self,commit=True):
        profile = super(CompanyForm,self).save(commit=False)
        profile.job_type = self.cleaned_data['job_type']
        profile.jobs_number = self.cleaned_data['jobs_number']
        profile.salary = self.cleaned_data['salary']
        profile.minimum_qualification = self.cleaned_data['minimum_qualification']
        profile.minimum_experience = self.cleaned_data['minimum_experience']
        profile.languages_required = self.cleaned_data['languages_required']
        profile.job_location = self.cleaned_data['job_location']      
        profile.job_hours = self.cleaned_data['job_hours']        
        profile.job_shift = self.cleaned_data['job_shift']
        profile.company_name = self.cleaned_data['comapnay_name']
        
        id = User.objects.latest('date_joined')
        profile.user = id


        if commit:
            profile.save()


            return profile