from django.shortcuts import render

# Create your views here.

def Product(request, nazwa, opis, cena, status):
    if request.user:
        Product.objects.create(nazwa=nazwa, opis=opis, cena=cena,status=status, user=request.user)
    else:
        Product.objects.create(nazwa=nazwa, opis=opis, cena=cena, status=status)

def fake_view(request):
    return render(request=request, template_name="products_list.html", context={})