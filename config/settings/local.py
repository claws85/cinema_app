from .base import *


DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


########## LOCAL DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cinema_app',
        'USERNAME':'chris',
        'PASSWORD':'',
        'PORT':'3306',
        'HOST': 'localhost',
    }
}
########## END LOCAL DATABASE CONFIGURATION

INSTALLED_APPS += ('debug_toolbar', )

