from time import perf_counter

from loguru import logger


def time_function(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        time_result = func(*args, **kwargs)
        end_time = perf_counter()
        total_time = end_time - start_time

        logger.info(f'Function {func.__name__} took {total_time:.4f} seconds')

        return time_result
    return wrapper
