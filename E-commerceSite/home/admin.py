from django.contrib import admin
from .models import Order,Product,LineDetails,CartDetails

# Register your models here.
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(LineDetails)
admin.site.register(CartDetails)