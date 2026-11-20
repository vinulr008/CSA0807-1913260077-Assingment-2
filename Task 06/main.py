from functools import lru_cache
import sys

calls = 0


def ways_naive(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_memo(n - 1) + ways_memo(n - 2)


def ways_loop(n):
    if n <= 1:
        return 1

    previous, current = 1, 1

    for _ in range(2, n + 1):
        previous, current = current, previous + current

    return current


print("Ways from 1 to 6:")

for n in range(1, 7):
    ways_memo.cache_clear()
    print(n, ways_memo(n))


calls = 0
print("Naive:", ways_naive(25), "calls =", calls)

ways_memo.cache_clear()
calls = 0
print("Memo:", ways_memo(25), "calls =", calls)


for n in (10, 20, 25, 30):
    calls = 0
    ways_naive(n)
    naive_calls = calls

    ways_memo.cache_clear()
    calls = 0
    ways_memo(n)
    memo_calls = calls

    print(n, naive_calls, memo_calls)


print("Recursion limit:", sys.getrecursionlimit())

ways_memo.cache_clear()

try:
    print("Memoised result for 1000:", ways_memo(1000))
except RecursionError:
    print("RecursionError")

print("Loop result for 1000:", ways_loop(1000))
