"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+3h4b6-doee-tdw(xlpb$9ya-w9nu@0ynsialksz)y+rz$a_nh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'cafe.apps.CafeConfig',
    'github_oauth.apps.GithubOauthConfig',
    'google_oauth.apps.GoogleOauthConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#Google Oauth Section
GOOGLE_CLIENT_ID = '887751516891-mmmeu1utsfnhaeg2lgelsfc83s7n2jjc.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET_PASSWORD = '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'
GOOGLE_TOKEN_API = 'https://oauth2.googleapis.com/token'
GOOGLE_ENDPOINT = 'https://accounts.google.com/o/oauth2/v2/auth' #인증서버
GOOGLE_SCOPE = 'https://www.googleapis.com/auth/userinfo.email ' + 'https://www.googleapis.com/auth/userinfo.profile ' + 'openid'
GOOGLE_REDIRECT_URI = 'http://127.0.0.1:8000/cafe/login/google/callback'

#Github Oauth Section
GITHUB_CLIENT_ID = 'c59828e0ab3892454f14'
GITHUB_CLIENT_SECRET_PASSWORD = '1e7c13eb0b7808b242be5bcb1386a3fdacf457cd'
GITHUB_TOKEN_API = 'https://github.com/login/oauth/access_token'
GITHUB_ENDPOINT = 'https://github.com/login/oauth/authorize'
GITHUB_SCOPE = 'repo'
GITHUB_REDIRECT_URI = 'http://localhost:8000/cafe/login/github/callback'