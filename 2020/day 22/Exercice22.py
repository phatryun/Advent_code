
with open("input.txt") as f:
    chunks = f.read().split("\n\n")

orig_p1 = list(map(int, chunks[0].strip().split("\n")[1:]))
orig_p2 = list(map(int, chunks[1].strip().split("\n")[1:]))

# print('player 1 :')
# print(deck_player_1.queue)
# print('player 2 :')
# print(deck_player_2.queue)

def copyQueue(q1, len_max=-1) :
    q2 = queue.Queue()
    list_q1 = list(q1.queue)
    if len_max == -1 :
        len_max = len(list_q1)

    for i in range(len_max) :
        q2.put(list_q1[i])

    return q2

def countScore(list_deck_player):
    res = 0
    for i in range(len(list_deck_player), 0, -1) :
        res += list_deck_player[len(list_deck_player) - i] * i

    return res

def playCombat(p1, p2):

    while len(p1) > 0 and len(p2) > 0  :
        carte_1 = p1.pop(0)
        carte_2 = p2.pop(0)

        if carte_1 < carte_2 :
            p2 += [carte_2,carte_1]
        else :
            p1 += [carte_1, carte_2]


    if len(p1) > 0:
        winner = p1
    else:
        winner = p2

    return winner

winner = playCombat(orig_p1.copy(), orig_p2.copy())
print(f'Part I : {sum(e*(len(winner)-i) for i, e in enumerate(winner))}')

def isInfinitGames(list_old_deck, deck_player_1, deck_player_2):

    for q1, q2 in list_old_deck :
        if q1 == deck_player_1 and q2 == deck_player_2 :
            return True

    return False

def playRecursiveCombat(p1, p2, game):
    seen1, seen2 = set(), set()
    nb_round = 1
    while len(p1) > 0 and len(p2) > 0 :

        if game == 1 :
            print(f'-- Round {nb_round} (Game {game}) --')
            # print(f'Player 1s deck: {p1}')
            # print(f'Player 2s deck: {p2}')

        s1 = ",".join([str(c) for c in p1])
        s2 = ",".join([str(c) for c in p2])
        if s1 in seen1 or s2 in seen2:
            return 1, p1

        seen1.add(s1)
        seen2.add(s2)

        carte_1 = p1.pop(0)
        carte_2 = p2.pop(0)

        # if game == 1  and nb_round == 49 :
        #     print(f'Player 1 plays: {carte_1}')
        #     print(f'Player 2 plays: {carte_2}')

        bool_size_1 = carte_1 <= len(p1)
        bool_size_2 = carte_2 <= len(p2)

        res = 1
        if bool_size_1 and bool_size_2 :
            #print('new game !!')
            res, _ = playRecursiveCombat(
                        p1.copy()[:carte_1],
                        p2.copy()[:carte_2],
                        game+1)
            # print(f'winner is : {res}')
        else :
            if carte_1 < carte_2 :
                    res = 2
            elif carte_1 > carte_2 :
                    res = 1

        if res == 2 :
            p2 += [carte_2, carte_1]
        elif res == 1 :
            p1 += [carte_1, carte_2]

        nb_round += 1

    if len(p1) == 0 :
        return 2, p2
    else :
        return 1, p1

_, winner_deck = playRecursiveCombat(orig_p1.copy(), orig_p2.copy(), 1)

print(f'Part II : {sum(e*(len(winner_deck)-i) for i, e in enumerate(winner_deck))}')
