# Generated by Django 3.0.8 on 2020-09-18 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mush_store', '0003_auto_20200917_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='departmentadverts',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mush_store.Category'),
        ),
        migrations.AddField(
            model_name='productadverts',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mush_store.Category'),
        ),
    ]
