from __future__ import annotations

from typing import Callable, Any
from app.extensions import cache


def cached_section(timeout: int = 300):
    def decorator(func: Callable[..., Any]):
        def wrapper(*args, **kwargs):
            key = f"section:{func.__name__}:{args}:{kwargs}"
            rv = cache.get(key)
            if rv is not None:
                return rv
            rv = func(*args, **kwargs)
            cache.set(key, rv, timeout=timeout)
            return rv
        return wrapper
    return decorator
