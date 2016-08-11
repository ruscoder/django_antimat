from django.db import models

from django_antimat.core import Antimat

class TestAntimat(models.Model):
    text = models.TextField()


Antimat.install(TestAntimat, 'text')


