from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='user_profile')
    phone_number = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    profile_image_path = models.CharField(max_length=200)

    def __str__(self):
        return "Profile for: " + str(self.user)


class Post(models.Model):
    author = models.ForeignKey(Profile,
                               on_delete=models.CASCADE,
                               related_name='author_posting')
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    like_count = models.IntegerField()
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(Profile,
                               on_delete=models.CASCADE,
                               related_name='author_comment')
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="posting_comment")
    content = models.TextField()
