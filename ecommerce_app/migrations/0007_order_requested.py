# Generated by Django 3.0.8 on 2020-11-10 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0006_order_shippig_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='requested',
            field=models.BooleanField(default=False),
        ),
    ]