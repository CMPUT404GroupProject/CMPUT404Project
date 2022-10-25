# Generated by Django 4.1.2 on 2022-10-24 00:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('type', models.CharField(max_length=50)),
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=200)),
                ('host', models.CharField(max_length=200)),
                ('displayName', models.CharField(max_length=80)),
                ('github', models.CharField(max_length=200)),
                ('profileImage', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('summary', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_author', to='api.author', verbose_name='Author')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_object', to='api.author', verbose_name='Object')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('type', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=200)),
                ('origin', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('contentType', models.CharField(max_length=50)),
                ('categories', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
                ('comments', models.CharField(max_length=200)),
                ('published', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('visibility', models.CharField(max_length=50)),
                ('unlisted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_author', to='api.author', verbose_name='Actor')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(max_length=50)),
                ('summary', models.TextField()),
                ('type', models.CharField(max_length=50)),
                ('object', models.CharField(max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_author', to='api.author', verbose_name='Author')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('type', models.CharField(max_length=50)),
                ('comment', models.TextField()),
                ('contentType', models.CharField(max_length=50)),
                ('published', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to='api.author', verbose_name='Author')),
            ],
        ),
    ]
