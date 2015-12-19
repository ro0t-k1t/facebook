# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0003_friendship'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('initiator', models.ForeignKey(related_name='poke_initiator_set', to=settings.AUTH_USER_MODEL)),
                ('receiver', models.ForeignKey(related_name='poke_receiver_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
