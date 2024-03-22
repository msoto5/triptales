import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'triptales_project.settings')

import django

django.setup()  # This is necessary to then import the models
from django.contrib.auth.models import User
from triptales.models import VacationPost, Comment, Country, Location, UserProfile


def populate():
    countries = [
        {'name': 'Algeria', 'continent': 'Africa'},
        {'name': 'Angola', 'continent': 'Africa'},
        {'name': 'Benin', 'continent': 'Africa'},
        {'name': 'Botswana', 'continent': 'Africa'},
        {'name': 'Burkina', 'continent': 'Africa'},
        {'name': 'Burundi', 'continent': 'Africa'},
        {'name': 'Cameroon', 'continent': 'Africa'},
        {'name': 'Cape Verde', 'continent': 'Africa'},
        {'name': 'Central African Republic', 'continent': 'Africa'},
        {'name': 'Chad', 'continent': 'Africa'},
        {'name': 'Comoros', 'continent': 'Africa'},
        {'name': 'Congo', 'continent': 'Africa'},
        {'name': 'Democratic Republic of Congo', 'continent': 'Africa'},
        {'name': 'Djibouti', 'continent': 'Africa'},
        {'name': 'Egypt', 'continent': 'Africa'},
        {'name': 'Equatorial Guinea', 'continent': 'Africa'},
        {'name': 'Eritrea', 'continent': 'Africa'},
        {'name': 'Ethiopia', 'continent': 'Africa'},
        {'name': 'Gabon', 'continent': 'Africa'},
        {'name': 'Gambia', 'continent': 'Africa'},
        {'name': 'Ghana', 'continent': 'Africa'},
        {'name': 'Guinea', 'continent': 'Africa'},
        {'name': 'Guinea-Bissau', 'continent': 'Africa'},
        {'name': 'Ivory Coast', 'continent': 'Africa'},
        {'name': 'Kenya', 'continent': 'Africa'},
        {'name': 'Lesotho', 'continent': 'Africa'},
        {'name': 'Liberia', 'continent': 'Africa'},
        {'name': 'Libya', 'continent': 'Africa'},
        {'name': 'Madagascar', 'continent': 'Africa'},
        {'name': 'Malawi', 'continent': 'Africa'},
        {'name': 'Mali', 'continent': 'Africa'},
        {'name': 'Mauritania', 'continent': 'Africa'},
        {'name': 'Mauritius', 'continent': 'Africa'},
        {'name': 'Morocco', 'continent': 'Africa'},
        {'name': 'Mozambique', 'continent': 'Africa'},
        {'name': 'Namibia', 'continent': 'Africa'},
        {'name': 'Niger', 'continent': 'Africa'},
        {'name': 'Nigeria', 'continent': 'Africa'},
        {'name': 'Rwanda', 'continent': 'Africa'},
        {'name': 'Sao Tome and Principe', 'continent': 'Africa'},
        {'name': 'Senegal', 'continent': 'Africa'},
        {'name': 'Seychelles', 'continent': 'Africa'},
        {'name': 'Sierra Leone', 'continent': 'Africa'},
        {'name': 'Somalia', 'continent': 'Africa'},
        {'name': 'South Africa', 'continent': 'Africa'},
        {'name': 'South Sudan', 'continent': 'Africa'},
        {'name': 'Sudan', 'continent': 'Africa'},
        {'name': 'Swaziland', 'continent': 'Africa'},
        {'name': 'Tanzania', 'continent': 'Africa'},
        {'name': 'Togo', 'continent': 'Africa'},
        {'name': 'Tunisia', 'continent': 'Africa'},
        {'name': 'Uganda', 'continent': 'Africa'},
        {'name': 'Zambia', 'continent': 'Africa'},
        {'name': 'Zimbabwe', 'continent': 'Africa'},
        {'name': 'Afghanistan', 'continent': 'Asia'},
        {'name': 'Bahrain', 'continent': 'Asia'},
        {'name': 'Bangladesh', 'continent': 'Asia'},
        {'name': 'Bhutan', 'continent': 'Asia'},
        {'name': 'Brunei', 'continent': 'Asia'},
        {'name': 'Burma (Myanmar)', 'continent': 'Asia'},
        {'name': 'Cambodia', 'continent': 'Asia'},
        {'name': 'China', 'continent': 'Asia'},
        {'name': 'East Timor', 'continent': 'Asia'},
        {'name': 'India', 'continent': 'Asia'},
        {'name': 'Indonesia', 'continent': 'Asia'},
        {'name': 'Iran', 'continent': 'Asia'},
        {'name': 'Iraq', 'continent': 'Asia'},
        {'name': 'Israel', 'continent': 'Asia'},
        {'name': 'Japan', 'continent': 'Asia'},
        {'name': 'Jordan', 'continent': 'Asia'},
        {'name': 'Kazakhstan', 'continent': 'Asia'},
        {'name': 'North Korea', 'continent': 'Asia'},
        {'name': 'South Korea', 'continent': 'Asia'},
        {'name': 'Kuwait', 'continent': 'Asia'},
        {'name': 'Kyrgyzstan', 'continent': 'Asia'},
        {'name': 'Laos', 'continent': 'Asia'},
        {'name': 'Lebanon', 'continent': 'Asia'},
        {'name': 'Malaysia', 'continent': 'Asia'},
        {'name': 'Maldives', 'continent': 'Asia'},
        {'name': 'Mongolia', 'continent': 'Asia'},
        {'name': 'Nepal', 'continent': 'Asia'},
        {'name': 'Oman', 'continent': 'Asia'},
        {'name': 'Pakistan', 'continent': 'Asia'},
        {'name': 'Philippines', 'continent': 'Asia'},
        {'name': 'Qatar', 'continent': 'Asia'},
        {'name': 'Russia', 'continent': 'Asia'},
        {'name': 'Saudi Arabia', 'continent': 'Asia'},
        {'name': 'Singapore', 'continent': 'Asia'},
        {'name': 'Sri Lanka', 'continent': 'Asia'},
        {'name': 'Syria', 'continent': 'Asia'},
        {'name': 'Tajikistan', 'continent': 'Asia'},
        {'name': 'Thailand', 'continent': 'Asia'},
        {'name': 'Turkey', 'continent': 'Asia'},
        {'name': 'Turkmenistan', 'continent': 'Asia'},
        {'name': 'United Arab Emirates', 'continent': 'Asia'},
        {'name': 'Uzbekistan', 'continent': 'Asia'},
        {'name': 'Vietnam', 'continent': 'Asia'},
        {'name': 'Yemen', 'continent': 'Asia'},
        {'name': 'Albania', 'continent': 'Europe'},
        {'name': 'Andorra', 'continent': 'Europe'},
        {'name': 'Armenia', 'continent': 'Europe'},
        {'name': 'Austria', 'continent': 'Europe'},
        {'name': 'Azerbaijan', 'continent': 'Europe'},
        {'name': 'Belarus', 'continent': 'Europe'},
        {'name': 'Belgium', 'continent': 'Europe'},
        {'name': 'Bosnia and Herzegovina', 'continent': 'Europe'},
        {'name': 'Bulgaria', 'continent': 'Europe'},
        {'name': 'Croatia', 'continent': 'Europe'},
        {'name': 'Cyprus', 'continent': 'Europe'},
        {'name': 'CZ', 'continent': 'Europe'},
        {'name': 'Denmark', 'continent': 'Europe'},
        {'name': 'Estonia', 'continent': 'Europe'},
        {'name': 'Finland', 'continent': 'Europe'},
        {'name': 'France', 'continent': 'Europe'},
        {'name': 'Georgia', 'continent': 'Europe'},
        {'name': 'Germany', 'continent': 'Europe'},
        {'name': 'Greece', 'continent': 'Europe'},
        {'name': 'Hungary', 'continent': 'Europe'},
        {'name': 'Iceland', 'continent': 'Europe'},
        {'name': 'Ireland', 'continent': 'Europe'},
        {'name': 'Italy', 'continent': 'Europe'},
        {'name': 'Latvia', 'continent': 'Europe'},
        {'name': 'Liechtenstein', 'continent': 'Europe'},
        {'name': 'Lithuania', 'continent': 'Europe'},
        {'name': 'Luxembourg', 'continent': 'Europe'},
        {'name': 'Macedonia', 'continent': 'Europe'},
        {'name': 'Malta', 'continent': 'Europe'},
        {'name': 'Moldova', 'continent': 'Europe'},
        {'name': 'Monaco', 'continent': 'Europe'},
        {'name': 'Montenegro', 'continent': 'Europe'},
        {'name': 'Netherlands', 'continent': 'Europe'},
        {'name': 'Norway', 'continent': 'Europe'},
        {'name': 'Poland', 'continent': 'Europe'},
        {'name': 'Portugal', 'continent': 'Europe'},
        {'name': 'Romania', 'continent': 'Europe'},
        {'name': 'San Marino', 'continent': 'Europe'},
        {'name': 'Serbia', 'continent': 'Europe'},
        {'name': 'Slovakia', 'continent': 'Europe'},
        {'name': 'Slovenia', 'continent': 'Europe'},
        {'name': 'Spain', 'continent': 'Europe'},
        {'name': 'Sweden', 'continent': 'Europe'},
        {'name': 'Switzerland', 'continent': 'Europe'},
        {'name': 'Ukraine', 'continent': 'Europe'},
        {'name': 'United Kingdom', 'continent': 'Europe'},
        {'name': 'Vatican City', 'continent': 'Europe'},
        {'name': 'Antigua and Barbuda', 'continent': 'North America'},
        {'name': 'Bahamas', 'continent': 'North America'},
        {'name': 'Barbados', 'continent': 'North America'},
        {'name': 'Belize', 'continent': 'North America'},
        {'name': 'Canada', 'continent': 'North America'},
        {'name': 'Costa Rica', 'continent': 'North America'},
        {'name': 'Cuba', 'continent': 'North America'},
        {'name': 'Dominica', 'continent': 'North America'},
        {'name': 'Dominican Republic', 'continent': 'North America'},
        {'name': 'El Salvador', 'continent': 'North America'},
        {'name': 'Grenada', 'continent': 'North America'},
        {'name': 'Guatemala', 'continent': 'North America'},
        {'name': 'Haiti', 'continent': 'North America'},
        {'name': 'Honduras', 'continent': 'North America'},
        {'name': 'Jamaica', 'continent': 'North America'},
        {'name': 'Mexico', 'continent': 'North America'},
        {'name': 'Nicaragua', 'continent': 'North America'},
        {'name': 'Panama', 'continent': 'North America'},
        {'name': 'Saint Kitts and Nevis', 'continent': 'North America'},
        {'name': 'Saint Lucia', 'continent': 'North America'},
        {'name': 'Saint Vincent and the Grenadines', 'continent': 'North America'},
        {'name': 'Trinidad and Tobago', 'continent': 'North America'},
        {'name': 'US', 'continent': 'North America'},
        {'name': 'Australia', 'continent': 'Oceania'},
        {'name': 'Fiji', 'continent': 'Oceania'},
        {'name': 'Kiribati', 'continent': 'Oceania'},
        {'name': 'Marshall Islands', 'continent': 'Oceania'},
        {'name': 'Micronesia', 'continent': 'Oceania'},
        {'name': 'Nauru', 'continent': 'Oceania'},
        {'name': 'New Zealand', 'continent': 'Oceania'},
        {'name': 'Palau', 'continent': 'Oceania'},
        {'name': 'Papua New Guinea', 'continent': 'Oceania'},
        {'name': 'Samoa', 'continent': 'Oceania'},
        {'name': 'Solomon Islands', 'continent': 'Oceania'},
        {'name': 'Tonga', 'continent': 'Oceania'},
        {'name': 'Tuvalu', 'continent': 'Oceania'},
        {'name': 'Vanuatu', 'continent': 'Oceania'},
        {'name': 'Argentina', 'continent': 'South America'},
        {'name': 'Bolivia', 'continent': 'South America'},
        {'name': 'Brazil', 'continent': 'South America'},
        {'name': 'Chile', 'continent': 'South America'},
        {'name': 'Colombia', 'continent': 'South America'},
        {'name': 'Ecuador', 'continent': 'South America'},
        {'name': 'Guyana', 'continent': 'South America'},
        {'name': 'Paraguay', 'continent': 'South America'},
        {'name': 'Peru', 'continent': 'South America'},
        {'name': 'Suriname', 'continent': 'South America'},
        {'name': 'Uruguay', 'continent': 'South America'},
        {'name': 'Venezuela', 'continent': 'South America'},
    ]

    locations = [
        {'name': 'Beijing', 'country': 'China', 'vibe': 'Romantic', 'setting': 'City', 'partner':'Solo', 'climate': 'Hot'},
        {'name': 'London', 'country': 'United Kingdom', 'vibe': 'Romantic', 'setting': 'City', 'partner':'Partner', 'climate': 'Mixed'},
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
        {'title': 'Vacation Post 1', 'text': 'This is the first post by user1.', 'author': 'user1', 'country': 'China', 'location': 'Beijing'},
        {'title': 'Vacation Post 2', 'text': 'This is the second post by user1.', 'author': 'user1', 'country': 'United Kingdom', 'location': 'London'},
        {'title': 'Vacation Post 3', 'text': 'This is the first post by user2.', 'author': 'user2', 'country': 'Japan', 'location': 'Tokyo'},
        {'title': 'Vacation Post 4', 'text': 'This is the second post by user2.', 'author': 'user2', 'country': 'Austria', 'location': 'Gmunden'},
        {'title': 'Vacation Post 5', 'text': 'This is the first post by user3.', 'author': 'user3', 'country': 'Canada', 'location': 'Toronto'},
        {'title': 'Vacation Post 6', 'text': 'This is the second post by user3.', 'author': 'user3', 'country': 'Switzerland', 'location': 'Geneva'},
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
                add_post(post['title'], post['text'], u, country, location)


def add_user(username, password, email):
    user = User.objects.get_or_create(username=username, email=email)[0]
    user.set_password(password)
    user.save()
    return user


def add_post(title, text, author, country, location):
    user = User.objects.get(username=author)
    post = VacationPost.objects.get_or_create(title=title, text=text, author=user, country=country, location=location)[0]
    post.likes = random.randint(0, 60)
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
    print('TripTales population script complete. Objects in database:')
    print('- Countries:', Country.objects.count())
    print('- Locations:', Location.objects.count())
    print('- Users:', User.objects.count())
    print('- Profiles:', UserProfile.objects.count())
    print('- Posts:', VacationPost.objects.count())
    print('- Comments:', Comment.objects.count())


