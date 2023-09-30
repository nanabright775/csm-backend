from django.utils import timezone
import os
import uuid
from django.conf import settings
from django.db import models

# Create your models here.

from django.contrib.auth.models import(
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
def gallery_image_file_path(instance, filename):
    """generate file name for new recipe"""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'recipe', filename)

class UserManager(BaseUserManager):
    """manager for user for the gallery"""

    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        """create and return new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class TagModel(models.Model):
    """tag to categorise the gallary"""
    tagname = models.CharField(max_length=255)
    description = models.TextField(null=True)


class GalleryModel(models.Model):
    """creating Gallary models"""
    title = models.CharField(max_length=255) 
    description = models.TextField(null=True)
    date_created = models.DateField(default=timezone.now)
    tags = models.ForeignKey(TagModel, on_delete=models.CASCADE)
 

class ImageModel(models.Model):
    """creating Image model"""
    title = models.CharField(max_length=255) 
    date_created = models.DateField(default=timezone.now)
    image = models.ImageField(null=True, upload_to=gallery_image_file_path)
    gallery = models.ForeignKey(GalleryModel, on_delete=models.CASCADE)

    
    
class Event(models.Model):
    """models for event"""
    title = models.CharField(max_length=255)
    date_started = models.DateField(default=timezone.now)
    date_ended = models.DateField(default=timezone.now)
    description = models.TextField(null=True)
    image = models.ImageField(null=True, upload_to=gallery_image_file_path)

    
    
class News(models.Model):
    """models for news"""
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = models.ImageField(null=True, upload_to=gallery_image_file_path)
    date = models.DateField(default=timezone.now)


class Programs(models.Model):
    """models for handlings programs"""
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    date = models.DateField(default=timezone.now)
    
class Anouncement(models.Model):
    """models for managing announcement"""
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    date = models.DateField(default=timezone.now)