import random
import time

def game():
    global answer
    num = random.randint(1, 3)

    print("Spinning...")
    time.sleep(4)

    if num == 1:
        print("Heads")
        answer = input("Do you want to play again: ")

    elif num == 2:
        print("Tails")
        answer = input("Do you want to play again: ").lower()
    
    else:
        pass

game()

if answer == "yes":
    game()
    
else:
    pass
