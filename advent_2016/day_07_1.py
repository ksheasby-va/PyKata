import re


def is_abba_set(input_string):
    if input_string[0] == input_string[1]:
        return False
    first_half = input_string[:2]
    second_half = input_string[2:]
    second_half_reversed = second_half[1] + second_half[0]
    return first_half == second_half_reversed


def find_abba_strings(input_string):
    for i in xrange(len(input_string) - 3):
        if is_abba_set(input_string[i:i+4]):
            return True
    return False


def cut_string(input_string):
    hypernet_sequences = re.findall(r"\[\w*\]", input_string)
    other_pieces = re.findall(r"(\w+\[|\]\w+)", input_string)
    cleaned_others = []
    for item in other_pieces:
        cleaned_others.append(item.strip('[]'))
    return hypernet_sequences + cleaned_others


def supports_tls(input_data):
    count = 0
    for ip in input_data.splitlines():
        found_valid_ip = False
        sliced_ip = cut_string(ip)
        for item in sliced_ip:
            if item.startswith('['):
                if find_abba_strings(item.strip('[]')):
                    break
            else:
                if find_abba_strings(item):
                    found_valid_ip = True
        if found_valid_ip:
            count += 1
    return count



