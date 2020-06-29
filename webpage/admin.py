from django.contrib import admin
from .models import employees, videos, package , holidayspackage,hotel ,popular,test

# Register your models here.
admin.site.register(employees)
admin.site.register(videos)
admin.site.register(package)
admin.site.register(holidayspackage)
admin.site.register(hotel)
admin.site.register(popular)

admin.site.register(test)