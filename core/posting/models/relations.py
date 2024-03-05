from django.db import models
from .user import User



class Relation(models.Model):
    follower = models.ForeignKey(User, related_name='follower_username', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followed_username', on_delete=models.CASCADE)
    since = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-since']

    def __str__(self):
        return self.follower.username
