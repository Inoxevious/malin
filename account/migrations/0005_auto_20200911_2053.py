# Generated by Django 3.0.8 on 2020-09-11 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200911_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='noticeboard',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
