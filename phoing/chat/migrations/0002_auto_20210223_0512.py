# Generated by Django 3.1.7 on 2021-02-22 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat.group'),
        ),
        migrations.AddField(
            model_name='group',
            name='contact',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group', to='myApp.contact'),
        ),
        migrations.AddField(
            model_name='group',
            name='host',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_groups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='joined_groups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='pendings',
            field=models.ManyToManyField(blank=True, related_name='pending_groups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='rejected',
            field=models.ManyToManyField(blank=True, related_name='rejected_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]