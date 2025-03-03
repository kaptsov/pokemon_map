# Generated by Django 3.1.14 on 2022-04-18 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to='pokemon_images')),
                ('title_en', models.CharField(blank=True, max_length=200)),
                ('title_jp', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True, default='No description yet')),
                ('next_evolution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('appeared_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('dissappeared_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('level', models.SmallIntegerField(blank=True, null=True)),
                ('health', models.SmallIntegerField(blank=True, null=True)),
                ('strength', models.SmallIntegerField(blank=True, null=True)),
                ('defense', models.SmallIntegerField(blank=True, null=True)),
                ('stamina', models.SmallIntegerField(blank=True, null=True)),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon')),
            ],
        ),
    ]
