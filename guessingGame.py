import random
number = (random.randrange(0,9,1))
chances = 0
chances_left = 5
while chances < 5:
    print("The number of chances left:", chances_left)
    guess = int(input("guess a number (between 1 to 9):"))
    chances = chances + 1
    chances_left = chances_left - 1
    if guess > 9:
        print(" Write a number under 9")
        chances = chances - 1
        chances_left = chances_left + 1
        breakpoint
    if guess < 0:
        print("Write a number above 0")
        chances = chances - 1
        chances_left = chances_left + 1
        breakpoint
    if not guess == number:
        print("It is wrong. Try again")
    if guess == number:
        print("Congrtulations You Won!!! The number is:", number)
        break
if not chances < 5:
        print("You Lose!!! This Number is:", number)