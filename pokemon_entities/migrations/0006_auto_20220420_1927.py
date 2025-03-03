# Generated by Django 3.1.14 on 2022-04-20 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_auto_20220420_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='pokemon_element_type',
            field=models.ManyToManyField(to='pokemon_entities.PokemonElementType'),
        ),
        migrations.RemoveField(
            model_name='pokemonelementtype',
            name='title',
        ),
        migrations.AddField(
            model_name='pokemonelementtype',
            name='title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Стихия'),
        ),
    ]
