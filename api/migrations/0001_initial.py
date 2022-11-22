# Generated by Django 4.1.2 on 2022-11-21 21:06

import api.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('type', models.CharField(default='comment', max_length=50)),
                ('comment', models.TextField()),
                ('contentType', models.CharField(max_length=50)),
                ('published', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('id', models.CharField(default=api.models.generate_id, max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='FollowRequest',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('type', models.CharField(default='Follow', max_length=50)),
                ('summary', models.CharField(default='You have a follow request', max_length=500)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
