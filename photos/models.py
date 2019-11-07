from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.location_name
    
    
class Category(models.Model):
    category_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.category_name
    
    
class Image(models.Model):
    image_name = models.CharField(max_length=20),
    image_description = models.CharField(max_length=50),
    location = models.ForeignKey(Location, on_delete=models.CASCADE),
    category = models.ForeignKey(Category, on_delete=models.CASCADE),
    image = models.ImageField(upload_to = 'pics')
    