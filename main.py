import statistical, seed, rand

def main():
    print("\nWELCOME TO THE MARCH MADNESS BRACKET CHALLENGE!!!")
    print("What kind of bracket would you like to create?")
    print("\nOptions include:\n1- statistical\n2- seed-based probability\n3- random")
    probe = input("\nEnter: ")

    if probe.lower() == "1" or probe.lower() == "statistical" or probe.lower() == "statistic" or probe.lower() == "stats":
        print("Statistical it is! Check your bracket below!\n")
        statistical.statsBracket()

    elif probe.lower() == "2" or probe.lower() == "seed-based" or probe.lower() == "seed" or probe.lower() == "probablility":
        print("Seed-based probability it is! Check your bracket below!\n")
        seed.seed_bracket()

    elif probe.lower() == "3" or probe.lower() == "random":
        print("Random it is! Check your bracket below!\n")
        rand.rand_bracket()

main()