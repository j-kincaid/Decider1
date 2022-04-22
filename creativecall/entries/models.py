from django.db import models
from django.utils import timezone

# Create your models here.

class Artwork():
    title = models.CharField(max_length=200)
    artist_text = models.CharField(max_length=200)
    panelist_text = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    # int
    height = models.IntegerField(max_length=30)
    # int
    width = models.IntegerField(default=0)
    # int
    depth = models.IntegerField(max_length=30)
    media = models.CharField(max_length=200)
    year_completed = models.DateTimeField('')


class Artist():
    artist_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    full_name = models.CharField(max_length=200)
    pronouns = models.CharField(max_length=30)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    # int
    zip = models.IntegerField(max_length=30)
    # unique
    email = models.CharField(max_length=30)
    bio = models.CharField(max_length=300)
    # unique
    username = models.CharField(max_length=30)
    # unique
    password = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)


class Panelist():
    panelist_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    full_name = models.CharField(max_length=200)
    pronouns = models.CharField(max_length=30)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    # int
    zip = models.IntegerField(max_length=30)
    # unique
    email = models.CharField(max_length=30)
    bio = models.CharField(max_length=300)
    # unique
    username = models.CharField(max_length=30)
    # unique
    password = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)


class Criteria(models.Model):
    criteria_text = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.TextField(max_length=200, null=True)
    def __str__(self):
        return self.criteria_text

class Choice(models.Model):
    criteria = models.CharField(max_length=200, null=True)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.choice_text