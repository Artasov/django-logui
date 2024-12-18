# Django LogUi 

> Sometimes I use this in different projects, so I decided to put it on pypi

## Installation
```bash
pip install django-logui
```

## Settings

* ### Add the application to the project.
    ```python
    INSTALLED_APPS = [
        #...
        'adjango',
        'logui',
    ]
    ```
* ### In `settings.py` set the params
    ```python
    # settings.py
    from os.path import join
    from logui.utils import check_loggers
  
  
    # LOGS_DIR will be scanned for .log files
    # Nearest folders are also scanned.
    # LOGS_DIR *required
    LOGS_DIR = join(BASE_DIR, 'logs')

    LOGGING = ... # ur logging
    # Console report about existing loggers
    check_loggers(LOGGING)
    ```
    #### Read more about [adjango](https://github.com/Artasov/adjango)
* ### Add routes

    Only `is_staff` have access.
    ```python
    from django.urls import path, include
    # Not use django.conf.settings
    from logui.conf import LOGUI_URL_PREFIX

    urlpatterns = [
        ...
        path(LOGUI_URL_PREFIX, include('logui.routes.views')),
    ]
    ```
* ### Open https://localhost:8000/logui/
  `https:`//`localhost:8000`/`settings.LOGUI_URL_PREFIX`

* ### Additional
  ```python
  # only for request response middleware
  LOGUI_REQUEST_RESPONSE_LOGGER_NAME = 'global'
  MIDDLEWARE = [
    ...
    'adjango.middleware.IPAddressMiddleware',  # first IP middleware from adjango
    'logui.middleware.RequestResponseLoggerMiddleware',  # second logui middleware
    ...
  ]
  
  # not required
  LOGUI_URL_PREFIX = 'logui/'
  LOGUI_CONTROLLERS_SETTINGS = {
      'auth_required': True,
      'log_name': False,
      'not_auth_redirect': f'/admin/login/?next=/{LOGUI_URL_PREFIX}'
  }
  ```