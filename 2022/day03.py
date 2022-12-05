import string

with open('2022\inputs\day03.txt', 'r') as f:
    lines = f.read()
    bags = lines.split('\n')
    f.close()

print(bags)

letter_score = {letter:i+1 for i, letter in enumerate(list(string.ascii_letters))}

result = 0
for items in bags:
    n = len(items)
    d1 = int(n/2)
    d2 = n - d1
    items_1 = items[0:d1]
    items_2 = items[d2:n]
    print(items_1, items_2)
    shared_item = list(set(list(items_2)).intersection(set(list(items_1))))
    print(shared_item)
    shared_item_score = sum([letter_score[si] for si in shared_item])
    print(shared_item_score)
    result += shared_item_score

print(result)

counter = 0
current_group = []
result = 0
for items in bags:
    current_group.append(items)
    counter += 1
    print(counter)
    if counter == 3:
        bag_1 = set(list(current_group[0]))
        bag_2 = set(list(current_group[1]))
        bag_3 = set(list(current_group[2]))
        badge = list(bag_1.intersection(bag_2.intersection(bag_3)))
        print(badge)
        badge_score = sum([letter_score[b] for b in badge])
        result += badge_score
        counter = 0
        current_group = []

print(result)