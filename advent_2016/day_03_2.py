def split_string_by_columns(input_string):
    first_column = []
    second_column = []
    third_column = []
    for item in input_string.splitlines():
        item_list = item.split()
        first_column.append(item_list[0])
        second_column.append(item_list[1])
        third_column.append(item_list[2])

    string = build_string_from_list(first_column)
    string += build_string_from_list(second_column)
    string += build_string_from_list(third_column)

    return string


def build_string_from_list(column):
    i = 1
    string = ''
    for side in column:
        if (i % 3) == 0:
            i = 1
            string += side
            string += '\n'
        else:
            i += 1
            string += side + ' '

    return string

