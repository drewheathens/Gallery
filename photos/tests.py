from django.test import TestCase
from .models import Location, Category, Images
import datetime as dt

# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.Moringa = Location(location='Moringa')

    def test_instance(self):
        self.assertTrue(isinstance(self.Moringa,Location))

    def tearDown(self):
        Location.objects.all().delete()

    def test_save_method(self):
        self.Moringa.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_method(self):
        self.Moringa.delete_location('Moringa')
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)

class categoryTestClass(TestCase):
    def setUp(self):
        self.Nature = Category(category='Nature')

    def test_instance(self):
        self.assertTrue(isinstance(self.Nature,Category))

    def tearDown(self):
        Category.objects.all().delete()

    def test_save_method(self):
        self.Nature.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category)>0)

    def test_delete_method(self):
        self.Nature.delete_category('Nature')
        categories = category.objects.all()
        self.assertTrue(len(category)==0)

class ImagesTestClass(TestCase):
    def setUp(self):
        self.test_category = category(category=list('Travel'))
        self.test_category.save_category()

        self.location = Location(location="Town")
        self.location.save_location()

        self.images = Images(id=1,title="Slide Away",categories=self.test_category,location=self.location,)
        self.images.save_images()

    def tearDown(self):
        category.objects.all().delete()
        Location.objects.all().delete()
        Images.objects.all().delete()