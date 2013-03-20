from django.db import models


class Post(models.Model):
    """Represents a post in a user's feed.
    """
    post_id = models.CharField(max_length=255, unique=True, blank=False, null=False)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(null=True, blank=True)
    like_count = models.IntegerField(default=0)


class Comment(models.Model):
    """Represents a comment on a post.
    """
    comment_id = models.CharField(max_length=255, unique=True, blank=False, null=False)
    user_id = models.CharField(max_length=255)
    message = models.TextField(null=True, blank=True)
    like_count = models.IntegerField(default=0)
    user_likes = models.IntegerField(default=0)
    post = models.ForeignKey(Post)
