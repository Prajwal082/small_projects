from tkinter.messagebox import YES


print('welcome to my computer quizz')
x= input('Ready to Play ').lower()
if x != 'yes':
    quit()
print('ok lets play')
count = 0

ans = input('what is the capital of karnataka ').lower()
if ans == 'bangalore':
    print('right ans')
    count +=1
else:
    print('wrong')

ans = input('what is the capital of kerala ').lower()
if ans == 'tiruvanathapuram':
    print('right ans')
    count +=1
else:
    print('wrong')

ans = input('what is the capital of tamil nadu ').lower()
if ans == 'chennai':
    print('right ans')
    count +=1
else:
    print('wrong')

print('total score',count)
print('you got yes' + str(((count/4)*100)) +'%' )
