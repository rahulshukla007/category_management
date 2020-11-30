from django.db import models
from taggit.managers import TaggableManager

class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length = 50, unique=True)
    password = models.CharField(max_length=50)


class Category(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE) # If "parent" rec gone, delete "child" rec!!!
    category_name = models.CharField(max_length=150)
  

class Product(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE) # If "parent" rec gone, delete "child" rec!!!
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=150)
    Description = models.TextField()
    Image = models.ImageField(upload_to=None, height_field=None, width_field=None)
    tags = TaggableManager()






