import re

with open('2022\inputs\day05.txt', 'r') as f:
    lines = f.readlines()
    f.close()

stacks = {}
orders = []
for line in lines:
    line = re.sub('^    ','[x] ', line)
    line = re.sub('    $',' [x]', line)
    line = re.sub('\]     ', '] [x] ', line)
    line = re.sub('\]     \[', '] [x] [', line)
    boxes_in_row = re.findall('\[.\]', line)
    if boxes_in_row != []:
        for i, b in enumerate(boxes_in_row):
            key = i+1
            if b != '[x]':
                if key in stacks:
                    stacks[key] = stacks[key] + b[1]
                else:
                    stacks[key] = b[1]
    if re.match(' 1   2   3', line) is not None:
        continue
    order = tuple(re.findall('\d+', line))
    if order != ():
        orders.append(order)

for order in orders:
    n = int(order[0])
    frm = int(order[1])
    to = int(order[2])
    stack_frm = stacks[frm]
    stack_to = stacks[to]
    stacks[to] = stack_frm[0:n][::-1] + stack_to
    stacks[frm] = stack_frm[n:]

result = ''
for i in range(len(stacks)):
    result += stacks[i+1][0]

print(result)

import re

with open('2022\inputs\day05.txt', 'r') as f:
    lines = f.readlines()
    f.close()

stacks = {}
orders = []
i = 0
for line in lines:
    line = re.sub('^    ','[x] ', line)
    line = re.sub('    $',' [x]', line)
    line = re.sub('\]     ', '] [x] ', line)
    line = re.sub('\]     \[', '] [x] [', line)
    line = re.sub('\]     \[', '] [x] [', line)
    if i == 0:
        print(line)
    i+=1
    boxes_in_row = re.findall('\[.\]', line)
    if boxes_in_row != []:
        print(boxes_in_row)
        for i, b in enumerate(boxes_in_row):
            key = i+1
            if b != '[x]':
                if key in stacks:
                    stacks[key] = stacks[key] + b[1]
                else:
                    stacks[key] = b[1]
    if re.match(' 1   2   3', line) is not None:
        continue
    order = tuple(re.findall('\d+', line))
    if order != ():
        orders.append(order)

print(stacks)

for order in orders:
    n = int(order[0])
    frm = int(order[1])
    to = int(order[2])
    stack_frm = stacks[frm]
    stack_to = stacks[to]
    stacks[to] = stack_frm[0:n] + stack_to
    stacks[frm] = stack_frm[n:]

result = ''
for i in range(len(stacks)):
    result += stacks[i+1][0]

print(result)