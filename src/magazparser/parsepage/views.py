from django.shortcuts import render
from .models import Apartment
# Create your views here.
def home_page(request):
    Apartment.objects.all()
    return render(request,'page.html',{'home_page':home_page })