# django-antimat


# Requirements:

* Django>=1.4
* pymorphy2 
* pymorphy2-dicts-ru

# Install

Add to installed apps in settings `django_antimat`
   
```shell
./manage migrate django_antimat
```

Initialize with, as example:
```python
from django.db import models

from django_antimat import Antimat

class TestAntimat(models.Model):
    text = models.TextField()

Antimat.install(TestAntimat, 'text')
```

Get mat list from internet
And add this list in admin panel:
each word on new line


# Contributors

* Vadim <rusmiligamer@gmail.com>
* Apkawa <apkawa@gmail.com>

