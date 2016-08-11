# -*- coding: utf-8 -*-


class AntimatDescriptor(object):
    def __init__(self, field):
        self.field = field

        self.orig_attr_name = '__orig_' + field.name

    def __get__(self, instance, cls=None):
        # That was fun, wasn't it?
        text = instance.__dict__[self.field.name]
        return text

    def __set__(self, instance, value):
        from .core import Antimat
        orig_text = instance.__dict__.get(self.orig_attr_name)
        if orig_text != value:
            instance.__dict__[self.orig_attr_name] = value
            value = Antimat.replace_badwords(value)
        instance.__dict__[self.field.name] = value
