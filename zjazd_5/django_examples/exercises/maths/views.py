from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from maths.models import Math

def calculate (oper, l1, l2):
    if oper == "+":
        return int(l1) + int(l2)
    elif oper == "-":
        return int(l1) - int(l2)
    if oper == "*":
        return int(l1) * int(l2)
    elif oper == ":":
        return int(l1) / int(l2)

# Create your views here.
@login_required()
def math(request, oper, l1, l2):
    if request.user:
        Math.objects.create(oper=oper, l1=l1, l2=l2, user=request.user)
    else:
        Math.objects.create(oper=oper, l1=l1, l2=l2)
    if oper == "+":
        return HttpResponse(content=int(l1) + int(l2))
    elif oper == "-":
        return HttpResponse(content=int(l1) - int(l2))
    if oper == "*":
        return HttpResponse(content=int(l1) * int(l2))
    elif oper == ":":
        return HttpResponse(content=int(l1) / int(l2))


def math_list(request):
    objects = Math.objects.all()

    out = ""
#    for o in objects:
#        out += f"{o.oper}: {o.l1} {o.l2} <br>"

    return render(
        request=request,
        template_name="math_list.html",
        context={"maths":objects}
    )


def math_details(request, id):
    m = Math.objects.get(pk=id)
    wynik = calculate(m.oper, m.l1, m.l2)
    out = f"""
Operacja: {m.oper}<br>
arg1: {m.l1}<br>
arg2: {m.l2}<br>
-----------------<br>
wynik: {wynik}<br>
user: {m.user}
"""

    return HttpResponse(out)