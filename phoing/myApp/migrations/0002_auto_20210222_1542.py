# Generated by Django 3.1.7 on 2021-02-22 06:42

from django.db import migrations, models
import myApp.utils


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=myApp.utils.uuid_name_upload_to, verbose_name='Image'),
        ),
    ]
