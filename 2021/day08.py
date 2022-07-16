day = '08'

with open(f'2021\inputs\day{day}.txt', 'r') as f:
    lines = f.read()
    lines = lines.split('\n')
    f.close()

inputs = []
outputs = []
for line in lines:
    input, output = line.split(' | ')
    inputs.append(input.split(' '))
    outputs.append(output.split(' '))


def sort_string(string):
    new_string = []
    for s in string:
        s = [''.join(sorted(x)) for x in s]
        new_string.append(s)
    return new_string

inputs = sort_string(inputs)
outputs = sort_string(outputs)

easy_digits = [1, 4, 7, 8]
easy_digit_lengths = [2, 4, 3, 7]

easy_digit_count = 0
for output in outputs:
    for digit in output:
        if len(digit) in easy_digit_lengths:
            easy_digit_count += 1

print(f'Part 1: {easy_digit_count}')

def str_intersection(a,b):
    return ''.join(set(a).intersection(set(b)))

def str_union(a,b):
    if a is None or b is None:
        return ''
    else:
        return ''.join(set(a).union(set(b)))

def decode_inputs(inputs):
    decoded_digits = [None for i in range(10)]
    remaining_inputs = inputs
    while None in decoded_digits:
        for input in remaining_inputs:
            if len(input) == 2:
                decoded_digit = 1
            elif len(input) == 4:
                decoded_digit = 4
            elif len(input) == 3:
                decoded_digit = 7
            elif len(input) == 7:
                decoded_digit = 8
            elif len(input) == 6:
                if len(str_union(input, decoded_digits[1])) == 7 and decoded_digits[1] is not None and decoded_digits[6] is None:
                    decoded_digit = 6
                elif len(str_union(input, decoded_digits[4])) == 6 and decoded_digits[6] != input and decoded_digits[6] is not None and decoded_digits[9] is None:
                    decoded_digit = 9
                elif decoded_digits[6] is not None and decoded_digits[9] is not None:
                    decoded_digit = 0
                else:
                    continue
            elif len(input) == 5:
                if len(str_union(input, decoded_digits[1])) == 5:
                    decoded_digit = 3
                elif len(str_union(input, decoded_digits[6])) == 6 and decoded_digits[6] != input and decoded_digits[6] is not None and decoded_digits[3] is not None and decoded_digits[5] is None:
                    decoded_digit = 5
                elif decoded_digits[3] is not None and decoded_digits[5] is not None:
                    decoded_digit = 2
                else:
                    continue
            else:
                continue
            decoded_digits[decoded_digit] = input
            remaining_inputs.remove(input)
    return {k:i for i, k in enumerate(decoded_digits)}

def apply_map(outputs, map):
    x = ''
    for output in outputs:
        x += str(map[output])
    return int(x)

vals = []
for input, output in zip(inputs, outputs):
    map = decode_inputs(input)
    val = apply_map(output, map)
    vals.append(val)

print(f'Part 2: {sum(vals)}')