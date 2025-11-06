import threading

_thread_locals = threading.local()

class ThreadLocalUserMiddleware:
    """Middleware to store the current request user in thread-local storage."""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _thread_locals.user = getattr(request, 'user', None)
        response = self.get_response(request)
        _thread_locals.user = None
        return response
