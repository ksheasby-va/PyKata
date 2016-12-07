import string


def get_most_common_letter_in_column(input_string):
    column = ''.join(input_string.splitlines())
    count = 0
    most_common_letter = '.'
    for letter in string.lowercase:
        if column.count(letter) > count:
            most_common_letter = letter
            count = column.count(letter)

    return most_common_letter


def get_most_common_letters(input_string):
    message = []
    for index in xrange(len(input_string.splitlines()[0])):
        input_column = []
        for row in input_string.splitlines():
            input_column.append(row.strip()[index])

        message.append(get_most_common_letter_in_column(''.join(input_column)))

    return ''.join(message)
