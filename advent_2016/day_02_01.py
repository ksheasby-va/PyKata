from day_02_01_mapping import MAPPING


def get_next_number(directions):
    current = 5
    for item in directions:
        current = MAPPING[current][item]

    return current


def calculate_code(directions):
    code = []
    for direction in directions:
        code.append(get_next_number(direction))

    return code
