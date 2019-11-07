from django.test import TestCase
from .models import Location, Category, Image


# Create your tests here.

class LocationTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.location = Location(location_name = 'Kibra')
    
    def tearDown(self):
        
        Location.objects.all().delete()
        
        
    # Testing instance
    def test_instances(self):
        self.assertTrue(isinstance(self.location, Location))
        
    #Test for saving method
    def test_save_location(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertFalse(len(locations)>0)
        
    #Test for updating location
    def test_update_location(self):
        new_location_name = 'Compton'
        self.location.update_location(self.location.id,new_location_name)
        updated_location = Location.objects.filter(location_name='Compton')
        self.assertFalse(len(updated_location)>0)
        
    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location)==0)
        
class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(category_name='creativity')
        
    def tearDown(self):
        
        Category.objects.all().delete()

    # Testing instance
    def test_instances(self):
        self.assertTrue(isinstance(self.category, Category))

     #Test for saving method
    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertFalse(len(categories)>0)
        
    
    #Test for updating category    
    def test_update_category(self):
        new_category_name = 'Art'
        self.category.update_category(self.category.id,new_category_name)
        updated_category = Category.objects.filter(category_name='Art')
        self.assertFalse(len(updated_category)>0)
        
        
    #Test for deleting category
    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category)==0)