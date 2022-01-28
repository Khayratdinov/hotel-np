from email.policy import default
from pyexpat import model
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.fields import CharField
from django.forms import ModelForm
from django.urls import reverse
from django.db.models import Avg, Count
from django.utils.safestring import mark_safe
from autoslug import AutoSlugField

# Create your models here.

class Category(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud emas'),
    )
    title = models.CharField(max_length = 150)
    description = models.CharField(max_length = 250, blank=True)
    image = models.ImageField(upload_to='images/category/', blank=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)
    status = models.CharField(max_length=15, choices=STATUS)
    
    
    

    def __str__(self):
        return self.title



class Room(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud emas'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length = 150)
    price = models.CharField(max_length = 250, blank=True)
    image = models.ImageField(upload_to="images/", blank=True)
    description = models.CharField(max_length = 255, blank=True)
    text = RichTextUploadingField(blank=True, null=True)
    status = models.CharField(choices=STATUS, max_length=15)
    slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = "image"

    def get_absolute_url(self):
        return reverse("room_detail", kwargs={"self": self.slug})


class RoomServices(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length = 255, blank=True)
    icon = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return str(self.title)

class Room_Image(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='Room_Images')
    image = models.ImageField(upload_to='images/rooms/', blank=True)

    def __str__(self):
        return str(self.room)

class Order(models.Model):
    STATUS = (
        ('New', 'Yangi'),
        ('Accepted', 'Qabul qilindi'),
    )
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100)
    citizenship = models.CharField(max_length=100, blank=True)
    pay = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    guest = models.IntegerField()
    children = models.IntegerField(blank=True)
    arrival = models.CharField(max_length=100)
    departure = models.CharField(max_length=100, blank=True)
    room = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=50, choices=STATUS)
    select = models.CharField(max_length=100)
    comment = models.TextField(blank=True, max_length=300)
    ip = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

        
class Comment(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud emas'),
    )    
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    comment = models.TextField(max_length=300, blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'phone', 'comment', 'rate']

    def avaregereview(self):
        reviews = Comment.objects.filter(room=self,status='True').aggregate(avarage=Avg('rate'))
        avg = 0
        if reviews["avarage"] is not None:
            avg = float(reviews["avarage"])
        return avg

    def countreview(self):
        reviews = Comment.objects.filter(room=self,status='True').aggregate(count=Count('id'))
        cnt = 0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt













    
    


    
    
    