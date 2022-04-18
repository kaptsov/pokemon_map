from django.db import models


class Pokemon(models.Model):

    name = models.TextField(verbose_name='Имя покемона')
    picture = models.ImageField(verbose_name='Картинка', upload_to='pokemon_images', blank=True, null=True)
    title_en = models.CharField(verbose_name='Название (англ)', max_length=200, blank=True)
    title_jp = models.CharField(verbose_name='Название (яп)', max_length=200, blank=True)
    description = models.TextField(verbose_name='Описание', default='No description yet', blank=True)
    previous_evolution = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='next_evolution',
        verbose_name='Из кого эволюционировал'
    )

    def __str__(self):
        return self.name


class PokemonEntity(models.Model):

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Появился в ', default=None, null=True, blank=True)
    dissappeared_at = models.DateTimeField(verbose_name = 'Исчез в ', default=None, null=True, blank=True)
    level = models.SmallIntegerField(verbose_name = 'Уровень', null=True, blank=True)
    health = models.SmallIntegerField(verbose_name = 'Здоровье', blank=True, null=True)
    strength = models.SmallIntegerField(verbose_name = 'Сила', blank=True, null=True)
    defense = models.SmallIntegerField(verbose_name = 'Защита', blank=True, null=True)
    stamina = models.SmallIntegerField(verbose_name = 'Выносливость', blank=True, null=True)

    def __str__(self):
        return f'{self.pokemon} - {self.level}'

