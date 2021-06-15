"""todo URL Configuration

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
from django.contrib import admin
from django.urls import path
from .views import create_view,list_view,delete_view,update_view,registration_view,Login_Page,Home_Page,Logout_page

urlpatterns = [
    path("create",create_view,name="create"),
    path("list",list_view,name="list"),
    path("delete/<int:id>",delete_view,name="remove"),
    path("update/<int:id>",update_view,name="update"),
    path("regis",registration_view,name="regis"),
    path("login",Login_Page,name="log"),
    path("home",Home_Page,name="home"),
    path("logout",Logout_page,name="logout")
]
