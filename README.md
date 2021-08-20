# django-gnd

A python package to query and store data from [Lobid's GND-API](https://lobid.org/gnd)

## install

`pip install django-gnd`

add `gnd` to INSTALLED_APPS:

```python
#  project/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gnd',
    'example',
]
```

## features

see the example Project

### GND/LOBID autocomplete widget


