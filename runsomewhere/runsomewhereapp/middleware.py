import logging

logger = logging.getLogger("user_events")


class RequestResponseLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        return response

    def process_request(self, request):
        logger.info(f"Request: {request.method} {request.get_full_path()}")
        logger.info(f'Client IP: {request.META.get("REMOTE_ADDR")}')
        logger.info(f'User Agent: {request.META.get("HTTP_USER_AGENT")}')
        logger.info(f'Referrer: {request.META.get("HTTP_REFERER", "No Referrer")}')

    def process_response(self, request, response):
        logger.info(f"Response Status: {response.status_code}")
        return response
