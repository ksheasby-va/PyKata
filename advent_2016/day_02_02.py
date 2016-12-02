from day_02_2_mapping import MAPPING


def get_next_number(directions, start):
    current = start
    for item in directions:
        current = MAPPING[current][item]

    return current


def calculate_code(directions):
    code = []
    start = 5
    for direction in directions:
        code.append(get_next_number(direction, start))
        start = code[-1] if code else 5

    return code
