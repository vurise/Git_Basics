from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

# Create your views here.
#def register(request):
    #form = UserCreationForm
    #return render(request = request,
                  #template_name = "accounts/register.html",
                  #context={"form":form})




def register(request):
  	if request.method =="POST":
  		form= UserCreationForm(request.POST)
  		if form.is_valid():
  			user=form.save()
  			username=form.cleaned_data.get('username')
  			messages.success(request, f"New Account Created: {username}")
  			username=form.cleaned_data.get('username')
  			login(request,user)
  			return redirect('accounts/home.html')
  		else:
  			for msg in form.error_messages:
  				messages.error(request,f"{msg}:{form.error_messages[msg]}")
  				print(form.error_messages[msg])
  	form=UserCreationForm
  	return render(request=request, template_name='accounts/register.html', context={"form": form})





def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("accounts/home.html")


def login_request(request):
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "accounts/login.html",
                  context={"form":form})

 

    






