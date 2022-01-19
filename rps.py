import random
guess = 0
print("WELCOME YOU GOT  5 GUESS :-)")
while True:
    options = ['rock', 'paper', 'scissors']
    inpt = input('Enter Rock/Paper/Scissors or q to quit: ').lower()
    if inpt == 'q':
        quit()
    rand = random.randrange(0,3)
    if options[rand] == inpt:
        print('you won!!')
        guess += 1
        print('Computer guess ',options[rand], 'your guess ',inpt)
        break
    else:
        print('You lost')
        guess += 1
        print('Computer guess: ',options[rand], 'your guess: ',inpt)
    
    if guess == 5:
        print('Your Out of guesses')
        quit()
    continue
    