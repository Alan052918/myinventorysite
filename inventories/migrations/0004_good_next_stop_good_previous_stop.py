# Generated by Django 4.0.1 on 2022-01-18 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventories', '0003_good_update_description_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='next_stop',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='good',
            name='previous_stop',
            field=models.CharField(default='', max_length=50),
        ),
    ]
