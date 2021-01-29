import random

rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

user_play = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

if(user_play == 0):
        print(rock)
if (user_play == 1 ):
        print(paper)
if (user_play == 2 ):
        print(scissors)

print("Computer Chose: ")

random_number = random.randint(0, 2)

if (random_number == 0):
        print(rock)
if (random_number == 1):
        print(paper)
if (random_number == 2):
        print(scissors)


if user_play ==  random_number:
    print("You tied! Rematch needed!")

#user = rock
elif user_play == 0 and random_number == 1:
    print("You lost")
elif user_play == 0 and random_number == 2:
    print("You won")
#user = paper
elif user_play == 1 and random_number == 0:
    print("You won")
elif user_play == 1 and random_number == 2:
    print("You lost")
#user = scissors
elif user_play == 2 and random_number == 0:
    print("You lost")
elif user_play == 2 and random_number == 1:
    print("You won")
else:
    print("Game Over!")