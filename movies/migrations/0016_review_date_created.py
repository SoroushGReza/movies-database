# Generated by Django 4.2.4 on 2023-08-24 17:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_review_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
