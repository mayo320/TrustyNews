from django.db import models

# Create your models here.

class Message(models.Model):
    author = models.CharField(max_length = 200, default="Anonymous")
    content = models.CharField(max_length = 1000)

    def __str__(self):
        return self.author + ": " + self.content
