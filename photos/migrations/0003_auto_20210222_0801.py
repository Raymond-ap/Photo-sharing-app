# Generated by Django 3.0.5 on 2021-02-22 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20210222_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='thumbnail',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
