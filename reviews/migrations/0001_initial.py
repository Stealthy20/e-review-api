# Generated by Django 3.2.17 on 2023-02-06 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('category', models.CharField(choices=[('tv', 'TV'), ('mobile phone', 'Mobile Phone'), ('tablet', 'Tablet'), ('tv accessories', 'TV Accessories'), ('mobile phone accessories', 'Mobile Phone Accessories'), ('tablet accessories', 'Tablet Accessories')], max_length=50)),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('image', models.ImageField(blank=True, default='../https://res.cloudinary.com/dz6tnfhbp/image/upload/v1675674247/istockphoto-1225193385-612x612_tdfjpj.jpg', upload_to='images/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
