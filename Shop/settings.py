"""
Django settings for Shop project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3(9ny*q9mym@=hgkrw&o=apu%0+!l2m!w@bfjwx8063abacav8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['futuretech.powerpooll.space', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'Products.apps.SuitConfig',
    'django.contrib.admin', #Админка
    'django.contrib.auth', #Вход
    'django.contrib.contenttypes',
    'django.contrib.sessions', #Приложение сессий(проверка входа пользователя)
    'django.contrib.messages', #Сообщения (ИЗУЧИТЬ ВОПРОС!)
    'django.contrib.staticfiles', #Приложение статики
    'Products.apps.ProductsConfig', #Приложение продуктов
    'Orders', #Приложение заказов
    'MainApp', #Приложение Home-страницы
    'ShopApp', #Приложение страницы магазина
    'django_summernote', #Тектовый редактор
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

ROOT_URLCONF = 'Shop.urls' #Основной урл куда приходит реквест

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Orders.context_processors.getting_basket_info',
            ],
        },
    },
] #Подрубаем папку с темплейтами(HTML)

WSGI_APPLICATION = 'Shop.wsgi.application' #Проверка чего то там (ИЗУЧИТЬ!)


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ShopDB',
        'USER': 'ShopAdmin',
        'PASSWORD': '35653565Nick',
        'HOST': 'localhost',
        'PORT': '5432',
    }
} #Подрубаем базу данных. Инфа по этой теме в хелпере(юзается Postgesql)



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
] #Изучить!


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us' #Язык сайта, админка реагирует на это

TIME_ZONE = 'UTC' #Смена часового пояса

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/staticfiles/' #Путь до папки со статикой(из основной директории)

STATICFILES_DIRS = [(
  os.path.join(BASE_DIR, "staticfiles")
)] #Остальные папки со статикой(инфа берется из первого аргумента, в данном случае из корневого каталога)

MEDIA_URL = '/media/' #Папка с медиафайлами(загружаемые на сайт картинки и пр.)

MEDIA_ROOT = os.path.join(BASE_DIR, "staticfiles", "media") #Остальные папки с медиафайлами(инфа берется из первого аргумента, в данном случае из корневого каталога)
