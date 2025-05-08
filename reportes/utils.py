# utils.py
import time
from functools import wraps
from django.db import DatabaseError

def retry_operation(max_retries=5, delay=2, exponential_backoff=False): #maximos intentos 5, espera 2 segundos entre intentos, y si se activa el backoff exponencial, la espera se duplica en cada intento fallido.
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs): #reintento, se ejecuta la uncion y si falla se vuelve a ejecutar
            retries = 0
            current_delay = delay
            while retries < max_retries:
                try:
                    print(f"Intento #{retries + 1}")  # Verifica si lo lorgra
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