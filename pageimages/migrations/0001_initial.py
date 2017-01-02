# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', mezzanine.core.fields.FileField(max_length=200, verbose_name='File')),
                ('type', models.CharField(choices=[('BACKGROUND', 'Background image for the page')], max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='PageImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', mezzanine.core.fields.FileField(max_length=200, verbose_name='File')),
                ('type', models.CharField(choices=[('BACKGROUND', 'Background image for the page')], max_length=32)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Page')),
            ],
            options={
                'verbose_name_plural': 'Pages Images',
                'verbose_name': 'Page-Image',
            },
        ),
    ]
