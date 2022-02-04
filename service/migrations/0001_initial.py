# Generated by Django 4.0.2 on 2022-02-04 18:02

import autoslug.fields
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
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='images/service/')),
                ('description', models.TextField(blank=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('icon', models.CharField(blank=True, max_length=150)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category_gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('cat_filter', models.CharField(choices=[('*', '*'), ('.filter-restaurant', '.filter-restaurant'), ('.filter-room', '.filter-room'), ('.filter-fitess', '.filter-fitess'), ('.filter-spa', '.filter-spa'), ('.filter-swimming', '.filter-swimming'), ('.filter-business', '.filter-business'), ('.filter-other', '.filter-other')], default='*', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category_staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cat_filter', models.CharField(choices=[('*', '*'), ('Restaurant', 'Restaurant'), ('Spa - Beauty & Health', 'Spa - Beauty & Health'), ('Conference Room', 'Conference Room'), ('Swimming Pool', 'Swimming Pool'), ('Fitness', 'Fitness')], max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True)),
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
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True)),
                ('status', models.CharField(choices=[('True', 'Mavjud'), ('False', 'Mavjud emas')], default=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Fitness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='images/service/')),
                ('description', models.TextField(blank=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('icon', models.CharField(blank=True, max_length=150)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
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
                ('status', models.CharField(choices=[('True', 'Mavjud'), ('False', 'Mavjud emas')], default=True, max_length=15)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='images/service/')),
                ('description', models.TextField(blank=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('icon', models.CharField(blank=True, max_length=150)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
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
                ('status', models.CharField(choices=[('True', 'Mavjud'), ('False', 'Mavjud emas')], default=True, max_length=50)),
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
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Spa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='images/service/')),
                ('description', models.TextField(blank=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('icon', models.CharField(blank=True, max_length=150)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
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
                ('hot_offer', models.CharField(choices=[('True', 'Mavjud'), ('False', 'Mavjud emas')], default=True, max_length=50)),
                ('status', models.CharField(choices=[('True', 'Mavjud'), ('False', 'Mavjud emas')], default=True, max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True)),
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
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.category_staff')),
            ],
        ),
        migrations.CreateModel(
            name='Offer_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('text', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('New', 'Yangi'), ('Accepted', 'Qabul qilindi')], default='New', max_length=50)),
                ('ip', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offer_oreder', to='service.special_offer')),
            ],
        ),
        migrations.CreateModel(
            name='Offer_events_ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('text', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('New', 'Yangi'), ('Accepted', 'Qabul qilindi')], default='New', max_length=50)),
                ('ip', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.events')),
            ],
        ),
        migrations.CreateModel(
            name='Image_spa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/service/')),
                ('spa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Image_spa', to='service.spa')),
            ],
        ),
        migrations.CreateModel(
            name='Image_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/service/')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Images_service', to='service.service')),
            ],
        ),
        migrations.CreateModel(
            name='Image_restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/service/')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Image_restaurant', to='service.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Image_place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/place/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Images_place', to='service.place')),
            ],
        ),
        migrations.CreateModel(
            name='Image_offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/offers/')),
                ('special_offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Images_offer', to='service.special_offer')),
            ],
        ),
        migrations.CreateModel(
            name='Image_fitness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/service/')),
                ('fitness', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Image_fitness', to='service.fitness')),
            ],
        ),
        migrations.CreateModel(
            name='Image_events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/events/')),
                ('events', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Images_events', to='service.events')),
            ],
        ),
        migrations.CreateModel(
            name='Image_business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/service/')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Image_business', to='service.business')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='images/gallery/')),
                ('cat_filter', models.CharField(choices=[('*', '*'), ('filter-restaurant', 'filter-restaurant'), ('filter-room', 'filter-room'), ('filter-fitess', 'filter-fitess'), ('filter-spa', 'filter-spa'), ('filter-swimming', 'filter-swimming'), ('.filter-business', '.filter-business'), ('filter-other', 'filter-other')], default='*', max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.category_gallery')),
            ],
        ),
    ]
