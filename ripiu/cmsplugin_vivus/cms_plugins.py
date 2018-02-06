from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import __version__
from .models import VivusPlugin


@plugin_pool.register_plugin
class VivusPluginPublisher(CMSPluginBase):
    model = VivusPlugin
    name = _('Vivus animation')
    module = 'Ri+'
    render_template = 'ripiu/cmsplugin_vivus/vivus.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        import json
        context = super(VivusPluginPublisher, self).render(
            context, instance, placeholder
        )
        vivus_conf = {
            'animation_type': instance.animation_type,
            'start': instance.start,
            'duration': instance.duration,
            'delay': instance.delay,
            # 'onReady':
            # 'pathTimingFunction':
            # 'animTimingFunction':
            'dash_gap': instance.dash_gap,
            'reverse_stack': json.dumps(instance.reverse_stack),
            'self_destroy': json.dumps(instance.self_destroy),
        }
        if instance.force_render is not None:
            vivus_conf['force_render'] = json.dumps(instance.force_render)
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'version': __version__,
            'conf': vivus_conf,
        })
        return context
