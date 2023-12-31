# Generated by Django 4.2.6 on 2023-12-17 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='address',
            field=models.CharField(max_length=255),
        ),
    ]
