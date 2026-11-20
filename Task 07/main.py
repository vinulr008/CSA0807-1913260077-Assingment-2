from functools import lru_cache
import time

naive_calls = 0
memo_calls = 0


def original_ways(n):
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return 1

    return original_ways(n - 1) + original_ways(n - 2)


@lru_cache(maxsize=None)
def redesigned_ways(n):
    global memo_calls
    memo_calls += 1

    if n <= 1:
        return 1

    return redesigned_ways(n - 1) + redesigned_ways(n - 2)


def compare(n):
    global naive_calls, memo_calls

    naive_calls = 0

    start = time.perf_counter()
    original_result = original_ways(n)
    original_time = time.perf_counter() - start

    original_count = naive_calls

    redesigned_ways.cache_clear()
    memo_calls = 0

    start = time.perf_counter()
    redesigned_result = redesigned_ways(n)
    redesigned_time = time.perf_counter() - start

    redesigned_count = memo_calls

    print("\nInput:", n)
    print("Original result:", original_result)
    print("Redesigned result:", redesigned_result)
    print("Results equal:", original_result == redesigned_result)
    print("Original calls:", original_count)
    print("Redesigned calls:", redesigned_count)
    print(f"Original time: {original_time:.8f} seconds")
    print(f"Redesigned time: {redesigned_time:.8f} seconds")


for value in (10, 20, 25, 30):
    compare(value)
