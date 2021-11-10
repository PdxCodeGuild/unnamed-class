# Generated by Django 3.2.8 on 2021-11-10 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_alter_tweet_published_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('tweet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tweets.tweet')),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='tweets.tweet')),
            ],
            bases=('tweets.tweet',),
        ),
    ]
