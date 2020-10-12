from django.db import models

# Create your models here.
class Word(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    part_of_speech = models.TextField(default='')
    definition = models.TextField()
    example = models.TextField(default='')
    
    def __str__(self):
        return self.name