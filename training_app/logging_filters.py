import logging
import threading

_thread_locals = threading.local()

def get_current_user():
    return getattr(_thread_locals, 'user', None)

class UsernameFilter(logging.Filter):
    def filter(self, record):
        user = get_current_user()
        record.username = user.username if user and user.is_authenticated else 'Anonymous'
        return True
