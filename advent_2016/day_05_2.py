from day_05_1 import get_hash_with_5_zeros


def calculate_password_dict(input_string):
    index = -1
    digits = {}
    while len(digits) < 8:
        hex_digest, index = get_hash_with_5_zeros(input_string, index)
        if hex_digest[5] in ['1', '2', '3', '4', '5', '6', '7', '0'] and not digits.get(int(hex_digest[5])):
            digits[int(hex_digest[5])] = hex_digest[6]

    return digits


if __name__ == '__main__':
    print calculate_password_dict('ugkcyxxp')
