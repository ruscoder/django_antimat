# -*- coding: utf8 -*-
from django import forms
from .models import Mat
from django.forms.widgets import Textarea


class MatForm(forms.ModelForm):
    word = forms.CharField(widget=Textarea, help_text='Each word on new line')

    def save(self, commit=True):
        words = self.cleaned_data['word'].split('\n')
        # If Update - set only last word
        # And this truck for add by super save
        # 50 - is max length
        self.instance.word = words.pop()[:50]
        # If create - add remaining words
        if self.instance.pk is None:
            for word in words:
                self.Meta.model.objects.create(word=word[:50])

        return super(MatForm, self).save(commit=commit)

    class Meta:
        model = Mat
        exclude = ('word', )