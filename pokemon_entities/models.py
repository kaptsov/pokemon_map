from django.db import models

class Pokemon(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name