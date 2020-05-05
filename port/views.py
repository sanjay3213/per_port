from django.shortcuts import render
from .models import project
# Create your views here.

def home(request):
	projects=project.objects.all()
	return render(request,'port/home.html', {'projects':projects})

def autocad(request):
	return render(request, 'port/autocad.html')

def about(request):
	return render(request, 'port/about.html')

    