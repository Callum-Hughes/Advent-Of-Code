import numpy as np

day = '09'

with open(f'2021\inputs\day{day}.txt', 'r') as f:
    lines = f.read()
    lines = lines.split('\n')
    lines = [list(line) for line in lines]
    f.close()

array = np.array(lines).reshape(len(lines), len(lines[0])).astype(int)

X, Y = array.shape

risk_points = []
for x in range(X):
    for y in range(Y):
        x_min = max(0, x-1)
        x_max = min(x+2, X)
        y_min = max(0, y-1)
        y_max = min(y+2, Y)
        window = array[x_min:x_max, y_min:y_max]
        window = np.array(window).astype(int)
        low_point = np.amin(window)
        middle_point = array[x,y]
        if int(low_point) == int(middle_point):
            risk_points.append(low_point+1)

print('Day 1:')
print(sum(risk_points))

array_basin = np.zeros(array.shape)
basin_counter = 1
for x in range(X):
    for y in range(Y):
        if array[x, y] == 9:
            array_basin[x, y] = -1
            continue
        if x == 0 and y == 0:
            array_basin[x, y] = basin_counter
            continue
        if x == 0:
            if array_basin[x, y-1] == -1:
                basin_counter += 1
                array_basin[x, y] = basin_counter
            else:
                array_basin[x, y] = array_basin[x, y-1]
            continue
        if y == 0:
            if array_basin[x-1, y] == -1:
                basin_counter += 1
                array_basin[x, y] = basin_counter
            else:
                array_basin[x, y] = array_basin[x-1, y]
            continue

        if array_basin[x, y-1] == -1 and array_basin[x-1, y] == -1:
            basin_counter += 1
            array_basin[x, y] = basin_counter
        if array_basin[x, y-1] != -1 and array_basin[x-1, y] == -1:
            basin_counter += 1
            array_basin[x, y] = array_basin[x, y-1]
        if array_basin[x-1, y] != -1 and array_basin[x, y-1] == -1:
            basin_counter += 1
            array_basin[x, y] = array_basin[x-1, y]
        if (array_basin[x, y-1] != -1) and (array_basin[x-1, y] != -1):
            array_basin[x, y] = array_basin[x, y-1]
            if array_basin[x, y-1] != array_basin[x-1, y]:
                array_basin[array_basin == array_basin[x-1, y]] = array_basin[x, y-1] 


basins = []
for n in np.unique(array_basin.astype(int))[1:]:
    basins.append(np.count_nonzero(array_basin[array_basin == n]))

print('Day 2:')
print(np.prod(sorted(basins, reverse= True)[0:3]))
