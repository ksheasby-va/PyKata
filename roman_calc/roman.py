def parse_numeral(numeral):
    digits = [parse_digit(digit) for digit in numeral]
    total = 0
    i = 0
    for i in range(0, len(digits) - 1):
        current_digit = digits[i]
        next_digit = digits[i + 1]
        if current_digit < next_digit:
            total -= current_digit
        else:
            total += current_digit

    total += digits[-1]

    return total


def parse_digit(character):

    if character == 'I':
        return 1
    elif character == 'V':
        return 5
    elif character == 'X':
        return 10
    elif character == 'L':
        return 50
    else:
        raise NotImplementedError()

def add(numeral1, numeral2):
    x = parse_numeral(numeral1)
    y = parse_numeral(numeral2)
    total = x + y

    return total
