# Generated by Django 3.2.8 on 2021-11-05 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='deleted',
            field=models.BooleanField(auto_created=True, default=False),
        ),
        migrations.AlterField(
            model_name='groceryitem',
            name='is_complete',
            field=models.BooleanField(auto_created=True, default=False),
        ),
    ]
