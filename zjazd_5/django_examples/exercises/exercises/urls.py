"""exercises URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib import admin

from Products.views import fake_view
from mainpage.views import main_page, hello_world, hello_personalized
from maths.views import math, math_list,math_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", main_page),
    path("hello", hello_world),
    path("hello/<name>", hello_personalized),
    # path("add/<l1>/<l2>", Madd),
    # path("sub/<l1>/<l2>", Msub),
    # path("mul/<l1>/<l2>", Mmul),
    # path("div/<l1>/<l2>", Mdiv)
    path("maths",math_list),
    path("maths/<int:id>",math_details),
    path("math/<oper>/<l1>/<l2>", math),
    path("products",fake_view)
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls'))
]