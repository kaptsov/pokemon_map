from django.db import models


class Pokemon(models.Model):

    name = models.TextField()
    picture = models.ImageField(upload_to='pokemon_images', blank=True, null=True)
    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)
    description = models.TextField(default='No description yet', blank=True)
    previous_evolution = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='next_evolution'
    )

    def __str__(self):
        return self.name


class PokemonEntity(models.Model):

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    appeared_at = models.DateTimeField(default=None, null=True, blank=True)
    dissappeared_at = models.DateTimeField(default=None, null=True, blank=True)
    level = models.SmallIntegerField(null=True, blank=True)
    health = models.SmallIntegerField(blank=True, null=True)
    strength = models.SmallIntegerField(blank=True, null=True)
    defense = models.SmallIntegerField(blank=True, null=True)
    stamina = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.pokemon} - {self.latitude} - {self.longitude}'

