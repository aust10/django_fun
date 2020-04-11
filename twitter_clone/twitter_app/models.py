from django.db import models
from django.urls import reverse
from django.db import models

from django.conf import settings


class Twitter(models.Model):
    title = models.CharField(max_length= 140)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    body_text = models.TextField()
    my_img = models.ImageField(upload_to='images/', default='images/default.png')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('twitter_app:detail', args=(self.id,)) 

    class Meta:
        ordering = ['-created_date']


class Tweet(models.Model):
    favorite = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='user_favorite')
