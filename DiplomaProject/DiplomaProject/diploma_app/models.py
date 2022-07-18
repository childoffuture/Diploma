from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    subscribers = models.ManyToManyField(User, through="Subscription")

    def __str__(self):
        return self.name

    @property
    def is_subscribed(self):
        return Subscription.objects.filter(id_category=self.pk).exists()


class Video(models.Model):
    name = models.CharField(max_length=128, unique=True)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    #video data


class HashTag(models.Model):
    name = models.CharField(max_length=128, unique=True)
    id_video = models.ForeignKey(Video, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    id_video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Subscription(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Chat(models.Model):
    id_video_author = models.ForeignKey(User, on_delete=models.CASCADE)
    id_commentator = models.ForeignKey(User, on_delete=models.CASCADE)


class ChatMessage(models.Model):
    id_author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
