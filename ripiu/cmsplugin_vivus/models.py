from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from filer.fields.file import FilerFileField


class VivusPlugin(CMSPlugin):
    '''Drawing animation on SVG'''

    TYPE_DELAYED = 'delayed'
    TYPE_SYNC = 'sync'
    TYPE_ONE_BY_ONE = 'oneByOne'
    TYPE_SCRIPT = 'script'
    TYPE_SCENARIO = 'scenario'
    TYPE_SCENARIO_SYNC = 'scenario-sync'
    TYPE_CHOICES = (
        (TYPE_DELAYED, _('Delayed start')),
        (TYPE_SYNC, _('Synchronous')),
        (TYPE_ONE_BY_ONE, _('One by one')),
        # (TYPE_SCRIPT, TYPE_SCRIPT),
        # (TYPE_SCENARIO, TYPE_SCENARIO),
        # (TYPE_SCENARIO_SYNC, TYPE_SCENARIO_SYNC),
    )

    START_IN_VIEWPORT = 'inViewport'
    START_MANUAL = 'manual'
    START_AUTOSTART = 'autostart'
    START_CHOICES = (
        (START_IN_VIEWPORT, _('Start once the SVG is in the viewport')),
        (START_MANUAL, _('Start manually')),
        (START_AUTOSTART, _('Start right away')),
    )

    animation_type = models.CharField(
        _('animation type'), max_length=15, choices=TYPE_CHOICES,
        blank=False, default=TYPE_DELAYED,
        help_text=_('Defines what kind of animation will be used.')
    )

    svg_file = FilerFileField(
        blank=False, null=False, verbose_name=_('SVG file')
    )

    start = models.CharField(
        _('animation trigger'), max_length=15, choices=START_CHOICES,
        blank=False, default=START_IN_VIEWPORT,
        help_text=_('Defines how to trigger the animation.')
    )

    duration = models.PositiveSmallIntegerField(
        _('duration'),
        blank=False, null=False, default=200,
        help_text=_('Animation duration, in frames.')
    )

    delay = models.PositiveSmallIntegerField(
        _('delay'),
        blank=False, null=False, default=0,
        help_text=_('Time between the drawing of first and last path, in '
                    'frames (only for delayed animations).')
    )

    # on_ready
    # Function called when the instance is ready to play.

    # path_timing_function
    # Timing animation function for each path element of the SVG.

    # anim_timing_function
    # Timing animation function for the complete SVG.

    dash_gap = models.PositiveSmallIntegerField(
        _('dash gap'),
        blank=False, null=False, default=2,
        help_text=_('Whitespace extra margin between dashes. Increase it in '
                    'case of glitches at the initial state of the animation.')
    )

    force_render = models.NullBooleanField(
        _('force render'), default=None,
        help_text=_('Force the browser to re-render all updated path items. '
                    'By default, the value is true on IE only.')
    )

    reverse_stack = models.BooleanField(
        _('reverse stack'), default=False,
        help_text=_("Reverse the order of execution. The default behaviour "
                    "is to render from the first 'path' in the SVG to the "
                    "last one. This option allow you to reverse the order.")
    )

    self_destroy = models.BooleanField(
        _('self destroy'), default=False,
        help_text=_('Removes all extra styling on the SVG, and leaves it as '
                    'original.')
    )

    def __str__(self):
        return str(self.svg_file)

    class Meta:
        verbose_name = _('Drawing animation on SVG')
        verbose_name_plural = _('Drawing animations on SVG')
