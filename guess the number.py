import random 
usr = int(input('enter a range of number  '))
rd =random.randrange(0,usr)
ipt = int(input('guess  a number '))
guess = 0

while True:
    ipt = int(input('guess  a number '))
    rd =random.randrange(0,usr)
    if ipt == rd:
        print('You have guessed it!!')
        guess +=1
        break
    if ipt <rd:
        print('enter a larger number next time')
        guess +=1
        continue
    elif ipt > rd:
        print('enter a smaller number ')
        guess +=1
        continue
    if guess == 5:
       quit()

print(guess)