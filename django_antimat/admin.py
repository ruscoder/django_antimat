# -*- coding: utf8 -*-
from models import Mat
from forms import MatForm
from django.contrib import admin


class MatAdmin(admin.ModelAdmin):
    form = MatForm
    fields = ['word']
    list_display = ['word', 'word_normalized']


admin.site.register(Mat, MatAdmin)
