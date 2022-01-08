import sys
import itertools
import numpy as np

with open('2021\inputs\day01.txt', 'r') as f:
    lines = f.readlines()
    depths = np.array([int(line.strip()) for line in lines])
    f.close()

def calculate_inc_depths(depths):
    depths_diff = np.append(depths[1:], 0) - depths
    return (depths_diff > 0).sum()

part1 = calculate_inc_depths(depths)

print(f'Result to Part 1: {part1}')

depths_groups = np.array([depths, np.append(depths[1:], 0), np.append(depths[2:], [0, 0])])

depths_rolling_sum = np.sum(depths_groups, axis= 0)

part2 = calculate_inc_depths(depths_rolling_sum)

print(f'Result to Part 2: {part2}')