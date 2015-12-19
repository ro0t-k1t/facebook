# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20151214_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profimg',
            field=models.ImageField(default=b"{%  media 'images/default.jpg' %}", upload_to=b'images'),
        ),
    ]
