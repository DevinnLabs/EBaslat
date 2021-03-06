# Generated by Django 3.1.4 on 2021-01-21 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0004_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('image', models.ImageField(upload_to='')),
                ('notes', models.TextField()),
            ],
            options={
                'db_table': 'Product',
            },
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('products', models.ManyToManyField(to='dashboard.Product')),
            ],
            options={
                'db_table': 'ProductVariant',
            },
        ),
    ]
