import logging

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

log = logging.getLogger(settings.LOGUI_REQUEST_RESPONSE_LOGGER_NAME)


class RequestResponseLoggerMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        super().__init__(get_response)
        self.get_response = get_response

    @staticmethod
    def process_request(request):
        if settings.LOGUI_URL_PREFIX not in request.path:
            log.info(f'{request.method} {request.path} {request.ip}')
        return None

    @staticmethod
    def process_response(request, response):
        if settings.LOGUI_URL_PREFIX not in request.path:
            log.info(f'Response {request.path}: {response.status_code}')
        return response
