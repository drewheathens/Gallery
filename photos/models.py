from django.db import models
from django.db.models import Q

import datetime as dt


# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=100)
    
    
    def __str__(self):
    	return self.location


    def save_location(self):
        self.save()


    @classmethod
    def delete_location(cls,location):
        cls.objects.filter(location=location).delete()

            
class Category(models.Model):
    category = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.category


    def save_category(self):
        self.save()

  

class Image(models.Model):
	name = models.CharField(max_length = 60)
	description = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, blank=True, default='lol.jpg')
	image = models.ImageField(upload_to = 'images/')

	def __str__(self):
		return self.name

	def save_images(self):
		self.save

	@classmethod
	def all_photos(cls):
            photos = cls.objects.all()
            return photos

	
	@classmethod
	def search_by_category(cls,search_term):
		#__icontains searches for matches of search term(s)
		photos = cls.objects.filter(category__category__icontains=search_term)

		return photos


