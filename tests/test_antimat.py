# -*- coding: utf-8 -*-
from unittest import TestCase

from django_antimat.models import Mat
from django_antimat import Antimat


class AntimatTestCase(TestCase):
    def setUp(self):
        self.test_text = u'Гуляла корова по полю'
        self.replaced_text = u'Гуляла ****** по полю'
        self.stop_word = Mat(word='коровы')
        self.stop_word.save()

    def test_collect_badword(self):
        self.assertEqual(Antimat.collect_badwords(self.test_text), {u'КОРОВА'})

    def test_replace(self):
        self.assertEqual(Antimat.replace_badwords(self.test_text), self.replaced_text)

    def test_has_exists_badwords(self):
        self.assert_(Antimat.has_exists_badwords(self.test_text))
