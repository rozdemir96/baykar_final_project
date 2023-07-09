from django.db import models
from django.contrib.auth.models import User

class Ihas(models.Model):
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    agirlik = models.FloatField()
    kategori = models.CharField(max_length=50)

    class Meta:
        db_table = 'ihas'

