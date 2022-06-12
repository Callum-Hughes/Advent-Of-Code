import numpy as np

day = '04'

with open(f'2021\inputs\day{day}.txt', 'r') as f:
    lines = f.readlines()
    f.close()

drawn_numbers = [int(n) for n in lines[0].split(',')]

bingo_cards = ''.join(lines[2:]).split('\n\n')

bingo_cards = [b.replace('\n', ' ').replace('  ', ' ').split(' ') for b in bingo_cards]

bingo_cards_int = []
for bingo_card in bingo_cards:
    bingo_card_int = [int(b) for b in bingo_card if b != '']
    bingo_cards_int.append(bingo_card_int)


bingo_cards_len = [len(b) for b in bingo_cards_int]

bingo_cards_array = [np.reshape(np.array(b), (5,5)) for b in bingo_cards_int]

bingo_cards_dim = [b.shape for b in bingo_cards_array]

marked_cards_array = [np.zeros((5,5)) for b in bingo_cards_dim]

def mark_bingo_card(card, marked_card, number):
    return np.where(card == number, 1, marked_card)

def check_marked_card(marked_card):
    max_row_sum = max(np.sum(marked_card, axis=0))
    max_col_sum = max(np.sum(marked_card, axis=1))

    return max_row_sum == 5 or max_col_sum == 5

def score_bingo_card(bingo_card, marked_card, n):
    return np.sum(bingo_card * (1-marked_card)) * n

def play_bingo(bingo_cards_array, marked_cards_array, drawn_numbers):
    won = False
    while not won:
        for n in drawn_numbers:
            for i, (b, m) in enumerate(zip(bingo_cards_array, marked_cards_array)):
                m = mark_bingo_card(b, m, n)
                marked_cards_array[i] = m
                won = check_marked_card(marked_cards_array[i])
                if won:
                    output = i, n, score_bingo_card(b,m,n)
                    break
            if won:
                break
    return output

print(f'Part 1: {play_bingo(bingo_cards_array, marked_cards_array, drawn_numbers)[2]}')

# Part 2 - Not a nice soln
cards_remaining = len(bingo_cards_array)
while cards_remaining > 1:
    result = play_bingo(bingo_cards_array, marked_cards_array, drawn_numbers)
    winning_card = result[0]
    bingo_cards_array.pop(winning_card)
    marked_cards_array.pop(winning_card)
    cards_remaining = len(bingo_cards_array)

print(f'Part 2: {play_bingo(bingo_cards_array, marked_cards_array, drawn_numbers)[2]}')
