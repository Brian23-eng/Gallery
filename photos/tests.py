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

