def normalise(text):
    return text.strip().replace(" ", "").replace("-", "").upper()


def is_valid(reg):
    if len(reg) not in (9, 10):
        return False

    if not reg[:2].isalpha():
        return False

    if not reg[2:4].isdigit():
        return False

    series_length = len(reg) - 8

    if not reg[4:4 + series_length].isalpha():
        return False

    if not reg[4 + series_length:].isdigit():
        return False

    return True


def format_registration(reg):
    if not is_valid(reg):
        return "Invalid registration number"

    series_length = len(reg) - 8

    state = reg[:2]
    district = reg[2:4]
    series = reg[4:4 + series_length]
    number = reg[4 + series_length:]

    return f"{state} {district} {series} {number}"


test_numbers = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB"
]

for raw in test_numbers:
    reg = normalise(raw)
    result = "valid" if is_valid(reg) else "INVALID"
    print(f"{raw:18} -> {reg:11} {result}")

print(format_registration(normalise("tn 09 ab 1234")))
