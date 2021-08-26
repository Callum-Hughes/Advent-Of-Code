import sys
import itertools
import numpy as np

with open('2020\inputs\day01.txt', 'r') as f:
    lines = f.readlines()
    lines = np.array([int(line.strip()) for line in lines])
    f.close()

print(np.where(lines == 2020))

def find_pair(x):
    x = sorted(x)
    for i1, n1 in enumerate(x):
        if n1 > 2020:
            continue
        for i2, n2 in enumerate(x[i1+1:]):
            if n2 > 2020:
                continue
            if n1 + n2 == 2020:
                return (n1, n2)

def find_trips(x):
    x = sorted(x)
    for i1, n1 in enumerate(x):
        if n1 > 2020:
            continue
        for i2, n2 in enumerate(x[i1+1:]):
            if n2 > 2020:
                continue
            for i3, n3 in enumerate(x[i2+1:]):
                if n3 > 2020:
                    continue
                if n1 + n2 + n3 == 2020:
                   return (n1, n2, n3)


pairs = find_pair(lines)
print(pairs[0] * pairs[1])

trips = find_trips(lines)
print(trips[0] * trips[1] * trips[2])