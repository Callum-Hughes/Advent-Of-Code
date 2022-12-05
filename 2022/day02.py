with open('2022\inputs\day02.txt', 'r') as f:
    lines = f.read()
    lines = lines.split('\n')
    strat = [tuple(l.split(' ')) for l in lines]
    f.close()

scoring = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
    'Win': 6,
    'Draw': 3,
    'Lose': 0
}

def result(x, y):
    test = (y-x)%3
    if test == 1:
        return 'Win'
    elif test == 2:
        return 'Lose'
    else:
        return 'Draw'

def score_result(x, y):
    return scoring[result(x, y)] + y

def total_score(strat):
    score = 0
    for s in strat:
        opp = scoring[s[0]]
        my = scoring[s[1]]
        score += score_result(opp, my)
    return score

print(f'Part 1: {total_score(strat)}')



convert = {
    'X': 'Lose',
    'Y': 'Draw',
    'Z': 'Win'
}

def my(x, res):
    if res == 6:
        return x%3+1
    elif res == 0:
        return (x-2)%3+1
    else:
        return x

def score_my(x, res):
    return res + my(x, res)

def total_score2(strat):
    score = 0
    for s in strat:
        opp = scoring[s[0]]
        res = scoring[convert[s[1]]]
        score += score_my(opp, res)
    return score

print(f'Part 2: {total_score2(strat)}')