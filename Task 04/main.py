import time


def build_plus(parts):
    text = ""

    for part in parts:
        text += part + ";"

    return text


def build_join(parts):
    return ";".join(parts) + ";"


def build_fstring(parts):
    return "".join(f"{part};" for part in parts)


def measure(parts, repeats=3):
    plus_times = []
    join_times = []
    fstring_times = []

    for _ in range(repeats):
        start = time.perf_counter()
        a = build_plus(parts)
        plus_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        b = build_join(parts)
        join_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        c = build_fstring(parts)
        fstring_times.append(time.perf_counter() - start)

        assert a == b == c

    return (
        sum(plus_times) / repeats,
        sum(join_times) / repeats,
        sum(fstring_times) / repeats,
        len(a)
    )


for size in (1000, 10000, 200000):
    items = [f"Item{i}:Rs{i % 50}" for i in range(size)]

    plus_avg, join_avg, fstring_avg, length = measure(items)

    print("\nNumber of lines:", size)
    print("Same text:", build_plus(items) == build_join(items))
    print("Length:", length)
    print(f"Average += time: {plus_avg:.6f} seconds")
    print(f"Average join time: {join_avg:.6f} seconds")
    print(f"Average f-string time: {fstring_avg:.6f} seconds")
