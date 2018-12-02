from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.


def main_page(request):
    return HttpResponse(content="Main page")


def hello_world(request):
    return HttpResponse(content="Hello World!")


def hello_personalized(request, name):
    return HttpResponse(content=f"Hello {name}!")


"""def Madd(request, l1, l2):
    return HttpResponse(content=int(l1) + int(l2))


def Msub(request, l1, l2):
    return HttpResponse(content=int(l1) - int(l2))


def Mmul(request, l1, l2):
    return HttpResponse(content=int(l1) * int(l2))


def Mdiv(request, l1, l2):
    return HttpResponse(content=int(l1) / int(l2))

def math(request,oper, l1, l2):
    if oper == "+":
        return HttpResponse(content=int(l1) + int(l2))
    elif oper == "-":
        return HttpResponse(content=int(l1) - int(l2))
    if oper == "*":
        return HttpResponse(content=int(l1) * int(l2))
    elif oper == ":":
        return HttpResponse(content=int(l1) / int(l2))
"""