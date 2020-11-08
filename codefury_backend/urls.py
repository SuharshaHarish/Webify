from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
app_name = "codefury_backend"

urlpatterns = [
    path('employee_register/',views.employee_register, name="employee_register"),
    path('company_register/',views.company_register, name="company_register"),
    path('job_search/',views.job_search, name="job_search"),
    path('jobs_list/',views.jobs_list, name="jobs_list"),
    path('candidate_search/',views.candidate_search, name="candidate_search"),
    path('candidates_list/',views.candidates_list, name="candidates_list"),
    path('login_redirect/',views.login_redirect, name="login_redirect"),
    path('home/',views.home, name="home"),
    path('login/',LoginView.as_view(template_name='codefury_backend/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='codefury_backend/logout.html'),name='logout')
]