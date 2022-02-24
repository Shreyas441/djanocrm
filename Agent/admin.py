from django.contrib import admin

# Register your models here.
from .models import Customer,Services_taken,Services_taken_request

admin.site.register(Customer)
admin.site.register(Services_taken)
admin.site.register(Services_taken_request)