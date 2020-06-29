"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from paygate.models import airbook
from . import view
from.settings import *
from django.conf.urls.static import static
from project1.view import ActivateAccount
from paygate.views import  *
from django.contrib.auth import  views as auth_views

urlpatterns = [
    path('',view.show,name="show"),
    path('admin/', admin.site.urls),
    path('login',view.login,name="login"),
    path('registration',view.registration,name="registration"),
    path('dashboard',view.dashboard,name="dashboard"),
    path('about',view.about,name="about"),
    path('logout',view.logout,name="logout"),
    path('conbooking',view.conbooking,name="conbooking"),
    path('contact',view.contact,name="contact"),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('paymentMode/<int:pk>/', paymentMode,name="paymentMode"),
    path('paymentMode1/<int:pk>/', paymentMode1,name="paymentMode1"),
    path('paymentMode3/<int:pk>/', paymentMode3,name="paymentMode3"),
    #path('pack',view.pack,name="pack"),
    path('hotel1',view.hotel1,name="hotel1"),
    path('holidaypackage',view.holidaypackage,name="holidaypackage"),
    path('honeymoonpackage',view.honeymoonpackage,name="honeymoonpackage"),
    path('myaccount',view.myaccount,name="myaccount"),
    path('employees/',view.employeesList.as_view()),
    path('employeespost/',view.employeeListPost.as_view()),
    path('user_registration/', view.registration, name ='user_registration'),
    path('booking/<int:pk>',booking,name="booking"),
    path('hotelbooking/<int:pk>',hotelbooking,name="hotelbooking"),
    path('holibooking/<int:pk>',holibooking,name="holibooking"),
    path('familybooking/<int:pk>',familybooking,name="familybooking"),
    path('abooking',abooking,name="abooking"),
   # path('add',add,name="add"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
        name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
        name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete')
]
urlpatterns=urlpatterns+static(MEDIA_URL,document_root=MEDIA_ROOT)