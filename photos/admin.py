from django.contrib import admin
from .models import Location,Images,Category

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    # filter_horizontal =('Images',)
    admin.site.register(Location)
    admin.site.register(Images)
    admin.site.register(Category)