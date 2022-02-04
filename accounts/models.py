from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator


class CustomUser(AbstractUser):
    USER = 1
    REGISTRATION = 2
    ADMIN = 3
    USER_TYPE = [
        (USER, "User"),
        (REGISTRATION, "Registration"),
        (ADMIN, "Admin"),
    ]
    full_name = models.CharField('full name', max_length=200, blank=False, null=False)
    avatar = models.ImageField(upload_to="images/profiles/avatars/", null=True, blank=True)
    email = models.EmailField('email address', blank=False, null=False, unique=True)
    bio = models.TextField(default="no bio...", max_length=400)
    birthday = models.DateField(null=True, blank=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE, null=True, blank=True , default=1)
    phone = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    zip = models.CharField(max_length=30, null=True, blank=True)
    username_validator = UnicodeUsernameValidator()
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        null=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )

    def __str__(self):
        return str(self.username)
