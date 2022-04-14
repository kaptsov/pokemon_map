from django.db import models

class Pokemon(models.Model):
    name = models.TextField()
    picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

class PokemonEntity(models.Model):

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f'{self.latitude} - {self.longitude}'