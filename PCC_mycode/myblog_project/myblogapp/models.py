from django.db import models

class BlogPost(models.Model):
    """This is a blog entry."""
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)

def __str__(self):
    """Return a string representation of the model."""
    return self.text