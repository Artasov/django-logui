from os.path import join
from pathlib import Path

from adjango.utils.common import is_celery

from logui.classes.logger import LoggingBuilder, Logger

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
ADJANGO_BACKENDS_APPS = BASE_DIR / 'apps'
ADJANGO_FRONTEND_APPS = BASE_DIR.parent / 'frontend' / 'src' / 'apps'
ADJANGO_APPS_PREPATH = 'apps.'
ADJANGO_EXCEPTION_REPORT_EMAIL = ('ivanhvalevskey@gmail.com',)
ADJANGO_EXCEPTION_REPORT_TEMPLATE = 'core/error_report.html'
ADJANGO_LOGGER_NAME = 'global'
ADJANGO_EMAIL_LOGGER_NAME = 'email'

# logui settings
LOGUI_LOGS_DIR = join(BASE_DIR, 'logs')
LOGUI_REQUEST_RESPONSE_LOGGER_NAME = 'global'
LOGUI_URL_PREFIX = 'logui/'
LOGUI_CONTROLLERS_SETTINGS = {
    'auth_required': True,
    'log_name': False,
    'not_auth_redirect': f'/admin/login/?next=/{LOGUI_URL_PREFIX}'
}
IS_CELERY = is_celery()
LOGGING = LoggingBuilder(
    logs_dir=LOGUI_LOGS_DIR,
    format='{levelname} {asctime}: {message}',
    datefmt='%d-%m %H:%M:%S',
    loggers=(
        Logger(name='tbank', include_in=['commerce', 'global']),
        Logger(name='prodamus', include_in=['commerce', 'global']),
        Logger(name='cloudpayments', include_in=['commerce', 'global']),
        Logger(name='bitrix', include_in=['global']),
        Logger(name='shopozz', include_in=['global']),
        Logger(name='email', include_in=['notify', 'global']),
        Logger(name='sms', include_in=['notify', 'global']),
        Logger(name='notify', include_in=['global']),
        Logger(name='conference', include_in=['global']),
        Logger(name='commerce', include_in=['global']),
        Logger(name='lhv2tbank', include_in=['global']),
        Logger(name='celery', level='INFO', include_in=['global']),
        Logger(name='global'),
    ) if not IS_CELERY else (Logger(name='cworker'),)
).build()
LoggingBuilder.check_loggers(LOGGING)

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
