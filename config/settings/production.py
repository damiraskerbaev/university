from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'universityprojec$default',
        'USER': 'universityprojec',
        'PASSWORD': 'DaMiR2810',
        'HOST': 'universityprojectapi.mysql.pythonanywhere-services.com'
    }
}