import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'triptales_project.settings')

import django
django.setup() # This is necessary to then import the models
from django.contrib.auth.models import User
from triptales.models import VacationPost, Comment

def populate():
    users = [
        {'username': 'user1', 'password': 'qmwnebrv', 'email': 'user1@triptales.com'},
        {'username': 'user2', 'password': 'qmwnebrv', 'email': 'user2@triptales.com'},
        {'username': 'user3', 'password': 'qmwnebrv', 'email': 'user3@triptales.com'},
    ]

    vacation_posts = [
        {'text': 'This is the first post by user1.', 'author': 'user1'},
        {'text': 'This is the second post by user1.', 'author': 'user1'},
        {'text': 'This is the first post by user2.', 'author': 'user2'},
        {'text': 'This is the second post by user2.', 'author': 'user2'},
        {'text': 'This is the first post by user3.', 'author': 'user3'},
        {'text': 'This is the second post by user3.', 'author': 'user3'},
    ]

    # Create
    for user in users:
        add_user(user['username'], user['password'], user['email'])
    
    for post in vacation_posts:
        add_post(post['text'], post['author'])

def add_user(username, password, email):
    user = User.objects.get_or_create(username=username, email=email)[0]
    user.set_password(password)
    user.save()
    return user

def add_post(text, author):
    user = User.objects.get(username=author)
    post = VacationPost.objects.get_or_create(text=text, author=user)[0]
    return post

if __name__ == '__main__':
    print('Starting TripTales population script...')
    populate()