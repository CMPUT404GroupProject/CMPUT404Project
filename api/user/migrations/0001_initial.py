# Generated by Django 4.1.2 on 2022-11-25 12:07

import api.user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('type', models.CharField(default='author', max_length=32)),
                ('id', models.CharField(default=api.user.models.generate_id, max_length=128, primary_key=True, serialize=False)),
                ('url', models.CharField(default='', max_length=255)),
                ('host', models.CharField(default='https://socialdistribution-cmput404.herokuapp.com/', max_length=255)),
                ('displayName', models.CharField(db_index=True, max_length=255, unique=True)),
                ('github', models.URLField(blank=True, db_index=True, null=True, unique=True)),
                ('profileImage', models.URLField(default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png', max_length=500)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
