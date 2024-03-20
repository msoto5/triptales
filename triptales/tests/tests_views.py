from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from triptales.models import VacationPost, Country, Location, UserProfile


class IndexPageViewTest(TestCase):
    def test_index_view_status_code(self):
        response = self.client.get(reverse('triptales:index'))
        self.assertEqual(response.status_code, 200)

class AboutPageViewTest(TestCase):
    def test_about_view_status_code(self):
        response = self.client.get(reverse('triptales:about'))
        self.assertEqual(response.status_code, 200)

class ContactUsPageViewTest(TestCase):
    def test_contact_us_index_view_status_code(self):
        response = self.client.get(reverse('triptales:contact_us'))
        self.assertEqual(response.status_code, 200)

class AddCountryPageViewTest(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(username='testuser', password='testpassword')
        test_user.save()

    def test_add_country_view_status_code_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('triptales:add_country'))
        self.assertEqual(response.status_code, 200)

    def test_add_country_view_status_code_unauthenticated(self):
        response = self.client.get(reverse('triptales:add_country'))
        self.assertEqual(response.status_code, 302)

class AddLocationPageViewTest(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(username='testuser', password='testpassword')
        test_user.save()

    def test_add_location_view_status_code_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('triptales:add_location'))
        self.assertEqual(response.status_code, 200)

    def test_add_location_view_status_code_unauthenticated(self):
        response = self.client.get(reverse('triptales:add_location'))
        self.assertEqual(response.status_code, 302)

class FAQPageViewTest(TestCase):
    def test_faq_index_view_status_code(self):
        response = self.client.get(reverse('triptales:FAQ'))
        self.assertEqual(response.status_code, 200)

class PostDetailPageViewTest(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(username='testuser', password='testpassword')
        test_country = Country.objects.create(name='testcountry', continent='Europe')
        test_location = Location.objects.create(
            name='testlocation', 
            country=test_country, 
            vibe='Adventure', 
            setting='City', 
            travelPartners='Solo', 
            climate='Hot'
        )

        self.post = VacationPost.objects.create(
            title = 'Test',
            text = 'This is a test',
            author = test_user,
            country = test_country,
            location = test_location
        )

    def test_contact_us_index_view_status_code(self):
        response = self.client.get(reverse('triptales:post_detail', args=(self.post.id,)))
        self.assertEqual(response.status_code, 200)

class CreatePostPageViewTest(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(username='testuser', password='testpassword')
        test_user.save()

    def test_create_post_view_status_code_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('triptales:create_post'))
        self.assertEqual(response.status_code, 200)

    def test_create_post_view_status_code_unauthenticated(self):
        response = self.client.get(reverse('triptales:create_post'))
        self.assertEqual(response.status_code, 302)

class PostByContinentViewTest(TestCase):
    def test_posts_by_continent_view_status_code(self):
        test_continent = 'Europe'
        response = self.client.get(reverse('triptales:posts_by_continent', kwargs={'continent_name': test_continent}))
        self.assertEqual(response.status_code, 200)

class ProfileRegistrationViewTest(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(username='testuser', password='testpassword')
        test_user.save()

    def test_profile_registration_view_status_code_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('triptales:register_profile'))
        self.assertEqual(response.status_code, 200)
    
    def test_profile_registration_view_status_code_unauthenticated(self):
        response = self.client.get(reverse('triptales:register_profile'))
        self.assertEqual(response.status_code, 302)

class EditProfileViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        UserProfile.objects.create(user=self.user, bio='Test bio')

    def test_edit_profile_view_status_code(self):
        response = self.client.get(reverse('triptales:edit_profile'))
        self.assertEqual(response.status_code, 200)

class ProfileViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        UserProfile.objects.create(user=self.user, bio='Test bio')

    def test_profile_view_status_code(self):
        response = self.client.get(reverse('triptales:profile', kwargs={'username': 'testuser'}))
        self.assertEqual(response.status_code, 200)
        


    






