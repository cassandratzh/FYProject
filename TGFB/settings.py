"""
Django settings for TGFB project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_&d^3812bt=q_h%b+4@)*rdv)xe313&@f#_f1k2m_*8jz&9j6m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    #'south',
    'cancer',
    'markdown_deux',
    'django_tables2',
    'csvimport',
    'django_commands',
    'embed_video',
    'dbbackup'
    #'django_social_share',
    #'javascript_settings'
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'TGFB.urls'

WSGI_APPLICATION = 'TGFB.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}


DATABASES = {
    'default': { 
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'smad2',                     
        'USER': 'root',
        'PASSWORD': '',
    }
}

TEMPLATE_DIRS = (
'/Users/cassandrateo/fyp/tgfb/templates',
)


TEMPLATE_CONTEXT_PROCESSORS = (
'django.core.context_processors.request',
'django.contrib.auth.context_processors.auth',
)




# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    ('assets', '/Users/cassandrateo/fyp/tgfb/static/'),

)

SITE_ID = 1



DBBACKUP_STORAGE = 'dbbackup.storage.filesystem_storage'

DBBACKUP_FILESYSTEM_DIRECTORY = '/Users/cassandrateo/fyp'






