# Generated by Django 3.1.6 on 2021-02-22 22:06

from django.db import migrations, models
import myApp.utils


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210222_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='unnamed.png', upload_to=myApp.utils.uuid_name_upload_to),
        ),
    ]
