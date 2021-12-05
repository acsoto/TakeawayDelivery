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
from django.urls import path
from django.views.generic import TemplateView
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', myapp.views.login),
    path('api/register/', myapp.views.register),
    path('api/getInformation/', myapp.views.get_information),
    path('api/changeInformation/', myapp.views.change_information),
    path('api/changePassword/', myapp.views.change_password),
    path('api/getStores/', myapp.views.get_stores),
    path('api/getStoreInformation/', myapp.views.get_store_information),
    path('api/deleteUser/', myapp.views.delete_user),
    path('api/getEvaluateFood/', myapp.views.get_evaluate_food),
    path('api/evaluateFood/', myapp.views.evaluate_food),
    path('api/deleteEvaluateFood/', myapp.views.delete_evaluate_food),
    path('api/getEvaluateUser/', myapp.views.get_evaluate_user),
    path('api/setOrders/', myapp.views.set_orders),
    path('api/unStar/', myapp.views.un_star),
    path('api/setStar/', myapp.views.set_star),
    path('api/finishOrder/', myapp.views.finish_order),
    path('api/takeOrder/', myapp.views.take_order),
    path('api/getAllOrders/', myapp.views.get_all_orders),
    url(r'^', TemplateView.as_view(template_name="index.html")),
]
