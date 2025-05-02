# utils.py
import time
from functools import wraps
from django.db import DatabaseError

def retry_operation(max_retries=3, delay=2, exponential_backoff=False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            current_delay = delay
            while retries < max_retries:
                try:
                    print(f"Intento #{retries + 1}")  # Verifica si entra
                    return func(*args, **kwargs)
                except DatabaseError as e:
                    retries += 1
                    if retries >= max_retries:
                        print("Máximo número de reintentos alcanzado")
                        raise e
                    print(f"Error detectado: {e}. Reintentando en {current_delay} segundos...")
                    time.sleep(current_delay)
                    if exponential_backoff:
                        current_delay *= 2
        return wrapper
    return decorator