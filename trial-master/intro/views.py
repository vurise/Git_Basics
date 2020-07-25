from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home_view(request, *args , **kwargs):
	return render(request, 'intro/index.html', {})

def hackathons(request):
	return render(request,'intro/hackathons.html', {})

def codingcompetitions(request):
	return render(request,'intro/codingcompetitions.html', {})

def muns(request):
	return render(request, 'intro/muns.html', {})

def meetups(request):
	return render(request, 'intro/meetups.html', {})

def profile(request):
	return render(request,'intro/profile.html', {})

def about(request):
	return render(request,'intro/about.html', {})





