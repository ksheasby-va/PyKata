import re


def is_abba_set(input_string):
    first_half = input_string[:2]
    second_half = input_string[2:]
    second_half_reversed = second_half[1] + second_half[0]
    return first_half == second_half_reversed


def find_abba_strings(input_string):
    count = 0
    for i in xrange(len(input_string) - 4):
        if is_abba_set(input_string[i:i+4]):
            count += 1
    return count


def cut_string(input_string):
    hypernet_sequences = re.findall(r"\[\w*\]", input_string)
    other_pieces = re.findall(r"(\w+\[|\]\w+)", input_string)
    cleaned_others = []
    for item in other_pieces:
        cleaned_others.append(item.strip('[]'))
    return hypernet_sequences + cleaned_others
