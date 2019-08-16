"""my_first_website URL Configuration

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
from django.contrib import admin
from django.urls import path
from ram import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Tatti,name= 'Tatti'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('pokipost', views.poki,name='poki'),
    path('show/',views.shows,name='show'),
    path('edit/<int:id>/',views.sudhaar,name='edit'),
    path('update/<int:id>/', views.update),
    path('delete/<int:id>', views.destroy),
    path('registration/',views.register,name='register'),
    path('login/',views.user_login,name='login')



]
