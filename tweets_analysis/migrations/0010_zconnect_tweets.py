# Generated by Django 3.2.12 on 2022-10-11 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets_analysis', '0009_auto_20220921_0719'),
    ]

    operations = [
        migrations.CreateModel(
            name='zconnect_tweets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zconnect_tweets', models.CharField(max_length=10000)),
            ],
        ),
    ]
