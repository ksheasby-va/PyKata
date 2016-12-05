import re
import string


def separate_parts(input_string):
    letters = []
    sector = ''
    checksum = ''
    all_parts = re.split('[-\[]', input_string)
    all_parts[-1] = '[' + all_parts[-1]
    for part in all_parts:
        if part[0].isdigit():
            sector = part
        elif part.startswith('['):
            checksum = part
        else:
            letters.append(part)
    return ''.join(letters), sector, checksum


def count_letters(input_string):
    all_letters = string.ascii_lowercase
    counts = {}
    for letter in all_letters:
        if input_string.count(letter):
            counts[letter] = input_string.count(letter)

    return counts


def get_five_most_frequent_letters(input_dict):
    """ 5 most frequent letters becomes the checksum """
    tuple_list = input_dict.items()
    tuple_list.sort(key=lambda tup: (-tup[1], tup[0]))
    return ''.join([i[0] for i in tuple_list[0:5]])
