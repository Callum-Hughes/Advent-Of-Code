import sys
import itertools
import numpy as np

day = '02'

with open(f'2021\inputs\day{day}.txt', 'r') as f:
    lines = f.readlines()
    commands = np.array([line.strip() for line in lines])
    f.close()

directions = {
    'forward': np.array([1, 0]),
    'up': np.array([0, -1]),
    'down': np.array([0, 1])
}

command_directions = np.array([directions[command.split(' ')[0]] for command in commands])
command_values = np.array([int(command.split(' ')[1]) for command in commands]).reshape((len(commands), 1))

commands_yz = command_directions * command_values

position = np.sum(commands_yz, axis = 0)

part1 = np.prod(position)

print(f'Result to Part 1: {part1}')

aim = (np.cumsum(commands_yz, axis = 0))[:, 1]

command_directions_aim = np.array([[command_directions[i, 0], aim[i]] for i in range(len(aim))])

commands_aim = command_directions_aim * command_values

moving_commands = commands_aim[np.ma.where(commands_aim[:, 0] != 0)]

position_aim = np.sum(moving_commands, axis = 0)

part2 = np.prod(position_aim)

print(f'Result to Part 2: {part2}')