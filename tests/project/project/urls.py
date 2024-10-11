from django.contrib import admin
from django.urls import path, include

from tests.project.project.settings import LOGUI_URL_PREFIX

urlpatterns = [
    path('admin/', admin.site.urls),
    path(LOGUI_URL_PREFIX, include('logui.routes.views')),
]
