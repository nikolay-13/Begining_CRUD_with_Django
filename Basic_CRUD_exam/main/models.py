from django.db import models


class Profile(models.Model):
    USER_NAME_MAX_LENGTH = 15
    username = models.CharField(
        max_length=USER_NAME_MAX_LENGTH,

    )
    email = models.EmailField()
    age = models.IntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    ALBUM_NAME_MAX_LENGTH = 30
    ARTIST_NAME_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30
    album_name = models.CharField(unique=True,
                                  max_length=ALBUM_NAME_MAX_LENGTH,
                                  )
    artist = models.CharField(
        max_length=ARTIST_NAME_MAX_LENGTH,
    )
    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField()
    price = models.FloatField()
