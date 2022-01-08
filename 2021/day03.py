import sys
import itertools
import numpy as np

day = '03'

def split_int(word):
    return [int(char) for char in word]

with open(f'2021\inputs\day{day}.txt', 'r') as f:
    lines = f.readlines()
    bits = np.array([(split_int(line.strip())) for line in lines])
    f.close()

def calculate_binary(input, type):
    entries = input.shape[0]
    bit_counts = np.sum(input, axis = 0)

    if type == 'gamma':
        bit_count_mask = bit_counts >= entries / 2
    elif type == 'epsilon':
        bit_count_mask = bit_counts < entries / 2
    else:
        raise ValueError('Incorrect config')

    binary = ''.join((list(map(str, map(int, bit_count_mask)))))

    return binary

def calculate_rate(input, type):
    return int(calculate_binary(input, type), 2)

def calculate_rate_gamma(input):
    return calculate_rate(input, 'gamma')

def calculate_rate_epsilon(input):
    return calculate_rate(input, 'epsilon')

part1 = calculate_rate_gamma(bits) * calculate_rate_epsilon(bits)

print(f'Result to Part 1: {part1}')


def generate_ratings(bits, type):
    retained_bits_count = bits.shape[0]
    i = 0
    while retained_bits_count > 1:
        binary = calculate_binary(bits, type)
        bits = bits[np.ma.where(bits[:,i] == int(binary[i]))]
        i += 1
        retained_bits_count = bits.shape[0]
    return int(''.join(list(map(str, bits[0]))), 2)

def generate_rating_o2(input):
    return generate_ratings(input, 'gamma')

def generate_rating_co2(input):
    return generate_ratings(input, 'epsilon')

part2 = generate_rating_o2(bits) * generate_rating_co2(bits)

print(f'Result to Part 2: {part2}')