from django.db import models
import uuid

class Music(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    name = models.CharField('Music Name', max_length=120)
    category = models.CharField('Category', max_length=120)
    description = models.TextField(blank=True)
    removed_for_representation = models.BooleanField(default=False)
