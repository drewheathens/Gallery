from django import url
from . import views
 
 urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    # convert date to day
    url(r'^$',views.photoss_today,name='photosToday'),
    #  return news from those dates
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^images/(\d+)',views.images,name ='images')
]