# Generated by Django 3.0.8 on 2020-09-18 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mush_store', '0005_departmentadverts_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
