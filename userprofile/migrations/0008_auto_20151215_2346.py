# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_auto_20151214_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profimg',
            field=models.ImageField(null=True, upload_to=b'images', blank=True),
        ),
    ]
