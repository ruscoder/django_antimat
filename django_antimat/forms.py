# -*- coding: utf8 -*-
from django import forms
from models import Mat
from django.forms.widgets import Textarea


class MatForm(forms.ModelForm):

    def save(self, commit=True):
        words = self.cleaned_data['word'].split('\n')
        # If Update - set only last word
        # And this truck for add by super save
        self.instance.word = words.pop()
        # If create - add remaining words
        if self.instance.pk is None:
            for word in words:
                self.Meta.model.objects.create(word=word)

        return super(MatForm, self).save(commit=commit)

    class Meta:
        model = Mat
        widgets = {
            'word': Textarea()
        }