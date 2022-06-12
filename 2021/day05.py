import itertools
from collections import Counter


day = '05'

with open(f'2021\inputs\day{day}.txt', 'r') as f:
    lines = f.readlines()
    lines = [l.replace('\n', '').replace(' -> ',',').split(',') for l in lines]
    f.close()

coords = []
for l in lines:
    x1,y1,x2,y2 = l
    coord = [(int(x1),int(y1)), (int(x2),int(y2))]
    coords.append(coord)

def create_line(coord, diag_lines=False):
    start = coord[0]
    start_x, start_y = start
    end = coord[1]
    end_x, end_y = end
    diff = (abs(end_x - start_x), abs(end_y - start_y))
    diff_x, diff_y = diff
    line = []

    if diff_x > 0 and diff_y == 0:
        x_0 = min(start_x, end_x)
        y_0 = start_y
        for x in range(0, diff_x + 1):
            pos = (x_0 + x, y_0)
            line.append(pos)
    
    if diff_y > 0 and diff_x == 0:
        x_0 = start_x
        y_0 = min(start_y, end_y)
        for y in range(0, diff_y + 1):
            pos = (x_0, y_0 + y)
            line.append(pos)

    if diff_x == diff_y and diag_lines:
        x_0 = start_x
        y_0 = start_y
        x_inc = 1 if start_x < end_x else -1
        y_inc = 1 if start_y < end_y else -1
        for i in range(0, diff_x + 1):
            pos = (x_0 + i * x_inc, y_0 + i * y_inc)
            line.append(pos)

    return line

def create_lines(coords, diag_lines=False):
    lines = []
    for coord in coords:
        lines.append(create_line(coord, diag_lines))
    return lines


def count_overlaps(coords, diag_lines=False):
    lines = create_lines(coords, diag_lines)
    line_coords = list(itertools.chain(*lines))
    overlapping_coords = Counter(line_coords)
    mask = [1 if x > 1 else 0 for x in overlapping_coords.values()]
    return sum(mask)


print(f'Part 1: {count_overlaps(coords, False)}')
print(f'Part 2: {count_overlaps(coords, True)}')