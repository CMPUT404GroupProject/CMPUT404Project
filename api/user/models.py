from email.policy import default
from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
import secrets
import random
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

curId = ""
def generate_id():
    length = 32
    id = secrets.token_hex(32)
    """ #TODO - check if id already exists in database
    while True:
        id = secrets.token_hex(32)
        if User.objects.filter(id=code).count() == 0:
            break
    """
    curId = str(id)
    return id
def generate_id_int():
    return random.randint(0,10000)

class UserManager(BaseUserManager):
    def create_user(self, displayName, github, password=None, profileImage="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png", **kwargs):
        """Create and return a `User` with an email, phone number, username and password."""
        if displayName is None:
            raise TypeError('Users must have a display name.')
        if github is None:
            raise TypeError('Users must have an github.')

        user = self.model(displayName=displayName, github=github, password=password, profileImage=profileImage)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, displayName, github, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        if github is None:
            raise TypeError('Superusers must have github.')
        if displayName is None:
            raise TypeError('Superusers must have an username.')

        user = self.create_user(displayName, github, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    type = models.CharField(max_length=32, default="author")
    id = models.CharField(max_length=128, primary_key=True, default=generate_id)
    url = models.CharField(max_length=255, default = "")
    host = models.CharField(max_length=255, default= "http://127.0.0.1:8000/")
    displayName = models.CharField(db_index=True, max_length=255, unique=True)
    #email = models.EmailField(db_index=True, unique=True,  null=True, blank=True)
    github = models.URLField(db_index=True, unique=True,  null=True, blank=True)
    profileImage = models.URLField(max_length=500, default="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'displayName'
    REQUIRED_FIELDS = ['github']

    objects = UserManager()

    def __str__(self):
        return f"{self.github}"

    def save(self, *args, **kwargs):
        self.url = "http://127.0.0.1:8000/authors/" + str(self.id)
        return super(User, self).save(*args, **kwargs)

    
class Followers(models.Model):
    type = models.CharField(max_length=50)
    id = models.CharField(max_length=200, primary_key=True)
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    created = models.DateTimeField(default=datetime.now, blank=True)
    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)