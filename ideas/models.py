from django.db import models

import tagulous

class Idea(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField()
    text = models.TextField()
    tags = tagulous.models.TagField(
        force_lowercase=True,
        tree=True,
        verbose_name_singular = "tag",
    )
    
    def __str__(self):
        return self.title
