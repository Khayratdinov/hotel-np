from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='images/service/', blank=True)
    description = models.TextField(blank=True)
    text = RichTextUploadingField(blank=True)
    icon = models.CharField(max_length = 150, blank=True)

    def __str_(self):
        return self.title


class Image_service(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='Images')
    image = models.ImageField(upload_to='images/service/', blank=True)

    def __str__(self):
        return str(self.service)


class Special_offer(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/offers/')
    description = models.TextField(blank=True)
    text = RichTextUploadingField(blank=True, null=True)
    price = models.CharField(max_length=100)
    hot_offer = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Image_offer(models.Model):
    special_offer = models.ForeignKey(Special_offer, on_delete=models.CASCADE, related_name='Images')
    image = models.ImageField(upload_to='images/offers/', blank=True)

    def __str__(self):
        return str(self.special_offer)


class Offer_order(models.Model):
    STATUS = (
        ('New', 'Yangi'),
        ('Accepted', 'Qabul qilindi'),
    )
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date = models.DateTimeField('date joined', default=timezone.now)
    text = RichTextUploadingField(blank=True, null=True)
    select = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS)
    ip = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Gallery(models.Model):
    STATUS = (
        ('*', '*'),
        ('filter-restaurant', 'filter-restaurant'),
        ('filter-room', 'filter-room'),
        ('filter-fitess', 'filter-fitess'),
        ('filter-spa', 'filter-spa'),
        ('filter-swimming', 'filter-swimming'),
        ('filter-other', 'filter-other'),
        
    )
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/gallery/')
    cat_filter = models.CharField(max_length=255, choices=STATUS)
    category = models.ForeignKey('Category_gallery', on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title


class Category_gallery(models.Model):
    STATUS = (
        ('*', '*'),
        ('.filter-restaurant', '.filter-restaurant'),
        ('.filter-room', '.filter-room'),
        ('.filter-fitess', '.filter-fitess'),
        ('.filter-spa', '.filter-spa'),
        ('.filter-swimming', '.filter-swimming'),
        ('.filter-other', '.filter-other'),
        
    )
    title = models.CharField(max_length=50, blank=True)
    cat_filter = models.CharField(max_length=255, choices=STATUS)


    def __str__(self):
        return self.title

class Our_Staff(models.Model):
    name = models.CharField(max_length=250)
    surename = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/staff/')
    description = models.CharField(max_length=250)
    profession = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    phone = models.CharField(max_length=150, blank=True)
    telegram = models.CharField(max_length=150, blank=True)
    instagram = models.CharField(max_length=150, blank=True)
    facebook = models.CharField(max_length=150, blank=True)
    category = models.ForeignKey('Category_staff', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category_staff(models.Model):
    STATUS = (
        ('*', '*'),
        ('Restaurant', 'Restaurant'),
        ('Spa - Beauty & Health', 'Spa - Beauty & Health'),
        ('Conference Room', 'Conference Room'),
        ('Swimming Pool', 'Swimming Pool'),
        ('Fitness', 'Fitness'),
        
    )
    title = models.CharField(max_length=100)
    cat_filter = models.CharField(max_length=255, choices=STATUS)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Restaurant_menu(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(blank=True, upload_to='images/restaurant-menu/')
    price = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Events(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/events/')
    description = models.CharField(max_length=250)
    text = RichTextUploadingField(blank=True, null=True)
    date = models.DateTimeField('date joined', default=timezone.now)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Image_events(models.Model):
    events = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='Images')
    image = models.ImageField(upload_to='images/events/', blank=True)

    def __str__(self):
        return str(self.events)

class Offer_events_ticket(models.Model):
    STATUS = (
        ('New', 'Yangi'),
        ('Accepted', 'Qabul qilindi'),
    )
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    events = models.ForeignKey(Events, on_delete=models.CASCADE)
    text = RichTextUploadingField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS)
    ip = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Place(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/place/')
    description = models.CharField(max_length=250)
    text = RichTextUploadingField(blank=True, null=True)
    status = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Image_place(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='Images')
    image = models.ImageField(upload_to='images/place/', blank=True)

    def __str__(self):
        return str(self.place)