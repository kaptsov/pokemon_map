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
    appeared_at =  models.DateTimeField(blank=True, null=True)
    dissappeared_at = models.DateTimeField(blank=True, null=True)
    level = models.SmallIntegerField(blank=True)
    health = models.SmallIntegerField(blank=True)
    strength = models.SmallIntegerField(blank=True)
    defense = models.SmallIntegerField(blank=True)
    stamina = models.SmallIntegerField(blank=True)

    def __str__(self):
        return f'{self.latitude} - {self.longitude}'

