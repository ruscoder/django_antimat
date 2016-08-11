# -*- coding: utf8 -*-
from django.db import models
from django.db.models.signals import pre_save

from pymorphy.contrib import tokenizers
from pymorphy import get_morph

class Mat(models.Model):
    word = models.CharField(verbose_name=u'Word', max_length=50)
    word_normalized = models.CharField(verbose_name=u'Normalized word', max_length=50,
        blank=False, null=False, unique=True)

    def __unicode__(self):
        return self.word

    def save(self, **kwargs):
        word = self.word.strip().upper()
        self.word_normalized = Normalizer.get_normalized(word)
        if not Mat.objects.filter(word_normalized=self.word_normalized).exists():
            super(Mat, self).save(**kwargs)

    class Meta:
        verbose_name = u'Mat'
        verbose_name_plural = u'Mats'


class Normalizer(object):
    morph = None

    @classmethod
    def init(cls, path):
        cls.morph = get_morph(path)

    @classmethod
    def get_normalized(cls, word):
        word_normalized = cls.morph.normalize(word)
        # Get first word of set
        if isinstance(word_normalized, set):
            word_normalized = word_normalized.pop()
        return word_normalized


class Antimat(object):
    @classmethod
    def del_repeated_chars_from_word(cls, word):
        new_word = ''
        prev_char = ''
        for char in word:
            if char != prev_char:
                new_word += char
                prev_char = char
        return new_word

    @classmethod
    def mat_filter(cls, body):
        body = tokenizers.extract_tokens(body)

        for i in range(0, len(body)):
            word = body[i]
            if not word.isalpha():
                continue
            word = word.upper()
            word = cls.del_repeated_chars_from_word(word)
            word_normalized = Normalizer.get_normalized(word)
            if Mat.objects.filter(word_normalized=word_normalized).exists():
                body[i] = '*' * len(word)
        return ''.join(body)

    @classmethod
    def install(cls, model, field):
        def antimat_field(instance, **kwargs):
            field_value = getattr(instance, field)

            modified_field_value = cls.mat_filter(field_value)
            if field_value != modified_field_value:
                setattr(instance, field, modified_field_value)
                instance.save()

        pre_save.connect(receiver=antimat_field, sender=model, weak=False)
