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
    category = models.CharField(max_length=40)
    
    
    def __str__(self):
        return self.category


    def save_category(self):
        self.save()

    @classmethod
    delete_category(cls, category):
    	cls.objects.filter(category=category).delete()
    		    

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Images(models.Model):
	name = models.CharField(max_length = 60)
	description = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	category = models.ManyToManyField(Category)
	tags = models.ManyToManyField(tags)
	images = models.ImageField(upload_to = 'images/')

	def __str__(self):
		return self.title

	def save_images(self):
		self.save

	@classmethod
	def all_photos(cls):
            photos = cls.objects.all()
            return photos

	@classmethod
	def todays_photos(cls):
            today = dt.date.today()
            photos = cls.objects.filter(pub_date__date = today)
            return photos

	@classmethod
	def search_by_category(cls,search_term):
		#__icontains searches for matches of search term(s)
		images = cls.objects.filter(Q(category__category=search_term) | Q(title__icontains = search_term) | Q(location__location= search_term))

		return photos


