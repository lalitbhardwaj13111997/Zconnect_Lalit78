# Generated by Django 3.2.12 on 2022-09-21 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets_analysis', '0008_auto_20220920_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=10000)),
            ],
        ),
        migrations.RemoveField(
            model_name='tata_tweets',
            name='location',
        ),
        migrations.RemoveField(
            model_name='tata_tweets',
            name='twitter_id',
        ),
    ]