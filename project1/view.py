from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth
from rest_framework import status
from django.shortcuts import render, redirect
from webpage.models import employees,package,holidayspackage,hotel,popular
from django.contrib import messages
from project1.settings import *
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from webpage.token import account_activation_token
from django.views.generic.base import View
from rest_framework.response import Response
from rest_framework.views import APIView
from webpage.serializers import employeesSerializers
def show(request):
    return HttpResponse("hello world")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("dashboard")
        else:
            messages.info(request,'invalid credantials !')
            return redirect('login')
    else:
        return render(request,"login.html")
def registration(request):
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        un = request.POST['username']
        em = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1==pass2:
            if User.objects.filter(username=un).exists():
                messages.info(request,'Username exists !!')
            elif User.objects.filter(email=em).exists():
                messages.info(request,'email exists !!')
            else:
                user = User.objects.create_user(username=un, email=em, password=pass1, first_name=fn, last_name=ln)
                user.is_active = False
                user.save()

                current_site = get_current_site(request)

                subject = 'Activate Your Account'

                message = render_to_string('activate_account.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })

                send_mail(
                    subject,
                    message,
                    EMAIL_HOST_USER,
                    [em],
                    fail_silently=False,
                )

                return redirect('login')
        else:
            messages.info(request,'Password not matched !')
    else :
        return render(request,'registration.html')
def dashboard(request):
    pops = popular.objects.all()
    return render(request,"dashboard.html",{'pops':pops})
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def conbooking(request):
    return render(request,"conbooking.html")
def holidaypackage(request):
    holidayspackages = holidayspackage.objects.all()
    return render(request,"holidaypack.html",{'holidayspackages':holidayspackages})
def honeymoonpackage(request):
    packages=package.objects.all()
    return render(request,"familypack.html",{'packages':packages})

def logout(request):
    auth.logout(request)
    return redirect("dashboard")
class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            #uid = force_text(urlsafe_base64_decode(uidb64))
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request)
            messages.success(request, ('Your account have been confirmed.'))
            return render(request,'home.html')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('/Thanks')

#def pack(request):
 #   packages=package.objects.all()
  #  holidayspackages = holidayspackage.objects.all()
   # return render(request,"pack.html",{'packages':packages,'holidayspackages':holidayspackages})


def hotel1(request):
    hotels=hotel.objects.all()
    return render(request,"hotel.html",{'hotels':hotels})



# def myaccount(request, pk=None):
#     v=User.objects.get(pk=pk)
#     return render(request,"account.html",{'v':v})




def myaccount(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'account.html', args)

class employeesList(APIView):
    def get(self,request):
        employee1=employees.objects.all()
        serializer=employeesSerializers(employee1,many=True)
        return Response(serializer.data)
    def POST(self):
        pass
class employeeListPost(APIView):
    def Post(self,request):
        serializer = employeesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
