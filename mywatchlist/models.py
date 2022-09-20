from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=250)
    rating = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    release_date = models.DateField()
    review = models.TextField()