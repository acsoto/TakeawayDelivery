"""back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', myapp.views.login),
    path('api/register/', myapp.views.register),
    path('api/getInformation/', myapp.views.getInformation),
    path('api/changeInformation/', myapp.views.changeInformation),
    path('api/changePassword/', myapp.views.changePassword),
    path('api/getStores/', myapp.views.getStores),
    path('api/getStoreInformation/', myapp.views.getStoreInformation),
    path('api/deleteUser/', myapp.views.deleteUser),
    path('api/getEvaluateFood/', myapp.views.getEvaluateFood),
    path('api/getEvaluateUser/', myapp.views.getEvaluateUser),
    path('api/setOrders/', myapp.views.setOrders),
    path('api/unstar/', myapp.views.unstar),
    path('api/finishOrder/', myapp.views.finishOrder),
    path('api/takeOrder/', myapp.views.takeOrder),
    path('api/getAllOrders/', myapp.views.getAllOrders),
    url(r'^', TemplateView.as_view(template_name="index.html")),
]
