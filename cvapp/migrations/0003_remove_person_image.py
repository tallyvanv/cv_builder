# Generated by Django 3.0.5 on 2020-05-23 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvapp', '0002_auto_20200523_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='image',
        ),
    ]