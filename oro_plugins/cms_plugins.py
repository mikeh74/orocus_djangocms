from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext as _

from .models import GalleryPluginModel

@plugin_pool.register_plugin
class GalleryPlugin(CMSPluginBase):
    model = GalleryPluginModel
    render_template = "oro_plugins/gallery/default.html"
    cache = False

    module = _("Oro")
    name = _("Gallery")  # name of the plugin in the interface

    def render(self, context, instance, placeholder):
        # model = self.model

        # image_list = News.objects.filter(category=instance.category.id).order_by('-pub_date')[:instance.items_to_show]

        context.update({'instance': instance})
        return context