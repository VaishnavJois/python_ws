'''
program to accept number from user and 
find the sum of digits of that number
ex : entered number = 12345
answer : 1+2+3+4+5 = -> = 1+5 = 6
'''

'''
number = input('Enter a number: ')

integer_form = int(number)

while integer_form//10>0:
    res=0
    for i in number:
        res += int(i)
    number = str(res)
    integer_form = res
print(f'The result is {integer_form}')
'''

TNUM = NUM = int(input('Enter a number: '))
while NUM>9:
    NUM = (NUM%10 + NUM//10)

print(f'The sum of digits is {NUM}')