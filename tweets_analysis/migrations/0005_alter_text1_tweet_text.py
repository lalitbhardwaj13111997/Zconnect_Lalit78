# Generated by Django 3.2.12 on 2022-09-19 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets_analysis', '0004_auto_20220914_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text1',
            name='tweet_text',
            field=models.CharField(max_length=300),
        ),
    ]