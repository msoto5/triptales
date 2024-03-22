from django.test import TestCase
from triptales.forms import *
from triptales.models import *
from django.core.files.uploadedfile import SimpleUploadedFile
import os

class CountryFormTest(TestCase):
    def test_valid_date(self):
        form = CountryForm({
            'name': 'TestCountry',
            'continent': 'Europe',
        })

        self.assertTrue(form.is_valid())
    
    def test_form_saves_correctly(self):
        form = CountryForm({
            'name': 'SaveTest',
            'continent': 'Asia',
        })

        if form.is_valid():
            country = form.save()
            self.assertEqual(country.name, 'SaveTest')
            self.assertEqual(country.continent, 'Asia')

class LocationFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.country = Country.objects.create(name="TestCountry", continent="Europe")

    def test_location_form_valid_data(self):
        form = LocationForm({
            'name': 'TestLocation',
            'country': self.country.id,
            'vibe': 'Adventure',
            'setting': 'City',
            'travelPartners': 'Solo',
            'climate': 'Hot',
        })
        self.assertTrue(form.is_valid())

    def test_location_form_invalid_data(self):
        form = LocationForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)  

class VacationPostFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        country = Country.objects.create(name="TestCountry", continent="Europe")
        cls.location = Location.objects.create(
            name="TestLocation", 
            country=country, 
            vibe="Adventure", 
            setting="City", 
            travelPartners="Solo", 
            climate="Hot"
            )

    def test_vacation_post_form_valid_data(self):
        image_path = os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'images', 'asia.webp')
        with open(image_path, 'rb') as image_file:
            test_image = SimpleUploadedFile(name='asia.webp', content=image_file.read(), content_type='image/webp')
        
        form_data = {
            'title': 'Test Post',
            'text': 'Testing...',
            'location': self.location.id,
        }
        form_files = {
            'image': test_image
        }
        
        form = VacationPostForm(data=form_data, files=form_files)
        self.assertTrue(form.is_valid())

    def test_vacation_post_form_save(self):
        image_path = os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'images', 'asia.webp')
        with open(image_path, 'rb') as image_file:
            test_image = SimpleUploadedFile(name='asia.webp', content=image_file.read(), content_type='image/webp')

        form_data = {
            'title': 'Test Post',
            'text': 'Testing...',
            'location': self.location.id,
        }
        form_files = {
            'image': test_image
        }

        form = VacationPostForm(data=form_data, files=form_files)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.create_user(username='testuser', password='testpassword')
            post.save()
            self.assertEqual(post.title, 'Test Post')
