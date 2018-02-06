# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-06 10:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0007_auto_20161016_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='VivusPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cmsplugin_vivus_vivusplugin', serialize=False, to='cms.CMSPlugin')),
                ('animation_type', models.CharField(choices=[('delayed', 'Delayed start'), ('sync', 'Synchronous'), ('oneByOne', 'One by one')], default='delayed', help_text='Defines what kind of animation will be used.', max_length=15, verbose_name='animation type')),
                ('start', models.CharField(choices=[('inViewport', 'Start once the SVG is in the viewport'), ('manual', 'Start manually'), ('autostart', 'Start right away')], default='inViewport', help_text='Defines how to trigger the animation.', max_length=15, verbose_name='animation trigger')),
                ('duration', models.PositiveSmallIntegerField(default=200, help_text='Animation duration, in frames.', verbose_name='duration')),
                ('delay', models.PositiveSmallIntegerField(default=0, help_text='Time between the drawing of first and last path, in frames (only for delayed animations).', verbose_name='delay')),
                ('dash_gap', models.PositiveSmallIntegerField(default=2, help_text='Whitespace extra margin between dashes. Increase it in case of glitches at the initial state of the animation.', verbose_name='dash gap')),
                ('force_render', models.NullBooleanField(default=None, help_text='Force the browser to re-render all updated path items. By default, the value is true on IE only.', verbose_name='force render')),
                ('reverse_stack', models.BooleanField(default=False, help_text="Reverse the order of execution. The default behaviour is to render from the first 'path' in the SVG to the last one. This option allow you to reverse the order.", verbose_name='reverse stack')),
                ('self_destroy', models.BooleanField(default=False, help_text='Removes all extra styling on the SVG, and leaves it as original.', verbose_name='self destroy')),
                ('svg_file', filer.fields.file.FilerFileField(on_delete=django.db.models.deletion.CASCADE, to='filer.File', verbose_name='SVG file')),
            ],
            options={
                'verbose_name': 'Drawing animation on SVG',
                'verbose_name_plural': 'Drawing animations on SVG',
            },
            bases=('cms.cmsplugin',),
        ),
    ]