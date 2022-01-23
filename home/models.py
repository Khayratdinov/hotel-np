from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe


class Informations(models.Model):
    STATUS =(
        ('True', 'Mavjud'),
        ('False', 'Mavjud emas'),
    )
    title = models.CharField(max_length=255)
    keyword = models.CharField(max_length=300)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(blank=True, max_length=20)
    fax = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True,upload_to='images/')
    telegram = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255,blank=True)
    youtube = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    linkedin = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class License(models.Model): 
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    detail = RichTextUploadingField()
    image = models.ImageField(upload_to='images/')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))
    image_tag.short_description = 'Image'

class LicImages(models.Model):
    license = models.ForeignKey(License,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True,upload_to='images/')

    def __str__(self):
        return self.title 


class ContactMessage(models.Model):
    STATUS = (
        ('New', 'Yangi'),
        ('Read', 'Read'),
        ('Closed', 'Yopilgan'),
    )
    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    phone = models.CharField(blank=True, max_length=255)
    subject = models.CharField(blank=True, max_length=50)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=50)
    note = models.CharField(blank=True, max_length=100)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class FAQ(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False','Mavjud emas'),
    )
    ordernumber = models.IntegerField()
    question = models.CharField(max_length=1000)
    answer = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS,)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class AboutUs(models.Model):
    title = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='images/')
    description = RichTextUploadingField()
    recommended_logo = models.ImageField(upload_to='images/')

    # For About Hotel
    logo = models.ImageField(upload_to='images/')
    hotel_star = models.CharField(max_length=500)
    hotel_name = models.CharField(max_length=30)
    short_description = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title