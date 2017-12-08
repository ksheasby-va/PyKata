from day_07.day_07_input import INPUT


def first_letters(line):
    return line.split()[0]


def last_letters(line):
    words = line.split()
    start_index = words.index('->')
    last_words = list()
    for i in range(start_index + 1, len(words)):
        if ',' in words[i]:
            last_words.append(words[i][:-1])
        else:
            last_words.append(words[i])
    return last_words

def find_bottom_program(input):
    not_tops = set()
    not_bottoms = set()
    for line in input.splitlines():
        if '->' in line:
            not_tops.add(first_letters(line))
            subtrees = last_letters(line)
            for i in subtrees:
                not_bottoms.add(i)

    for item in not_tops:
        if item not in not_bottoms:
            return item


if __name__ == "__main__":
    print find_bottom_program(INPUT)
