# Generated by Django 3.2.12 on 2022-09-20 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets_analysis', '0007_auto_20220920_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tata_tweets',
            name='location',
            field=models.CharField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='tata_tweets',
            name='tweet_text',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='tata_tweets',
            name='twitter_id',
            field=models.CharField(max_length=10000),
        ),
    ]