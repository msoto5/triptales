"""Models for the triptales app."""

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Country(models.Model):
    name = models.CharField(max_length=128, unique=True)
    posts = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    continent = models.CharField(max_length=10, choices=(("Europe", "Europe"),
                                                         ("Asia", "Asia"),
                                                         ("South America", "South America"),
                                                         ("North America", "North America"),
                                                         ("Africa", "Africa"),
                                                         ("Oceania", "Oceania"),
                                                         ("Antarctica", "Antarctica")))
    slug = models.SlugField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)


class Location(models.Model):
    name = models.CharField(max_length=128)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    posts = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=128, )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Location, self).save(*args, **kwargs)


class VacationPost(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='post_images', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f'Post by {self.author.username}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(VacationPost, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.user.username} commented on {self.post.id}: {self.text}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    bio = models.TextField(blank=True)

    saved_posts = models.ManyToManyField(VacationPost, blank=True,
                                         related_name='saved_by_users')
    liked_posts = models.ManyToManyField(VacationPost, blank=True,
                                         related_name='liked_by_users')

    posts_made = models.ManyToManyField(VacationPost, blank=True,
                                        related_name='posts_made')

    def __str__(self):
        return self.user.username

