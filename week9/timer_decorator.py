import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper


@timer
def slow_sum(n):
    return sum(range(n))


def main():
    print(slow_sum(1_000_000))


if __name__ == "__main__":
    main()
