import string


def decrypt_room_name(name_string, sector_id):
    lowercase_letters = string.ascii_lowercase
    decrypted_string = ''
    shift = sector_id % 26
    for letter in name_string:
        index = lowercase_letters.find(letter)
        if index + shift > 25:
            decrypted_string += lowercase_letters[index + shift - 26]
        else:
            decrypted_string += lowercase_letters[index + shift]

    return decrypted_string
