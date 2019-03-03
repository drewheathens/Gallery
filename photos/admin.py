from django.contrib import admin
from .models import Uploader,Images,tags

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
admin.site.register(Uploader)
admin.site.register(Images)
admin.site.register(tags)