from day_07.day_07_1 import first_letters, last_letters


def single_weight(line):
    weight = line.split()[1]
    return int(weight[1:-1])

def get_sub_weights(weights, program, children):
    all_weights = []
    if not children.get(program):
        all_weights.append(weights.get(program))
    else:
        for i in children.get(program):
            all_weights += get_sub_weights(weights, i, children)

    return all_weights

def find_balanced_weight(input):
    single_weights = {}
    children = {}
    child_weights = {}
    for line in input.splitlines():
        single_weights[first_letters(line)] = single_weight(line)
        if '->' in line:
            children[first_letters(line)] = last_letters(line)

    for program in single_weights.iterkeys():
        child_weights[program] = get_sub_weights(single_weights, program, children)

    return
