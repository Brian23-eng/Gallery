from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.location_name
    def save_location(self):
        self.save
        
    def delete_location(self):
        self.delete
        
    def update_location(self):
        self.update
        
    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(location_name=value)
    
    
class Category(models.Model):
    category_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.category_name
    
    def save_category(self):
        self.save
        
    def delete_category(self):
        self.delete
        
    def update_category(self):
        self.update
        
    @classmethod
    def update_category(cls, id, value):
        cls.objects.filter(id=id).update(category_name=value)
    
    
class Image(models.Model):
    image_name = models.CharField(max_length=20)
    image_description = models.TextField(max_length=60)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'pics')
    
    def __str__(self):
        return self.image_name
    
    
    def save_image(self):
        self.save
        
    def delete_image(self):
        self.delete
        
    class Meta:
        ordering = ['image_name']
        
    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    
    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)
        
    @classmethod
    def get_image_by_id(cls, search_term):
        image = cls.objects.filter(image__image_id__icontains=search_term)
        return image

    @classmethod
    def filter_by_location(cls,search_term):
        locations = cls.objects.filter(location__location_name__icontains=search_term)
        return locations
    
    @classmethod
    def search_by_category(cls,location):
        photos=cls.objects.filter(category__icontains=search_term)
        return photos
