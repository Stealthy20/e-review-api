# Generated by Django 3.2.17 on 2023-02-10 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_review_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(max_length=1),
        ),
    ]
