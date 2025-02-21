import random

def statsBracket(): 
    sections = ["*SOUTH*", "*MIDWEST*", "*EAST*", "*WEST*"]
    sixteen = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]
    eight = [0, 0, 0, 0, 0, 0, 0, 0]
    four = [0, 0, 0, 0]
    two = [0, 0]
    final4 = [0, 0, 0, 0]
    championship = [0, 0]
    champ = [0]

    for i in range(4):
        print(sections[i])

        h1 = int(len(sixteen) / 2)
        print("|", end=" ")
        for f in range(h1):
            index = f * 2
            print(sixteen[index], sixteen[index + 1], end=" | ")
            winner = statistic(0, sixteen[index], sixteen[index + 1])
            eight[f] = winner
        print("")

        h2 = int(len(eight) / 2)
        print("|", end=" ")
        for s in range(h2):
            index = s * 2
            print(eight[index], eight[index + 1], end=" | ")
            winner = statistic(1, eight[index], eight[index + 1])
            four[s] = winner
        print("")

        h3 = int(len(four) / 2)
        print("|", end=" ")
        for x in range(h3):
            index = x * 2
            print(four[index], four[index + 1], end=" | ")
            winner = statistic(2, four[index], four[index + 1])
            two[x] = winner
        print("")

        h4 = int(len(two) / 2)
        print("|", end=" ")
        for r in range(h4):
            index = r * 2
            print(two[index], two[index + 1], end=" | ")
            winner = statistic(3, two[index], two[index + 1])
            final4[i] = winner
        print("")

    print("*Final Four*")
    h5 = int(len(final4) / 2)
    print("|", end=" ")
    for w in range(h5):
        index = w * 2
        print(final4[index], final4[index + 1], end=" | ")
        winner = statistic(4, final4[index], final4[index + 1])
        championship[w] = winner
    print("")

    print("*Championship*")
    h6 = int(len(championship) / 2)
    print("|", end=" ")
    for c in range(h6):
        index = c * 2
        print(championship[index], championship[index + 1], end=" | ")
        winner = statistic(5, championship[index], championship[index + 1])
        champ[0] = winner
    print("")
    print("*Winner*")
    print("|", champ[0], "|")




# r is the round, s1 and s2 are the seeds
def statistic(r, s1, s2):
    rd1 = [99, 93, 85, 79, 64, 61, 60, 48, 51, 39, 38, 35, 20, 14, 7, 1]
    rd2 = [75, 62, 52, 47, 33, 29, 18, 10, 6, 16, 17, 14, 4, 2, 2, 0]
    sweet16 = [58, 45, 25 ,18 ,7, 10, 7, 6, 3, 6, 6, 2, 0, 0, 1, 0]
    elite8 = [30, 21, 12, 9, 5, 2, 2, 4, 1, 1, 4, 0, 0, 0, 0, 0]
    final4 = [15, 9, 8, 2, 2, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0]
    champ = [16, 8, 7, 4, 0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]

    rounds = [rd1, rd2, sweet16, elite8, final4, champ]
    round = rounds[r]

    s1P = round[s1 - 1]
    s2P = round[s2 - 1]
    total = s1P + s2P

    rand = random.randint(1,total)

    if rand <= s1P:
        return s1
    else:
        return s2