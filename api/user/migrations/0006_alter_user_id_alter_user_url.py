# Generated by Django 4.1.2 on 2022-10-20 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0005_alter_user_id_alter_user_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='dda1b410b77ede8a7f421954a3fbd8c266179aa8b65362d2f2160f664e6fd69e', max_length=128, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='url',
            field=models.CharField(default='http://127.0.0.1:8000/authors/dda1b410b77ede8a7f421954a3fbd8c266179aa8b65362d2f2160f664e6fd69e', max_length=255),
        ),
    ]
