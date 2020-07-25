from django.conf.urls import url
from. import views
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



app_name='accounts'

urlpatterns=[
url("register", views.register, name="register"),
url("logout", views.logout_request, name="logout"),
url("login", views.login_request, name="login"),
url(r'', TemplateView.as_view(template_name='accounts/home.html'), name='home'),
#url(r'signup', views.signup_view, name='signup_view'),

]

