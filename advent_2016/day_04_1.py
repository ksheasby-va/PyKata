import re


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
    return (''.join(letters), sector, checksum)
