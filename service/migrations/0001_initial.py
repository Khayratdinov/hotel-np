# Generated by Django 4.0.1 on 2022-01-22 10:01

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('cat_filter', models.CharField(choices=[('*', '*'), ('.filter-restaurnat', '.filter-restaurnat'), ('.filter-room', '.filter-room'), ('.filter-fitess', '.filter-fitess'), ('.filter-spa', '.filter-spa'), ('.filter-swimming', '.filter.swimming'), ('.filter-other', '.filter-other')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category_staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images/events/')),
                ('description', models.CharField(max_length=250)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Offer_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('select', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('New', 'Yangi'), ('Accepted', 'Qabul qilindi')], max_length=50)),
                ('ip', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images/place/')),
                ('description', models.CharField(max_length=250)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant_menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='images/restaurant-menu/')),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('status', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='images/service/')),
                ('description', models.TextField(blank=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('icon', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Special_offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='images/offers/')),
                ('description', models.TextField(blank=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('price', models.CharField(max_length=100)),
                ('hot_offer', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Our_Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('surename', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images/staff/')),
                ('description', models.CharField(max_length=250)),
                ('profession', models.CharField(max_length=250)),
                ('status', models.BooleanField(default=False)),
                ('phone', models.CharField(blank=True, max_length=150)),
                ('telegram', models.CharField(blank=True, max_length=150)),
                ('instagram', models.CharField(blank=True, max_length=150)),
                ('facebook', models.CharField(blank=True, max_length=150)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.category_staff')),
            ],
        ),
        migrations.CreateModel(
            name='Offer_events_ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('status', models.CharField(choices=[('New', 'Yangi'), ('Accepted', 'Qabul qilindi')], max_length=50)),
                ('ip', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('events', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.events')),
            ],
        ),
        migrations.CreateModel(
            name='Image_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/service/')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Images', to='service.service')),
            ],
        ),
        migrations.CreateModel(
            name='Image_place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/place/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Images', to='service.place')),
            ],
        ),
        migrations.CreateModel(
            name='Image_offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/offers/')),
                ('special_offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Images', to='service.special_offer')),
            ],
        ),
        migrations.CreateModel(
            name='Image_events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/events/')),
                ('events', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Images', to='service.events')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='images/gallery/')),
                ('cat_filter', models.CharField(choices=[('*', '*'), ('.filter-restaurnat', '.filter-restaurnat'), ('.filter-room', '.filter-room'), ('.filter-fitess', '.filter-fitess'), ('.filter-spa', '.filter-spa'), ('.filter-swimming', '.filter.swimming'), ('.filter-other', '.filter-other')], max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.category_gallery')),
            ],
        ),
    ]
