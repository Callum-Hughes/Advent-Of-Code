with open('2022\inputs\day01.txt', 'r') as f:
    lines = f.read()
    lines = lines.split('\n\n')
    lines = [l.split('\n') for l in lines]
    cals = [[int(x) for x in l] for l in lines]
    f.close()

def top_total_calories(x, n=1):
    return sum(sorted([sum(c) for c in x], reverse= True)[0:n])

if __name__ == '__main__':
    print(f'Part 1: {top_total_calories(cals, 1)}')
    print(f'Part 2: {top_total_calories(cals, 3)}')