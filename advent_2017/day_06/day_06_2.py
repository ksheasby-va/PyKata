def count_memory_reallocations(memory):
    seen_combinations = set()
    count = 0
    trigger_int = None
    while(1):
        max_value = max(memory)
        index = memory.index(max_value)
        memory[index] = 0
        index += 1
        for i in range(max_value):
            if index < len(memory):
                memory[index] += 1
            else:
                index = 0
                memory[index] += 1

            index += 1
        count += 1
        single_int = int(''.join(map(str, memory)))
        if single_int in seen_combinations and not trigger_int:
            trigger_int = single_int
            count = 0
        elif single_int == trigger_int:
            return count
        seen_combinations.add(single_int)


if __name__ == '__main__':
    print count_memory_reallocations([2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14])
