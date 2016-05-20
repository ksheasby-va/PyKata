def parse_numeral(numeral):
    digits = [parse_digit(digit) for digit in numeral]
    total = 0
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


def reconstruct_numeral(numeral1, numeral2):
    number = add(numeral1, numeral2)
    L_count = number / 50
    X_count = (number - (L_count * 50)) / 10
    V_count = (number - (X_count * 10) - (L_count * 50)) / 5
    I_count = (number - (V_count * 5) - (X_count * 10) - (L_count * 50)) / 1

    numeral = 'L' * L_count
    if number % 50 >= 40:
        numeral += 'XL'
        X_count = 0
    numeral += 'X' * X_count
    if number % 10 == 9:
        numeral += 'IX'
        V_count = 0
        I_count = 0
    numeral += 'V' * V_count
    if I_count == 4:
        numeral += 'IV'
    else:
        numeral += 'I' * I_count

    return numeral
