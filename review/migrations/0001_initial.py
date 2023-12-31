# Generated by Django 3.2.22 on 2023-10-22 19:49

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('genre', models.CharField(blank=True, choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Arcade', 'Arcade'), ('Beat Em Up', 'Beat Em Up'), ('Ego-Shooter', 'Ego-Shooter'), ('Platformer', 'Platformer'), ('Racing', 'Racing'), ('RPG', 'RPG'), ('Simulation', 'Simulation'), ('Sports', 'Sports'), ('Strategy', 'Strategy'), ('Puzzle', 'Puzzle'), ('Horror', 'Horror')], max_length=100)),
                ('year', models.IntegerField(blank=True, choices=[(1980, '1980'), (1981, '1981'), (1982, '1982'), (1983, '1983'), (1984, '1984'), (1985, '1985'), (1986, '1986'), (1987, '1987'), (1988, '1988'), (1989, '1989'), (1990, '1990'), (1991, '1991'), (1992, '1992'), (1993, '1993'), (1994, '1994'), (1995, '1995'), (1996, '1996'), (1997, '1997'), (1998, '1998'), (1999, '1999'), (2000, '2000'), (2001, '2001'), (2002, '2002'), (2003, '2003'), (2004, '2004'), (2005, '2005'), (2006, '2006'), (2007, '2007'), (2008, '2008')])),
                ('platform', models.CharField(blank=True, choices=[('Dreamcast', 'Dreamcast'), ('Gameboy', 'Gameboy'), ('Gameboy Color', 'Gameboy Color'), ('NES', 'NES'), ('N64', 'N64'), ('PC', 'PC'), ('PlayStation', 'PlayStation'), ('PlayStation 2', 'PlayStation 2'), ('Sega Genesis', 'Sega Genesis'), ('SNES', 'SNES'), ('XBOX', 'XBOX')], max_length=100)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['-rating'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('title', models.CharField(blank=True, max_length=200, unique=True)),
                ('slug', models.SlugField(default='', max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('excerpt', models.TextField(blank=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('rating', models.DecimalField(choices=[(0, '0.0 Stars'), (0.5, '0.5 Stars'), (1, '1.0 Stars'), (1.5, '1.5 Stars'), (2, '2.0 Stars'), (2.5, '2.5 Stars'), (3, '3.0 Stars'), (3.5, '3.5 Stars'), (4, '4.0 Stars'), (4.5, '4.5 Stars'), (5, '5.0 Stars')], decimal_places=1, max_digits=2)),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.game')),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
