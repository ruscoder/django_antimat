# -*- coding: utf-8 -*-
from django.db.models import FileField
from django.db.models.signals import pre_save
from django.utils.encoding import smart_text

from pymorphy2 import MorphAnalyzer, tokenizers


class Normalizer(object):
    morph = MorphAnalyzer()

    @staticmethod
    def del_repeated_chars_from_word(word):
        new_word = ''
        prev_char = ''
        for char in word:
            if char != prev_char:
                new_word += char
                prev_char = char
        return new_word

    @staticmethod
    def tokenize(text):
        return tokenizers.simple_word_tokenize(text)

    @classmethod
    def normalize_word(cls, word):
        word = smart_text(word)
        word = word.upper()
        word = cls.del_repeated_chars_from_word(word)

        word_normalized = cls.morph.parse(word)[0].normal_form.upper()
        # Get first word of set
        if isinstance(word_normalized, set):
            word_normalized = word_normalized.pop()
        return word_normalized

    @classmethod
    def normalize_text(cls, text):
        text = smart_text(text)
        for word in cls.tokenize(text):
            if not word.isalpha():
                yield (word, None)
            yield (word, cls.normalize_word(word))


class Antimat(object):
    @staticmethod
    def collect_badwords(body):
        from django_antimat.models import Mat
        normalized_words = set(n for o, n in Normalizer.normalize_text(body))
        badwords = set(
            Mat.objects.filter(word_normalized__in=normalized_words).values_list('word_normalized', flat=True)
        )
        return normalized_words & badwords

    @staticmethod
    def has_exists_badwords(body):
        return bool(Antimat.collect_badwords(body))

    @staticmethod
    def replace_badwords(body):
        collected_badwords = Antimat.collect_badwords(body)

        new_body = []
        for (original, normalized) in Normalizer.normalize_text(body):
            if normalized in collected_badwords:
                original = '*' * len(original)
            new_body.append(original)
        return ' '.join(new_body)

    @classmethod
    def install(cls, model, field):
        from .fields import AntimatDescriptor
        setattr(model, field, AntimatDescriptor(model._meta.get_field(field)))
