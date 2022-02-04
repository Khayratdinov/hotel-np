from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from autoslug import AutoSlugField
from django.db.models import Count


from accounts.models import CustomUser


class Blog(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud emas'),
    )
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/blog/')
    description = models.CharField(max_length=300, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = RichTextUploadingField(blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    category = models.ForeignKey('Category_Blog', on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tag_Blog',)
    slug = AutoSlugField(populate_from='title',
                         unique=True, null=True, default=None)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def countreview(self):
        reviews = Comment_blog.objects.filter(
            blog=self, status='True').aggregate(count=Count('id'))
        cnt = 0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt


class Category_Blog(models.Model):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title',
                         unique=True, null=True, default=None)

    def __str__(self):
        return self.title


class Tag_Blog(models.Model):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title',
                         unique=True, null=True, default=None)

    def __str__(self):
        return self.title


class Comment_blog(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=55, blank=False)
    phone = models.IntegerField(blank=False)
    email = models.EmailField(blank=True, null=True)
    comment = models.TextField(max_length=355, blank=False)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
