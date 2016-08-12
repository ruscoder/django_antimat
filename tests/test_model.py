# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from unittest import TestCase

from django_antimat.models import Mat
from .models import TestAntimat


class ModelTestCase(TestCase):
    def setUp(self):
        self.test_text = 'Гуляла корова по полю'
        self.replaced_text = 'Гуляла ****** по полю'
        self.stop_word = Mat(word='коровы')
        self.stop_word.save()

    def test_replace_field_body(self):
        m = TestAntimat(text=self.test_text)
        self.assertEqual(m.text, self.replaced_text)
        m.text = self.test_text
        self.assertEqual(m.text, self.replaced_text)

    def test_create(self):
        m = TestAntimat.objects.create(text=self.test_text)
        self.assertEqual(m.text, self.replaced_text)
        m.text = self.test_text
        self.assertEqual(m.text, self.replaced_text)

    def test_null(self):
        for v in [None, False, True]:
            m = TestAntimat(text=v)
            self.assertEqual(m.text, v)
            m = TestAntimat.objects.create(text=v)
            self.assertEqual(m.text, v)
