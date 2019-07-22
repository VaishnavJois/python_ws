import random as R
arl = list()
count=0
num = R.randint(1,6)
while True:
    unum = int(input('Enter a number: '))
    
    #arl.append(num)
    if unum == num:
        if count==0:
            print('You guessed it right at first attempt')
            break
        print(f'You got it right at {count+1} attempt')
        break
    elif num > unum:
        print('Try again! you guessed it less')
        count += 1
    elif num < unum:
        print('Try again! don\'t be too genorous')
        count += 1
    if count>3:
        print('Better luck next time')
        break
