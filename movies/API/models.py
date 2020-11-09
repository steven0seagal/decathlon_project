from django.db import models

# Create your models here.

class MovieData(models.Model):
    
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=128)
    year = models.CharField(max_length=128)
    rated = models.CharField(max_length=128)
    relased = models.CharField(max_length=128)
    runtime = models.CharField(max_length=128)
    genre = models.CharField(max_length=128)
    director = models.CharField(max_length=128)
    writer = models.CharField(max_length=512)
    actors = models.CharField(max_length=512) 
    plot = models.CharField(max_length=1024)
    language = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    awards = models.CharField(max_length=512)
    poster = models.CharField(max_length=128)
    metascore = models.CharField(max_length=128)
    imdbrating = models.CharField(max_length=128)
    imdbvotes = models.CharField(max_length=128)
    imdbID = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    dvd= models.CharField(max_length=128) 
    boxoffice = models.CharField(max_length=128)
    production = models.CharField(max_length=128)
    website = models.CharField(max_length=128)
    response= models.CharField(max_length=64)
    

class Rating(models.Model):
    source = models.CharField(max_length=128)
    value =  models.CharField(max_length=128)
    movie = models.ForeignKey(MovieData, on_delete=models.CASCADE, to_field='id', db_column='title')

class Comment(models.Model):
    comment = models.CharField(max_length=128)
    movie = models.ForeignKey(MovieData, on_delete=models.CASCADE, to_field='id', db_column='title')

