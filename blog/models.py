from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    """The Model for my Blog Post"""

    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
        
        
        


        
