from django.conf.urls import url
from. import views
from django.conf.urls import include

urlpatterns=[
 url(r'' , views.home_view , name='home'),
 url(r'hackathons', views.hackathons, name='hackathons'),
 url(r'codingcompetitions', views.codingcompetitions, name='codingcompetitions'),
 url(r'meetups', views.meetups, name='meetups'),
 url(r'muns', views.muns, name='muns'),
 url(r'accounts', include('accounts.urls')),
 
]
#path('accounts/', include('accounts.urls')), # new
    #path('accounts/', include('django.contrib.auth.urls')),
