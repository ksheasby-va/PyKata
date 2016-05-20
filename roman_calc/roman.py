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
    elif character == 'C':
        return 100
    elif character == 'D':
        return 500
    elif character == 'M':
        return 1000
    else:
        raise NotImplementedError()


def add(numeral1, numeral2):
    x = parse_numeral(numeral1)
    y = parse_numeral(numeral2)
    total = x + y

    return total


def reconstruct_numeral(numeral1, numeral2):
    number = add(numeral1, numeral2)
    M_count = number / 1000
    D_count = (number - (M_count * 1000)) / 500
    C_count = (number - (D_count * 500) - (M_count * 1000)) / 100
    L_count = (number - (C_count * 100) - (D_count * 500) - (M_count * 1000)) / 50
    X_count = (number - (L_count * 50) - (C_count * 100) - (D_count * 500) - (M_count * 1000)) / 10
    V_count = (number - (X_count * 10) - (L_count * 50) - (C_count * 100) - (D_count * 500) - (M_count * 1000)) / 5
    I_count = (number - (V_count * 5) - (X_count * 10) - (L_count * 50) - (C_count * 100) - (D_count * 500) - (M_count * 1000)) / 1

    numeral = 'M' * M_count
    if number % 1000 >= 900:
        numeral += 'CM'
        D_count = 0
        C_count = 0
    elif number % 500 >= 400:
        numeral += 'CD'
        C_count = 0
    numeral += 'D' * D_count
    numeral += 'C' * C_count
    numeral += 'L' * L_count
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
