from django.db import models

class Idea(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField()
    text = models.TextField()
    
    def __str__(self):
        return self.title
