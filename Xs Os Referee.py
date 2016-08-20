def xo_referee(game_result):
    d = {'X':False,'O':False}
    for j in range(len(game_result)-2):
        for k in range(len(game_result)-2):
            for i in range(3):
                if game_result[i+j][0+k] == game_result[i+j][1+k] == game_result[i+j][2+k]:
                    d[game_result[i+j][0+k]] = True
                if game_result[0+j][i+k] == game_result[1+j][i+k] == game_result[2+j][i+k]:
                    d[game_result[0+j][i+k]] = True
            if game_result[0+j][0+k] == game_result[1+j][1+k] == game_result[2+j][2+k]:
                d[game_result[0+j][0+k]] = True
            if game_result[0+j][2+k] == game_result[1+j][1+k] == game_result[2+j][0+k]:
                d[game_result[0+j][2+k]] = True
    
    if d['X'] == d['O']:
        return 'D'
    elif d['X']:
        return 'X'
    else:
        return 'O'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert xo_referee([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert xo_referee([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert xo_referee([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert xo_referee([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

    # Rank 2
    assert xo_referee([
        ".OX",
        ".OX",
        ".OX"]) == "D", "Mexican Vertical Duel"
    assert xo_referee([
        '.XO',
        'XXX',
        'OOO']) == "D", "Mexican Horizontal Duel"

    # Rank 3
    assert xo_referee([
        'XOO.',
        '.X.O',
        'X.OO',
        'XXOX']) == "D", "4WD"
    assert xo_referee([
        'XOO.',
        '.X.O',
        'XXOO',
        'XXOX']) == "X", "4X4"
    print("Earn cool rewards by using the 'Check' button!")
