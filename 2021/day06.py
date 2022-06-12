from collections import Counter

day = '06'

with open(f'2021\inputs\day{day}.txt', 'r') as f:
    lines = f.readlines()
    fish = [int(l) for l in lines[0].split(',')]
    f.close()

def update_fish(fish):
    for f in fish:
        if f == 0:
            fish.append(9)
    fish = [f - 1 if f > 0 else 6 for f in fish]
    return fish


def simulate_days(fish, days):
    for i in range(days):
        fish = update_fish(fish)
    return len(fish)

print(f'Part 1: {simulate_days(fish, 80)}')
## Saving states is too slow for part 2

fish_count = Counter(fish)
fish_array = [fish_count[i] for i in range(9)]

def update_fish_array(fish_array):
    head, *tail = fish_array
    tail.append(head) 
    tail[6] += head
    return tail

def simulate_days_array(fish_array, days):
    for i in range(days):
        fish_array = update_fish_array(fish_array)
    return sum(fish_array)

print(f'Part 1: {simulate_days_array(fish_array, 80)}')
print(f'Part 2: {simulate_days_array(fish_array, 256)}')