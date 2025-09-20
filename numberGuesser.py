import random

topOfrange = input("Type a number: ")

if topOfrange.isdigit():
    topOfrange = int(topOfrange)

    if topOfrange <= 0:
        print('Type number bigger than 0 next time')
        quit()

else:
    print('Type a number next time.')
    quit()

randomNumber = random.randint(0, topOfrange)
guesses = 0
while True:
    guesses += 1
    guess = input('Make a guess: ')
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Type a number next time.')
        continue

    if guess == randomNumber:
        print('You got it right!')
        break
    elif guess < randomNumber:
        print('Aim a little higher.')
    else:
        print('Go lower')

print(f'You had {guesses} guesses.')