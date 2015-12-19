# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_auto_20151218_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profimg',
            field=models.ImageField(upload_to=b'images', blank=True),
        ),
    ]
