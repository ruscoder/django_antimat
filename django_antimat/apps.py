from django.core.exceptions import AppRegistryNotReady

try:
    from django.apps import AppConfig
except ImportError:
    # Early Django versions import everything in test, avoid the failure due to
    # AppConfig only existing in 1.7+
    AppConfig = object

from django.conf import settings


class AntimatConfig(AppConfig):
    name = 'django_antimat'
    label = 'django_antimat'

    def ready(self):
        morphy_dict_path = getattr(settings, 'MORPHY_DICT_PATH', None)
        if not morphy_dict_path:
            raise AppRegistryNotReady('Do not set settings MORPHY_DICT_PATH')
        from .models import Normalizer
        Normalizer.init(path=morphy_dict_path)
