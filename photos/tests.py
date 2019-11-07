from django.test import TestCase
from .models import Location, Category, Image


# Create your tests here.

class LocationTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.kibra = Location(location_name = 'Kibra')
        
        
    # Testing instance
    def test_instances(self):
        self.assertTrue(isinstance(self.kibra, Location))
        
