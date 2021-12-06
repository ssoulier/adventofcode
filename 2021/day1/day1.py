
def read_input():
    with open("input.txt") as reader:
        for line in reader:
            yield int(line.strip())

## Part 1
def compare_current_and_previous(lines):
    previous = None
    count = 0
    for current in lines:
        if previous:
            count += current > previous
        previous = current
    print(count)

compare_current_and_previous(read_input())

# Part 2
def rolling_sum(lines, n):
    queue = list()
    for line in lines:
        if len(queue) == n:
            yield sum(queue)
            queue = queue[1:n]

        queue.append(line)

compare_current_and_previous(rolling_sum(read_input(), 3))
