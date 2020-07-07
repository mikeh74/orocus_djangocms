from django.db import models
from django.conf import settings
from filer.fields.image import FilerImageField
from filer.fields.folder import FilerFolderField
# from filer.models import Folder

from cms.models.pluginmodel import CMSPlugin
# from djangocms_text_ckeditor import HTMLField

from django.utils.translation import ugettext as _, ungettext


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
    youtube = models.CharField(_("Youtube Id"),
                               max_length=20,
                               null=True,
                               blank=True)
    gallery = models.ForeignKey(Gallery,
                                verbose_name=_("Gallery"),
                                on_delete=models.CASCADE)

    def __str__(self):
        return "%s (%s)" % (self.image, self.gallery)

class GalleryPluginModel(CMSPlugin):
    folder = FilerFolderField(on_delete=models.PROTECT)

    def __str__(self):
        return "%s" % (self.folder)
