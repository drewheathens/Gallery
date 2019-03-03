from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    # convert date to day
    url(r'^$',views.images,name='images'),
    #  return news from those dates
    url(r'^search/', views.search_results, name='search_results'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)