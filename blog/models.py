from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField



class Blog(models.Model):
    STATUS =(
        ('True', 'Mavjud'),
        ('False', 'Mavjud emas'),
    )
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True,upload_to='images/blog/')
    description = models.CharField(max_length=300, blank=True)
    text = RichTextUploadingField(blank=True, null=True)
    author = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.title

class Comment_blog(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=55, blank=True)
    surname = models.CharField(max_length=55, blank=True)
    phone = models.IntegerField()
    comment = models.TextField(max_length=255,blank=True)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


