from django.db import models

from django_antimat import Antimat


class TestAntimat(models.Model):
    text = models.TextField(null=True)


Antimat.install(TestAntimat, 'text')
