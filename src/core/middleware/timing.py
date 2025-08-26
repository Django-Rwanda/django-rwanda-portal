import time
from django.utils.deprecation import MiddlewareMixin

class TimingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()
    def process_response(self, request, response):
        duration = time.time() - getattr(request, "start_time", time.time())
        response["X-Response-Time"] = f"{duration:.3f}s"
        return response