from django.db import models
import datetime as dt


# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=30, unique=True)
    
    
    def __str__(self):
            return self.location_name


    def save_location(self):
        self.save()

            
class Category(models.Model):
    cat_name = models.CharField(max_length=40, unique=True)
    
    
    def __str__(self):
        return self.cat_name


    def save_category(self):
        self.save()

class Uploader(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	email = models.EmailField()
	# blank =True allows null values into db
	phone_number = models.CharField(max_length = 10,blank = True)


	def __str__(self):
		return self.first_name

	def save_uploader(self):
		self.save()


    

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Images(models.Model):
	uploader = models.ForeignKey(Uploader)
	name = models.CharField(max_length = 60)
	description = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)
	location = models.ForeignKey(Location)
	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(tags)
	images_image = models.ImageField(upload_to = 'images/')

	@classmethod
	def days_photos(cls,date):
            photos = cls.objects.filter(pub_date__date = date)
            return photos

	@classmethod
	def todays_photos(cls):
            today = dt.date.today()
            photos = cls.objects.filter(pub_date__date = today)
            return photos

	@classmethod
	def search_by_title(cls,search_term):
		#__icontains searches for matches of search term(s)
		images = cls.objects.filter(title__icontains=search_term)
		return images


