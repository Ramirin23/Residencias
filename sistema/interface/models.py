# En tu archivo models.py

from django.db import models


class Narrativa(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, verbose_name='description')
