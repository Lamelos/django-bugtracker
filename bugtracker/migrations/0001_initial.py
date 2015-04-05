# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('attachment', models.FileField(null=True, upload_to=b'bugtracker', blank=True)),
                ('status', models.CharField(max_length=1,
                                            choices=[(b'I', b'Initial'), (b'A', b'Awaiting Update'), (b'F', b'Fixed'),
                                                     (b'W', b"Won't Fix")])),
                ('priority',
                 models.CharField(max_length=1, choices=[(b'L', b'Low'), (b'M', b'Medium'), (b'H', b'High')])),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated_time'],
            },
        ),
        migrations.CreateModel(
            name='TicketUpdate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('update_text', models.TextField()),
                ('attachment', models.FileField(null=True, upload_to=b'bugtracker', blank=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('ticket', models.ForeignKey(to='bugtracker.Ticket')),
                ('updated_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated_time'],
            },
        ),
    ]
