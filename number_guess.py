from random import randint
easy_level=10
difficult_level=5

def check_answer(guess,answer,turns):
    if guess>answer:
        print("Too High")
        return turns-1
    elif guess<answer:
        print("Too Low")
        return turns-1
    else:
        print(f"You Win, The answer was {answer}")


def set_difficulty():
    level = input("Set the level of game , Type 'difficult' or 'easy' : ")
    if level=="easy":
        return easy_level
    else:
        return difficult_level

print("Welcome to the Number Guessing Game ! ")
print("Im thinking of number between 0 to 100 ")
answer = randint(0,101)
#print(f"The number is {answer}")
turns = set_difficulty()
guess = 0
while guess!=answer:
    print(f"Your have {turns} turns to guess te number ")
    guess = int(input("Guess a number : "))
    turns = check_answer(guess,answer,turns)
    if turns==0:
        print("You Lose")
        print(f"The answer was: {answer}")
        break

