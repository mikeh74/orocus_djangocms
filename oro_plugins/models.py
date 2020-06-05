from django.db import models
from django.conf import settings
from filer.fields.image import FilerImageField

from cms.models.pluginmodel import CMSPlugin
# from djangocms_text_ckeditor import HTMLField

from django.utils.translation import ugettext, ugettext_lazy as _, ungettext


class Gallery(models.Model):
    name = models.CharField(_("Gallery"),
                            max_length=80)

    def __str__(self):
        return self.name

class GalleryItem(models.Model):
    image = FilerImageField(
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    youtube = models.CharField(_("Gallery Item"),
                               max_length=20,
                               null=True,
                               blank=True)
    gallery = models.ForeignKey(Gallery,
                                verbose_name=_(""),
                                on_delete=models.CASCADE)
