# -*- coding: utf8 -*-
from __future__ import unicode_literals

from django.db import models

from django_antimat.core import Normalizer


class Mat(models.Model):
    word = models.CharField(verbose_name='Word', max_length=50)
    word_normalized = models.CharField(verbose_name='Normalized word', max_length=50,
                                       blank=False, null=False, unique=True,
                                       db_index=True)

    class Meta:
        verbose_name = 'Mat'
        verbose_name_plural = 'Mats'

    def __unicode__(self):
        return self.word

    def save(self, **kwargs):
        word = self.word.strip().upper()
        self.word_normalized = Normalizer.normalize_word(word)

        if not Mat.objects.filter(word_normalized=self.word_normalized).exists():
            super(Mat, self).save(**kwargs)
