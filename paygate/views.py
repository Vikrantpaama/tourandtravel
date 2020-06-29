from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from requests import packages
from django.contrib.auth.models import User

from paygate.models import book, hotelbook, airbook ,fbook
from webpage.models import package, hotel,holidayspackage,test
from . import checksum



# Create your views here.
def booking(request,pk):
    honeymoonpackages = package.objects.get(pk=pk)
    holidayspackages = holidayspackage.objects.get(pk=pk)
    return render(request,'booking.html', {'honeymoonpackages':honeymoonpackages,'holidayspackages': holidayspackages})

MERCHANT_KEY = "pXeKCySiW_0GLuCo"



def paymentMode(request, pk):
        test1= holidayspackage.objects.get(pk=pk)
        #test2 = User.objects.get(pk=pk)
        user = User.objects.get(pk=pk)
        current_user = User.objects.last()
        print(current_user.username)
        m = book(booking_id=user.id,  Email=user.email, Name=user.username,

                  amount=test1.amount, packagename=test1.packagename,)
        m.save()
        param_dict = {
            "MID": "xcZrot84908297102253",
            "ORDER_ID": str(user.id),
            "CUST_ID": (user.email),
            "TXN_AMOUNT": str(test1.amount),
            "CHANNEL_ID": "WEB",
            "INDUSTRY_TYPE_ID": "Retail",
            "WEBSITE": "WEBSTAGING",
            # "CALLBACK_URL": "http/127.0.0.1:8000/handleRequest/",
            "CALLBACK_URL": "https://merchant.com/callback/"

        }
        param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict, MERCHANT_KEY)

        return render(request, 'paytm.html', {'params': param_dict})
        # return redirect('conbooking')









def paymentMode1(request,pk):
    test1 = hotel.objects.get(pk=pk)
    user1 = User.objects.get(pk=pk)
    current_user = User.objects.last()
    print(current_user.username)
    m = hotelbook(booking_id=user1.id, Email=user1.email, Name=user1.username,

             amount=test1.amount, hotelname=test1.hotelname,address=test1.address, )
    m.save()
    param_dict = {
        "MID": "xcZrot84908297102253",
        "ORDER_ID": str(user1.id),
        "CUST_ID": (user1.email),
        "TXN_AMOUNT": str(test1.amount),
        "CHANNEL_ID": "WEB",
        "INDUSTRY_TYPE_ID": "Retail",
        "WEBSITE": "WEBSTAGING",
        # "CALLBACK_URL": "http/127.0.0.1:8000/handleRequest/",
        "CALLBACK_URL": "https://merchant.com/callback/"

    }
    param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict, MERCHANT_KEY)

    return render(request, 'paytm.html', {'params': param_dict})


#def paymentMode(request):
#    if request.method == 'POST':
 #       Name = request.POST['name']
  #      Email = request.POST['email']
   #     Phone = request.POST['phone']
    #    Address = request.POST['address']
     #   Address2 = request.POST['address2']
  #      City = request.POST['city']
   #     State = request.POST['state']
 #       check_in_date = request.POST['r2']
  #      check_out_date = request.POST['r3']
   #     Adult = request.POST['n1']
   #     Children = request.POST['n2']
   #     ACRooms = request.POST['n3']
    #    NonACRooms = request.POST['n4']
  #      user = hotelbook(Name=Name, Email=Email,Phone=Phone ,Address=Address, Address2=Address2,City=City , State=State, check_in_date=check_in_date, check_out_date=check_out_date, Adult=Adult, Children=Children, ACRooms=ACRooms, NonACRooms=NonACRooms)
   #     user.save()
    #    param_dict = {
   #         "MID": "xcZrot84908297102253",
   #         "ORDER_ID": "booking.booking_id",
   #         "CUST_ID": "email",
    #        "TXN_AMOUNT": "amount",
    #        "CHANNEL_ID": "WEB",
     #       "INDUSTRY_TYPE_ID": "Retail",
   #         "WEBSITE": "WEBSTAGING",
    #        # "CALLBACK_URL": "http/127.0.0.1:8000/handleRequest/",
    #        "CALLBACK_URL": "https://merchant.com/callback/"

    #    }
  #      param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict, MERCHANT_KEY)

   #     return render(request, 'paytm.html', {'params': param_dict})
    #    return redirect('paymentMode/')



def abooking(request):
  return render(request,'booking2.html')



def holibooking(request,pk):
    user = User.objects.get(pk=pk)
    holidayspackages = holidayspackage.objects.filter(specialized=user.name)
    return render(request,'holibooking.html', {'holidayspackages': holidayspackages})
def hotelbooking(request,pk):
    user = User.objects.get(pk=pk)
    hotels = hotel.objects.filter(specialized=user.name)
    return render(request,'hotel.html', {'hotels': hotels})
def familybooking(request,pk):
    user = User.objects.get(pk=pk)
    familypackage = package.objects.filter(specialized=user.name)
    return render(request,' familypack.html', {'familypackage':familypackage})
def paymentMode3(request,pk):
    test1 = package.objects.get(pk=pk)
    # test2 = User.objects.get(pk=pk)
    user2 = User.objects.get(pk=pk)
    current_user = User.objects.last()
    print(current_user.username)
    m = fbook(booking_id=user2.id, Email=user2.email, Name=user2.username,

             amount=test1.amount, packagename=test1.packagename, )
    m.save()
    param_dict = {
        "MID": "xcZrot84908297102253",
        "ORDER_ID": str(user2.id),
        "CUST_ID": (user2.email),
        "TXN_AMOUNT": str(test1.amount),
        "CHANNEL_ID": "WEB",
        "INDUSTRY_TYPE_ID": "Retail",
        "WEBSITE": "WEBSTAGING",
        # "CALLBACK_URL": "http/127.0.0.1:8000/handleRequest/",
        "CALLBACK_URL": "https://merchant.com/callback/"

    }
    param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict, MERCHANT_KEY)

    return render(request, 'paytm.html', {'params': param_dict})


@csrf_exempt
def handlerequest(request):
    #paytm will send you post request here
    return redirect('/Thanks')




#def add(request):
 #   if request.method == 'GET':
  #      return render(request,'booking.html')
   # else:
   #     a=int(request.POST['a1'])
   #     b=int(request.POST['a2'])
     #   c=a+b
    #    return render(request,'conbooking.html',{"sum":c})


#def amount(request, pk=None):
 #   if pk:
  #      user = amount.objects.get(pk=pk)
   # else:
    #    user = request.user
   # args = {'user': user}
    #return render(request, 'booking.html', args)



