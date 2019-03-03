from django.contrib import admin
from .models import Uploader,Images,tags

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('categories',)

admin.site.register(Location)
admin.site.register(Images,ImageAdmin)
admin.site.register(categories)