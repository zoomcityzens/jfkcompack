# Generated by Django 3.2.8 on 2021-10-19 19:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('interest', models.CharField(choices=[('swap', 'swap'), ('upgrade', 'upgrade')], max_length=7)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=30, unique=True)),
                ('image', models.ImageField(default='car.jpg', upload_to='car_images')),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
