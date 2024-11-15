from django.contrib import admin
from .models import ImageData

@admin.register(ImageData)
class ImageDataAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'md5_hash', 'phash')
    search_fields = ('image_url',)  
    list_filter = ('md5_hash',)  
