from django.db import models
class Artist(models.Model):
    song = models.CharField(max_length=100)
    email = models.EmailField()
    lyrics = models.TextField()

    def __str__(self):
        return self.name
