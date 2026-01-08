import random

print("Lesgo Gambling")


ask = input("Lesgo gambling: [y] ")

if ask == "y":
    print("=" * 20)

    out = random.randint(1, 100)

    if out == 67:
        print("SIX SEVENNNNNNN")
    elif out == 16:
        print("This is magic number idk why")
    elif out == 100:
        print("YOU RICH")
    else:
        print("u Broke")

    print(f"The gambling Machine says your score is {out}")

else:
    print("No gambling today.")
