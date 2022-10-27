# Generated by Django 4.1.2 on 2022-10-27 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0007_remove_followers_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='followers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]