def subsidy_separate(units, ration_card, senior):
    results = []

    if units <= 100:
        results.append("Full subsidy")

    if 101 <= units <= 200 and ration_card:
        results.append("Partial subsidy")

    if units > 200 and senior:
        results.append("Special subsidy")

    if not results:
        results.append("No subsidy")

    return results


def subsidy_elif(units, ration_card, senior):
    if units <= 100:
        return "Full subsidy"
    elif 101 <= units <= 200:
        if ration_card:
            return "Partial subsidy"
        else:
            return "No subsidy"
    elif units > 200:
        if senior:
            return "Special subsidy"
        else:
            return "No subsidy"


households = [
    (100, False, False),
    (101, True, False),
    (101, False, False),
    (150, True, False),
    (200, True, False),
    (201, False, False),
    (250, False, True),
    (250, True, False)
]

for units, ration, senior in households:
    print(units, ration, senior,
          subsidy_separate(units, ration, senior),
          subsidy_elif(units, ration, senior))
