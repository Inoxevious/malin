# Generated by Django 3.0.2 on 2020-06-16 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountuser',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountuser',
            name='category',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
