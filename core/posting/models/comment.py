from .post import Post
from django.db import models


class Comment(models.Model):
    content = models.CharField(max_length=180, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-created_on']
