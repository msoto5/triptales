from django.test import TestCase
from triptales.models import *
from django.contrib.auth.models import User
from django.utils import timezone

class CountryModelTest(TestCase):
    def test_country_creation(self):
        country = Country.objects.create(name='TestCountry', continent='Europe')
        self.assertEqual(country.name, 'TestCountry')

    def test_country_slug_creation(self):
        country = Country.objects.create(name='Test Country', continent='Europe')
        self.assertEqual(country.slug, 'test-country')

class LocationModelTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name='TestCountry', continent='Asia')

    def test_location_creation(self):
        location = Location.objects.create(
            name='TestLocation',
            country=self.country,
            vibe='Adventure',
            setting='City',
            travelPartners='Solo',
            climate='Hot'
        )

        self.assertEqual(location.__str__(), 'TestLocation')
        self.assertEqual(location.slug, 'testlocation')

class VacationPostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.country = Country.objects.create(name='TestCountry', continent='Africa')
        self.location = Location.objects.create(
            name='TestLocation',
            country=self.country,
            vibe='Adventure',
            setting='City',
            travelPartners='Solo',
            climate='Hot'
        )

    def test_vacation_post_creation(self):
        post = VacationPost.objects.create(
            title='TestPost',
            text='Testing...',
            author=self.user,
            country=self.country,
            location=self.location,
            created_at=timezone.now()
        )

        self.assertEqual(post.__str__(), 'TestPost by testuser')

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = VacationPost.objects.create(
            title='TestPost',
            text='Testing...',
            author=self.user,
        )

    def test_comment_creation(self):
        comment = Comment.objects.create(user=self.user, post=self.post, text='Test Comment')
        self.assertIn("commented on", comment.__str__())

class UserProfileModelTest(TestCase):
    def test_user_profile_creation(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        profile = UserProfile.objects.create(user=user, bio="Test Bio")
        self.assertEqual(profile.__str__(), "testuser")