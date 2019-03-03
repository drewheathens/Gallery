from django.http import HttpResponse
import datetime as dt
from django.shortcuts import render, redirect
from .models import Images

# Create your views here.
def images(request,images_id):
    images = images.objects.all()

   
    return render(request,"images.html", {"images":images, "ALLOWED_HOSTS":ALLOWED_HOSTS})

def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Images.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})

