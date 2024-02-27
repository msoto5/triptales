from django.db import models
from django.contrib.auth.models import User

class VacationPost(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='post_images', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

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

    def __str__(self):
        return self.user.username
