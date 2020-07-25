"""meetups URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from intro import urls
from django.conf.urls import include
from intro import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home_view, name='home'),
    path('home', views.home_view,name='home'),
    path('hackathons', views.hackathons, name='hackathons'),
    path('codingcompetitions', views.codingcompetitions, name='codingcompetitions'),
    path('meetups', views.meetups, name='meetups'),
    path('muns', views.muns, name='muns'),
    path('profile', views.profile, name='profile'),
    path('about', views.about, name='about'),
    path('register',include('accounts.urls')),
]
