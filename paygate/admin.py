from django.contrib import admin
from.models import book,hotelbook,airbook,fbook



# Register your models here.
admin.site.register(book)
admin.site.register(fbook)
admin.site.register(hotelbook)
admin.site.register(airbook)