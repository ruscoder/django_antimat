# -*- coding: utf8 -*-
from django.contrib import admin

from .models import Mat
from .forms import MatForm


class MatAdmin(admin.ModelAdmin):
    form = MatForm
    fields = ['word']
    list_display = ['word', 'word_normalized']


admin.site.register(Mat, MatAdmin)
