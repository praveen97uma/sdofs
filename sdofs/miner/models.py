from django.db import models

class Comment(models.Model):
    """Represents a comment on a post.
    """
    comment_id = models.CharField(max_length=255, unique=True, blank=False, null=False)
    user_id = models.CharField(max_length=255)
    message = models.TextField(null=True, blank=True)
    created_time = models.DateTimeField()


class Post(models.Model):
    """Represents a post in a user's feed.
    """
    post_id = models.CharField(max_length=255, unique=True, blank=False, null=False)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(null=True, blank=True)
    _type = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    likes = models.IntegerField(default=0)
