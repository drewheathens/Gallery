from django.http import HttpResponse
import datetime as dt
from django.shortcuts import render, redirect
from .models import Images

# Create your views here.
def welcome(request):
	return render(request,'welcome.html')

def photos_today(request):
    date = dt.date.today()
    photos = Images.todays_photos()
    return render(request, 'all-photos/images.html', {"date": date,"images":images})


def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

# View Function to present photos from past days
def past_days_photos(request, past_date):


    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_today)

    photos = Images.days_photos(date)
    return render(request, 'all-photos/past-photos.html',{"date": date,"photos":photos})    	

def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Images.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})

def images(request,images_id):
    try:
        images = Images.objects.get(id = images_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/images.html", {"images":images})