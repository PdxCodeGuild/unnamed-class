# Generated by Django 3.2.8 on 2021-11-17 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20211117_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]