def count_steps_to_reach_exit(instructions):
    number_instructions = [int(i) for i in instructions.splitlines()]
    exit_threshold = len(number_instructions)
    i = 0
    count = 0
    while i < exit_threshold:
        tmp = i
        i += number_instructions[i]
        number_instructions[tmp] += 1
        count += 1

    return count


if __name__ == '__main__':
    print count_steps_to_reach_exit("""0
0
1
2
0
1
0""")
