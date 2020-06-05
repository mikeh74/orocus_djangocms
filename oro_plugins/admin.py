from django.contrib import admin
from filer.admin.imageadmin import ImageAdmin
from filer import settings as filer_settings
from .models import OrocusCustomImage

from django.apps import apps

# x = filer_settings.FILER_IMAGE_MODEL

# name = x.split('.')[1]

# #  Image = apps.get_model('filer', name)

Image = OrocusCustomImage

admin.site.register(Image)

# class CustomImageAdmin(ImageAdmin):
#     # your custom code
#     pass

#     # Using build_fieldsets allows to easily integrate common field in the admin
#     # Don't define fieldsets in the ModelAdmin above and add the custom fields
#     # to the ``extra_main_fields`` or ``extra_fieldsets`` as shown below
#     CustomImageAdmin.fieldsets = CustomImageAdmin.build_fieldsets(
#         extra_main_fields=('default_alt_text',
#                            'default_caption', 'youtube_id'),
#         extra_fieldsets=(
#             ('Subject Location', {
#                 'fields': ('subject_location',),
#                 'classes': ('collapse',),
#             }),
#         )
#     )


# # Unregister the default admin
# admin.site.unregister(Image)
# # Register your own
# admin.site.register(Image, CustomImageAdmin)
