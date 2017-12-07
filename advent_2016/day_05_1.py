import hashlib


def get_hash_with_5_zeros(input_string, index=-1):
    output = ''
    while not output.startswith('00000'):
        index += 1
        output = hashlib.md5(input_string + str(index)).hexdigest()

    return output, index


def get_password_from_hash_results(input_string):
    password = ''
    index = -1
    for i in xrange(0, 8):
        hex_digest, index = get_hash_with_5_zeros(input_string, index)
        password += hex_digest[5]

    return password


if __name__ == '__main__':
    print get_password_from_hash_results('ugkcyxxp')
