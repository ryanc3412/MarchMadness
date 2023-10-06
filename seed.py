import random

def seedBracket():
    sections = ["*SOUTH*", "*MIDWEST*", "*EAST*", "*WEST*"]
    sixteen = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]
    eight = [0, 0, 0, 0, 0, 0, 0, 0]
    four = [0, 0, 0, 0]
    two = [0, 0]
    final4 = [0, 0, 0, 0]
    championship = [0, 0]
    winner = [0]

    for i in range(4):
        print(sections[i])

        # uses the 16 to get the 8
        h1 = int(len(sixteen) / 2)
        print("|", end = " ")
        for f in range(h1):
            indexF = f * 2
            print(sixteen[indexF], sixteen[indexF + 1], end = " | ")
            winnerF = play(sixteen[indexF], sixteen[indexF + 1])
            eight[f] = winnerF
        print("")

        # uses the 8 to get the 4
        h2 = int(len(eight) / 2)
        print("|", end=" ")
        for s in range(h2):
            indexS = s * 2
            print(eight[indexS], eight[indexS + 1], end=" | ")
            winnerS = play(eight[indexS], eight[indexS + 1])
            four[s] = winnerS
        print("")

        # uses the 4 to get the 2
        h3 = int(len(four) / 2)
        print("|", end=" ")
        for x in range(h3):
            indexX = x * 2
            print(four[indexX], four[indexX + 1], end=" | ")
            winnerX = play(four[indexX], four[indexX + 1])
            two[x] = winnerX
        print("")

        # uses the 2 to get the final4 contestant
        h4 = int(len(two) / 2)
        print("|", end=" ")
        for r in range(h4):
            indexR = r * 2
            print(two[indexR], two[indexR + 1], end=" | ")
            winnerR = play(two[indexR], two[indexR + 1])
            final4[i] = winnerR
        print("\n")

    # uses the final4 to get the championship teams
    print("*Final Four*")
    h5 = int(len(final4) / 2)
    print("|", end=" ")
    for w in range(h5):
        indexW = w * 2
        print(final4[indexW], final4[indexW + 1], end=" | ")
        winnerW = play(final4[indexW], final4[indexW + 1])
        championship[w] = winnerW
    print("")
    print("|", championship[0], championship[1], "|")
    print("")

    # uses the championship teams to get the winner
    winner[0] = play(championship[0], championship[1])
    print("*Champion*")
    print("|", winner[0], "|")



def play(s1, s2):
    probTotal = s1 + s2
    randNum = random.randint(1, probTotal)

    if randNum <= s1:
        return s2
    else:
        return s1