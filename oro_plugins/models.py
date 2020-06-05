from django.db import models
# from django.conf import settings
from filer.fields.image import FilerImageField

# from cms.models.pluginmodel import CMSPlugin
# from cms.models.fields import PageField

# from djangocms_text_ckeditor import HTMLField
# from djangocms_attributes_field.fields import AttributesField

from django.utils.translation import ugettext, ugettext_lazy as _, ungettext

# Create your models here.

from filer.models.abstract import BaseImage

class OrocusCustomImage(BaseImage):
    youtube_id = models.CharField(max_length=20,
      blank=True, null=True)

    class Meta(BaseImage.Meta):
        # You must define a meta with en explicit app_label
        app_label = 'oro_plugins'
        default_manager_name = 'objects'

# class GalleryField(FilerImageField):
#     youtube = models.CharField(_(""), max_length=20)
