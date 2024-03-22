"""Models for the triptales app."""

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from triptales_project.settings import PROFILE_IMG_DIR, POST_IMG_DIR
from django.utils import timezone


class Country(models.Model):
    name = models.CharField(max_length=128, unique=True)
    posts = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    continent = models.CharField(max_length=15, choices=(("Europe", "Europe"),
                                                         ("Asia", "Asia"),
                                                         ("South America", "South America"),
                                                         ("North America", "North America"),
                                                         ("Africa", "Africa"),
                                                         ("Oceania", "Oceania")))
    slug = models.SlugField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)


class Location(models.Model):
    name = models.CharField(max_length=128)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default = 0)
    posts = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    vibe = models.CharField(default='', max_length=128, choices=(("Party", "Party"),
                                                                 ("Adventure", "Adventure"),
                                                                 ("Romantic", "Romantic"),
                                                                 ("Relaxed", "Relaxed")))
    setting = models.CharField(default='',max_length=128, choices=(("City", "City"),
                                                        ("Beach", "Beach"),
                                                        ("Mountains", "Mountains"),
                                                        ("Countryside", "Countryside")))
    travelPartners = models.CharField(default='',max_length=128, choices=(("Family", "Family"),
                                                               ("Friends", "Friends"),
                                                               ("Partner", "Partner"),
                                                               ("Solo", "Solo")))
    climate = models.CharField(default='',max_length=128, choices=(("Hot", "Hot"),
                                                        ("Cold", "Cold"),
                                                        ("Mixed", "Mixed")))

    slug = models.SlugField(max_length=128)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Location, self).save(*args, **kwargs)


class VacationPost(models.Model):
    TITLE_MAX_LENGTH = 128
    title = models.CharField(max_length=TITLE_MAX_LENGTH,
                             default='Trip to ' + str(Location.name) + ', ' + str(Country.name))
    text = models.TextField()
    image = models.ImageField(upload_to=POST_IMG_DIR, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title} by {self.author.username}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(VacationPost, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.user.username} commented on {self.post.id}: {self.text}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=PROFILE_IMG_DIR, blank=True)
    bio = models.TextField(blank=True)

    saved_posts = models.ManyToManyField(VacationPost, blank=True,
                                         related_name='saved_by_users')
    liked_posts = models.ManyToManyField(VacationPost, blank=True,
                                         related_name='liked_by_users')

    posts_made = models.ManyToManyField(VacationPost, blank=True,
                                        related_name='posts_made')

    def __str__(self):
        return self.user.username
