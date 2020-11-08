from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Employee(models.Model):
    WORK_CHOICES=[
    ('F','Full Time'),
    ('P','Part time'),
    ]
    SHIFT_CHOICES=[
    ('M','Morning'),
    ('E','Evening'),
    ]
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=100,default='')
    employee = models.BooleanField(default=True)
    phone_no = models.IntegerField(default=0)
    education = models.CharField(max_length=100,default='')
    adhaar_number = models.IntegerField(default=0,unique=True)
    salary_expected = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    previous_job = models.CharField(max_length=100,default='')
    skills = models.CharField(max_length=100,default='')
    languages_known = models.CharField(max_length=100,default='')
    living_location = models.CharField(max_length=100,default='')
    working_hours = models.CharField(max_length=100, choices=WORK_CHOICES,default='')
    shift = models.CharField(max_length=100, choices=SHIFT_CHOICES,default='')
    referer_username = models.CharField(max_length=100,default='')
    points = models.IntegerField(default=0)
    recommended_user = models.BooleanField(default=False)
    def __str__(self):
            return self.user.username
    
    # def create_employee(sender, **kwargs):
    #     if kwargs['created']:
    #         employee = Employee.objects.create(user=kwargs['instance'])

    # post_save.connect(create_employee, sender= User)

class Company(models.Model):
    WORK_CHOICES=[
    ('F','Full Time'),
    ('P','Part time'),
    ]
    SHIFT_CHOICES=[
    ('M','Morning'),
    ('E','Evening'),
    ]
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    company_name = models.CharField(max_length=100,default='')
    company = models.BooleanField(default=True)
    job_type = models.CharField(max_length=100,default='')
    jobs_number = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    minimum_qualification = models.CharField(max_length=100,default='')
    minimum_experience = models.IntegerField(default=0)
    languages_required = models.CharField(max_length=100,default='')
    job_location = models.CharField(max_length=100,default='')
    job_hours = models.CharField(max_length=100, choices=WORK_CHOICES,default='')
    job_shift = models.CharField(max_length=100, choices=SHIFT_CHOICES,default='')

    def __str__(self):
            return self.user.username


    # def create_company(sender, **kwargs):
    #     if kwargs['created']:
    #         company = Company.objects.create(user=kwargs['instance'])

    # post_save.connect(create_company, sender= User)

