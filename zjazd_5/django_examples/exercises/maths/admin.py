from django.contrib import admin
from maths.models import Math

# Register your models here.

class MathAdmin (admin.ModelAdmin):
    list_display=["oper", "l1", "l2"]
    #list_filter =

admin.site.register(Math, MathAdmin)