from django.db import models
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password



class Category(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
class About(models.Model):
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return "About Page Content"
        
class User(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        """Hash the password before saving."""
        if not self.password.startswith('pbkdf2_sha256$'):  # Avoid rehashing if already hashed
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username




