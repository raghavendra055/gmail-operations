def trace(logger):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logger.info(f"CALL → {func.__name__}")
            result = func(*args, **kwargs)
            logger.info(f"RETURN ← {func.__name__}")
            return result
        return wrapper
    return decorator
