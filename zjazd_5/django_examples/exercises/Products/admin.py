from django.contrib import admin

# Register your models here.
class ProdAdmin (admin.ModelAdmin):
    list_display=["nazwa", "opis", "cena","status"]

#admin.site.register(Math, MathAdmin)
