# Generated by Django 3.2.8 on 2021-11-17 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_rename_time_book_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
