# Generated by Django 4.0 on 2021-12-22 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jat', '0002_remove_newapplication_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newapplication',
            name='status',
            field=models.CharField(default='Applied', max_length=30),
            preserve_default=False,
        ),
    ]
