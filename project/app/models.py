from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=45, unique=True)
    capital = models.CharField(max_length=30, blank=True, null=True)
    region = models.CharField(max_length=15)
    subregion = models.CharField(max_length=30, blank=True, null=True)
    population = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name
