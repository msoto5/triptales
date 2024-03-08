import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'triptales_project.settings')

import django

django.setup()  # This is necessary to then import the models
from django.contrib.auth.models import User
from triptales.models import VacationPost, Comment, Country, Location, UserProfile


def populate():
    countries = [
        {'name': 'China', 'continent': 'Asia'},
        {'name': 'UK', 'continent': 'Europe'},
        {'name': 'Brazil', 'continent': 'South America'},
        {'name': 'India', 'continent': 'Asia'},
        {'name': 'Canada', 'continent': 'North America'},
        {'name': 'Switzerland', 'continent': 'Europe'},
        {'name': 'Japan', 'continent': 'Asia'},
        {'name': 'Argentina', 'continent': 'South America'},
        {'name': 'Austria', 'continent': 'Europe'},
        {'name': 'Russia', 'continent': 'Asia'}

    ]

    locations = [
        {'name': 'Beijing', 'country': 'China', 'vibe': 'Romantic', 'setting': 'City', 'partner':'Solo', 'climate': 'Hot'},
        {'name': 'London', 'country': 'UK', 'vibe': 'Romantic', 'setting': 'City', 'partner':'Partner', 'climate': 'Mixed'},
        {'name': 'Rio', 'country': 'Brazil', 'vibe': 'Relaxed', 'setting': 'Beach', 'partner':'Partner', 'climate': 'Hot'},
        {'name': 'Bangalore', 'country': 'India', 'vibe': 'Adventure', 'setting': 'City', 'partner':'Solo', 'climate': 'Hot'},
        {'name': 'Toronto', 'country': 'Canada', 'vibe': 'Adventure', 'setting': 'City', 'partner':'Solo', 'climate': 'Cold'},
        {'name': 'Geneva', 'country': 'Switzerland', 'vibe': 'Adventure', 'setting': 'Mountains', 'partner':'Solo', 'climate': 'Mixed'},
        {'name': 'Tokyo', 'country': 'Japan', 'vibe': 'Adventure', 'setting': 'City', 'partner':'Solo', 'climate': 'Hot'},
        {'name': 'Buenos Aires', 'country': 'Argentina', 'vibe': 'Adventure', 'setting': 'City', 'partner':'Friends', 'climate': 'Hot'},
        {'name': 'Gmunden', 'country': 'Austria', 'vibe': 'Relaxed', 'setting': 'Mountains', 'partner':'Solo', 'climate': 'Mixed'},
        {'name': 'Moscow', 'country': 'Russia', 'vibe': 'Adventure', 'setting': 'City', 'partner':'Solo', 'climate': 'Hot'},
    ]
    users = [
        {'username': 'user1', 'password': 'qmwnebrv', 'email': 'user1@triptales.com'},
        {'username': 'user2', 'password': 'qmwnebrv', 'email': 'user2@triptales.com'},
        {'username': 'user3', 'password': 'qmwnebrv', 'email': 'user3@triptales.com'},
    ]

    vacation_posts = [
        {'text': 'This is the first post by user1.', 'author': 'user1', 'country': 'China', 'location': 'Beijing'},
        {'text': 'This is the second post by user1.', 'author': 'user1', 'country': 'UK', 'location': 'London'},
        {'text': 'This is the first post by user2.', 'author': 'user2', 'country': 'Japan', 'location': 'Tokyo'},
        {'text': 'This is the second post by user2.', 'author': 'user2', 'country': 'Austria', 'location': 'Gmunden'},
        {'text': 'This is the first post by user3.', 'author': 'user3', 'country': 'Canada', 'location': 'Toronto'},
        {'text': 'This is the second post by user3.', 'author': 'user3', 'country': 'Switzerland',
         'location': 'Geneva'},
    ]

    # Create
    for country in countries:
        c = add_country(country['name'], country['continent'])
        for location in locations:
            if location['country'] == country['name']:
                l = add_location(location['name'], c, location['vibe'], location['setting'], location['partner'], location['climate'])

    for user in users:
        u = add_user(user['username'], user['password'], user['email'])
        for post in vacation_posts:
            if post['author'] == user['username']:
                country = Country.objects.get(name=post['country'])
                location = Location.objects.get(name=post['location'])
                add_post(post['text'], u, country, location)


def add_user(username, password, email):
    user = User.objects.get_or_create(username=username, email=email)[0]
    user.set_password(password)
    user.save()
    return user


def add_post(text, author, country, location):
    user = User.objects.get(username=author)
    post = VacationPost.objects.get_or_create(text=text, author=user, country=country, location=location)[0]
    post.likes = 0
    post.save()
    return post


def add_country(name, continent):
    country = Country.objects.get_or_create(name=name, continent=continent)[0]
    country.posts = 0
    country.views = 0
    country.save()
    return country


def add_location(name, country, vibe, setting, partner, climate):
    location = Location.objects.get_or_create(name=name, country=country)[0]
    location.posts = 0
    location.views = 0
    location.vibe = vibe
    location.setting = setting
    location.partner = partner
    location.climate = climate
    location.save()
    return location


if __name__ == '__main__':
    print('Starting TripTales population script...')
    populate()
