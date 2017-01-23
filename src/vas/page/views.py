from django.shortcuts import render
from django.template import RequestContext
from .models import Apartment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def home_page(request):

    context = Apartment.objects.all()
    """
    paginator = Paginator(context,25)
    page = request.GET.get('context')
    try:
        apartment = paginator.page(page)
    except PageNotAnInteger:
        apartment = paginator.page(1)
    except EmptyPage:
        apartment = paginator.page(paginator.num_pages)
    """
    return render(request,'page.html',{'context':context})