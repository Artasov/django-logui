from os.path import join
from pathlib import Path

from adjango.utils.common import is_celery

from logui.utils import check_loggers

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-@!c2^-9o^q#&te$c(u(k$l$cm^17p6p9e7cp1v8hnkdzg)a4^w'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'adjango',
    'logui',
]

# adjango settings
LOGIN_URL = '/login/'

# logui settings
LOGS_DIR = join(BASE_DIR, 'logs')
LOGUI_REQUEST_RESPONSE_LOGGER_NAME = 'global'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '{levelname} {asctime}: {message}',
            'datefmt': '%d-%m %H:%M:%S',
            'style': '{',
        },
        'request': {
            'format': '{levelname} {asctime}: {message} - {method} {url} {status}',
            'style': '{',
        },
    },
    'handlers': {
        'daily_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': join(LOGS_DIR, 'django.log'),
            'when': 'midnight',  # Ротация происходит в полночь
            'interval': 1,  # Интервал ротации — 1 день
            'backupCount': 356,  # Хранить логи за последний год
            'formatter': 'simple',
            'encoding': 'utf8',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        # 'django.request': {
        #     'handlers': ['daily_file', 'console'],
        #     'level': 'DEBUG',
        #     'formatter': 'request',  # Используем кастомный формат для запросов
        #     'propagate': False,
        # },
        'tbank': {
            'handlers': ['daily_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'stripe': {
            'handlers': ['daily_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'prodamus': {
            'handlers': ['daily_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'cloudpayments': {
            'handlers': ['daily_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'bitrix': {
            'handlers': ['daily_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'shopozz': {
            'handlers': ['daily_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'order': {
            'handlers': ['daily_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'conference': {
            'handlers': ['daily_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'sms': {
            'handlers': ['daily_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'email': {
            'handlers': ['daily_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'notify': {
            'handlers': ['daily_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'confirmation': {
            'handlers': ['daily_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'celery-worker': {
            'handlers': ['daily_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'social_auth': {
            'handlers': ['daily_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'consultation': {
            'handlers': ['daily_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'commerce': {
            'handlers': ['daily_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'reports': {
            'handlers': ['daily_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'global': {
            'handlers': ['daily_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # # Если используете другие логгеры для запросов, например, 'django.server', добавьте их сюда
        # 'django.server': {
        #     'handlers': [],
        #     'level': 'CRITICAL',
        #     'propagate': False,
        # },
    },
    # 'root': {  # Корневой логгер (опционально)
    #     'handlers': ['daily_file', 'console'],
    #     'level': 'INFO',
    # },
}
check_loggers(LOGGING)

MIDDLEWARE = [
    'adjango.middleware.IPAddressMiddleware',  # first IP middleware from adjango
    'logui.middleware.RequestResponseLoggerMiddleware',  # second logui middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
}}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
