import numpy as np

day = '07'

with open(f'2021\inputs\day{day}.txt', 'r') as f:
    lines = f.readlines()
    h_pos = [int(l) for l in lines[0].split(',')]
    f.close()

def calc_fuel_f(h_pos, func):
    fuel = sum(func(np.array(h_pos)))
    fuel_step = fuel
    i=1
    while fuel_step <= fuel:
        fuel = fuel_step
        diff = np.abs(np.array(h_pos)-i)
        fuel_step = sum(func(diff))
        i+=1
    return fuel

print(f'Part 1: {calc_fuel_f(h_pos, lambda x:x)}')
print(f'Part 2: {calc_fuel_f(h_pos, lambda x: 0.5*x*(x+1))}')