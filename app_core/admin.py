from django.contrib import admin

from app_core.models import Order, Dish, Compound, Check, Waiter, DishCompound, CheckOrder

# Register your models here.
admin.site.register(Order)
admin.site.register(Dish)
admin.site.register(Compound)
admin.site.register(Check)
admin.site.register(Waiter)
admin.site.register(DishCompound)
admin.site.register(CheckOrder)
