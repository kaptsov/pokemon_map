from django.db import models


class PokemonElementType(models.Model):

    title = models.CharField(verbose_name='Стихия', max_length=200, blank=True)

    def __str__(self):
        return self.title


class Pokemon(models.Model):

    name = models.TextField(verbose_name='Имя покемона')
    picture = models.ImageField(verbose_name='Картинка', upload_to='pokemon_images', blank=True, null=True)
    title_en = models.CharField(verbose_name='Название (англ)', max_length=200, blank=True)
    title_jp = models.CharField(verbose_name='Название (яп)', max_length=200, blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    pokemon_element_type = models.ManyToManyField(
        PokemonElementType,
        related_name='element_types'
    )
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

    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name='entities',
        verbose_name='Вид покемона'
    )
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Появился в ', default=None, null=True, blank=True)
    dissappeared_at = models.DateTimeField(verbose_name='Исчез в ', default=None, null=True, blank=True)
    level = models.SmallIntegerField(verbose_name='Уровень', null=True, blank=True)
    health = models.SmallIntegerField(verbose_name='Здоровье', blank=True, null=True)
    strength = models.SmallIntegerField(verbose_name='Сила', blank=True, null=True)
    defense = models.SmallIntegerField(verbose_name='Защита', blank=True, null=True)
    stamina = models.SmallIntegerField(verbose_name='Выносливость', blank=True, null=True)

    def __str__(self):
        return f'{self.pokemon} - {self.level}'
