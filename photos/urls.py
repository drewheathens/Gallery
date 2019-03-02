from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    # convert date to day
    url(r'^$',views.photos_today,name='photosToday'),
    #  return news from those dates
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_photos,name = 'pastPhotos'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^images/(\d+)',views.images,name ='images')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)