from django.contrib import admin
from .models import Gallery, GalleryItem
from django.utils.html import format_html
from easy_thumbnails.files import get_thumbnailer
from filer.models import Folder
from django import forms

admin.site.register(Gallery)

@admin.register(GalleryItem) 
class GalleryItemAdmin(admin.ModelAdmin):

    def image_tag(self, obj):

        options = {'size': (100, 100), 'crop': True}
        thumb_url = get_thumbnailer(obj.image).get_thumbnail(options).url
        return format_html('<img src="{}" />'.format(thumb_url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag', 'image', 'gallery']

    list_filter = ('gallery',)
