from django.contrib import admin
from owner.models import *

# Register your models here
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Review)

