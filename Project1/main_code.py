import random
import time
roll = "y"
while roll == "y":
    number = random.randint(1,6)
    if number == 1:
        print(" - - -")
        time.sleep(1)
        print(" - x -")
        time.sleep(1)
        print(" - - -")
    elif number == 2:
        print(" x - -")
        time.sleep(1)
        print(" - - -")
        time.sleep(1)
        print(" - - x")
    elif number == 3:
        print(" x - -")
        time.sleep(1)
        print(" - x -")
        time.sleep(1)
        print(" - - x")
    elif number == 4:
        print(" x - x")
        time.sleep(1)
        print(" - - -")
        time.sleep(1)
        print(" x - x")
    elif number == 5:
        print(" x - x")
        time.sleep(1)
        print(" - x -")
        time.sleep(1)
        print(" x - x")
    elif number == 6:
        print(" x - x")
        time.sleep(1)
        print(" x - x")
        time.sleep(1)
        print(" x - x")
    roll = input("type y to continue and ny to stop: ")