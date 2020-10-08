# Generated by Django 3.0.8 on 2020-10-06 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_about_us'),
        ('ecommerce_app', '0002_auto_20181206_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(blank=True, max_length=70, null=True)),
                ('long_name', models.CharField(blank=True, max_length=70, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d')),
                ('description', models.TextField(blank=True, null=True)),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Department')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='product',
            name='isAvailable',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='long_name',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='major_color',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='restoke_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size1_model_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/models/products/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='product',
            name='size2_model_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/models/products/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='product',
            name='size3_model_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/models/products/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='product',
            name='size4_model_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/models/products/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(blank=True, max_length=70, null=True)),
                ('long_name', models.CharField(blank=True, max_length=70, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d')),
                ('description', models.TextField(blank=True, null=True)),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAdverts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d')),
                ('video', models.FileField(blank=True, null=True, upload_to='media/%Y/%m/%d')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('statement', models.TextField(blank=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('isFaceBanner', models.BooleanField(default=True)),
                ('written_date', models.DateTimeField()),
                ('published_date', models.DateTimeField()),
                ('expire_date', models.DateTimeField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.Category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.Product')),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentAdverts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d')),
                ('video', models.FileField(blank=True, null=True, upload_to='media/%Y/%m/%d')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('statement', models.TextField(blank=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('isFaceBanner', models.BooleanField(default=True)),
                ('written_date', models.DateTimeField()),
                ('published_date', models.DateTimeField()),
                ('expire_date', models.DateTimeField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.Category')),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Department')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.Product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.SubCategory'),
        ),
    ]
