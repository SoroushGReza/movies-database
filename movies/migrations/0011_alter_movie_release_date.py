# Generated by Django 4.2.4 on 2023-08-21 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]
