import random


def randBracket():
    sections = ["*SOUTH*", "*MIDWEST*", "*EAST*", "*WEST*"]
    sixteen = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]
    eight = [0, 0, 0, 0, 0, 0, 0, 0]
    four = [0, 0, 0, 0]
    two = [0, 0]
    winner = [0]

    final4 = [0, 0, 0, 0]

    for i in range(4):
        print(sections[i])
        print("First Round")
        print("|", end = " ")

        #print seeds for sixteen and then gets eight
        for j in range(len(sixteen)):
            print(sixteen[j], end = " ")
            if j % 2 == 1:
                print("|", end = " ")
        play(sixteen, eight, i)
        print()

        #print seeds for eight and then gets four
        print("Second Round")
        for e in range(len(eight)):
            if e % 2 == 0:
                print("|", end = " ")
            else:
                print("", end = " ")
            print(eight[e], end = " ")
            if len(str(eight[e])) == 1:
                print("", end = "")
        print("|", end = " ")
        play(eight, four, i)
        print()

        #print seeds for four and then gets two
        print("Sweet Sixteen")
        for f in range(len(four)):
            if f % 2 == 1:
                print("", end = " ")
            else:
                print("|", end = " ")
            print(four[f], end = " ")
        print("|", end = "")
        play(four, two, i)
        print()

        #print seeds for two and then gets final 4 contendant
        print("Elite Eight")
        for t in range(len(two)):
            if t == 0:
                print("|", two[t], end = " ")
            else:
                print(two[t], "|")
        play(two, final4, i)

        #prints final 4 contendant
        print("Final 4 Contendant")
        print("|", final4[i], "|")
        print("\n")


    play(final4, two, 0)
    print("Final 4")
    for s in range(len(final4)):
        if s == 0 or s == 2:
            print("|", final4[s], end = " ")
        else:
            print(final4[s], end = " ")
    print("|")
    print()

    play(two, winner, 0)
    print("\nChampionship")
    print("|", end = " ")
    for w in range(len(two)):
        print(two[w], end = " ")
    print("|")
    print()

    print("\nChampion")
    print("| ", winner[0], " |")


def play(now, next, round):
    num = int(len(now) / 2)
    pos = 0
    seed1 = 0
    seed2 = 1

    for i in range(num):
        rand = random.randint(1, 2)

        if rand == 1:
            if len(now) == 2:
                next[round] = now[seed1]
            else:
                next[pos] = now[seed1]
        else:
            if len(now) == 2:
                next[round] = now[seed2]
            else:
                next[pos] = now[seed2]

        seed1 += 2
        seed2 += 2
        pos += 1