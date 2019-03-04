from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image
from decouple import config,Csv

# Create your views here.
def images(request):
    images = Image.objects.all()
       
    return render(request,"images.html", {"images":images})

def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "Doesn't match any image"
        return render(request, 'search.html',{"message":message})

