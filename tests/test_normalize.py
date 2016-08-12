# -*- coding: utf-8 -*-
from unittest import TestCase

import types

from django_antimat.core import Normalizer


class NormalizerTestCase(TestCase):
    def test_initial(self):
        self.assert_(Normalizer.morph)

    def test_normalize_word(self):
        self.assertEqual(Normalizer.normalize_word(u'КоРовЫ'), u'КОРОВА')

    def test_normalize_text(self):
        word = u'КоРовЫ'
        n_word = u'КОРОВА'
        n_text = Normalizer.normalize_text(word)
        self.assert_(isinstance(n_text, types.GeneratorType))
        n_text = list(n_text)
        self.assertEqual(n_text, [(word, n_word)])
