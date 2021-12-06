## Common
def read_input():
    result = {}
    with open("input.txt") as reader:
        for line in reader:
            col_number = 0
            for bit in line.strip():
                if col_number not in result:
                    result[col_number] = list()
                result[col_number].append(int(bit))
                col_number += 1
        return result

def count(input):
    result = list()
    for i in input:
        result.append(1 if 1.0*sum(input[i]) / len(input[i]) >= 0.5 else 0)
    return result

def part_1(count):
    epsilon = int(''.join([str(b) for b in count]), base=2)
    gamma = int(''.join([str(~b & 1) for b in count]), base=2)
    return epsilon*gamma

print(part_1(count(read_input())))

## part 2
def filter(input, is_oxygen):
    for i in range(len(input)):
        if len(input[i]) == 1:
            break
        if is_oxygen:
            most_common_bit = 1 if 1.0 * sum(input[i]) / len(input[i]) >= 0.5 else 0
        else:
            most_common_bit = 0 if 1.0 * sum(input[i]) / len(input[i]) >= 0.5 else 1

        indexes = set()
        for j, bit in enumerate(input[i]):
            if bit == most_common_bit:
                indexes.add(j)

        result = {}
        for k in range(len(input)):
            for j, bit in enumerate(input[k]):
                if j in indexes:
                    if k not in result:
                        result[k] = list()
                    result[k].append(bit)

        input = result

    return input

def part2():
    oxyen = filter(read_input(), True)
    co2 = filter(read_input(), False)

    oxyen = int(''.join([str(b[0]) for _, b in oxyen.items()]), base=2)
    co2 = int(''.join([str(b[0]) for _, b in co2.items()]), base=2)
    return co2 * oxyen

print(part2())
