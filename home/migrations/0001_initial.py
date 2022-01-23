# Generated by Django 4.0.1 on 2022-01-22 10:00

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('recommended_logo', models.ImageField(upload_to='images/')),
                ('logo', models.ImageField(upload_to='images/')),
                ('hotel_star', models.CharField(max_length=500)),
                ('hotel_name', models.CharField(max_length=30)),
                ('short_description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('message', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('New', 'Yangi'), ('Read', 'Read'), ('Closed', 'Yopilgan')], default='New', max_length=15)),
                ('ip', models.CharField(blank=True, max_length=50)),
                ('note', models.CharField(blank=True, max_length=100)),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordernumber', models.IntegerField()),
                ('question', models.CharField(max_length=1000)),
                ('answer', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('True', 'Mavjud'), ('False', 'Mavjud emas')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Informations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('keyword', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('fax', models.CharField(blank=True, max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('telegram', models.CharField(blank=True, max_length=255)),
                ('instagram', models.CharField(blank=True, max_length=255)),
                ('facebook', models.CharField(blank=True, max_length=255)),
                ('youtube', models.CharField(blank=True, max_length=255)),
                ('twitter', models.CharField(blank=True, max_length=255)),
                ('linkedin', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('True', 'Mavjud'), ('False', 'Mavjud emas')], default='True', max_length=15)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('detail', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(upload_to='images/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='LicImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.license')),
            ],
        ),
    ]