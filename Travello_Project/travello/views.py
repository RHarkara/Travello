from django.shortcuts import render

from . models import Destination, WarangalDetails

# Create your views here.

def index(request):
    

    destinations = Destination.objects.all()
   
    
    return render(request, 'index.html',{'destinations' : destinations})

def warangal(request):

    warangalDetails = WarangalDetails.objects.all()


    return render(request,'warangal.html',{'warangalDetails' : warangalDetails})
