# Generated by Django 4.0.1 on 2022-01-18 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku_text', models.CharField(max_length=100)),
                ('description_text', models.CharField(max_length=200)),
                ('arrive_date', models.DateTimeField(verbose_name='arrival date')),
                ('update_date', models.DateTimeField(verbose_name='last update date')),
                ('update_description_text', models.CharField(max_length=200)),
                ('depart_date', models.DateTimeField(verbose_name='departure date')),
            ],
        ),
    ]
