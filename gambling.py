import random
import time

print("Lesgo Gambling")

time.sleep(2)

ask = input("Lesgo gambling: [y]")

out = random.randint(1,100)

if( ask == "y"):
    print("="*20)
    print(f"The gambling Machine says your score is {out}")

elif out == 67:
    print('SIX SEVENNNNNNN')
elif out == 16:
    print("This is magic number idk why")
    
elif out == 100:
    print("YOU RICH")
    
else:
    print("u Broke")