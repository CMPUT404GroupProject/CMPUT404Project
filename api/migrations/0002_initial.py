# Generated by Django 4.1.2 on 2022-11-21 21:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('author', models.OneToOneField(default='author', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
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
                ('contentType', models.CharField(blank=True, default='text/plain', max_length=50, null=True)),
                ('categories', models.CharField(max_length=50)),
                ('count', models.IntegerField(default=0)),
                ('comments', models.CharField(blank=True, max_length=200, null=True)),
                ('published', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('visibility', models.CharField(blank=True, default='PUBLIC', max_length=50, null=True)),
                ('unlisted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_author', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('inbox', models.ManyToManyField(to='api.inbox')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(max_length=50)),
                ('summary', models.TextField()),
                ('type', models.CharField(max_length=50)),
                ('object', models.CharField(max_length=1024)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_author', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like_comment', to='api.comment', verbose_name='Comment')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like_post', to='api.post', verbose_name='Post')),
            ],
        ),
        migrations.AddField(
            model_name='followrequest',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='followrequest',
            name='inbox',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.inbox'),
        ),
        migrations.AddField(
            model_name='followrequest',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='object', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_post', to='api.post', verbose_name='Post'),
        ),
    ]
