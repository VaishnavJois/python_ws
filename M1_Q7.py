'''
7.Write a program to accept a number from the user and determine the sum of digits of that number.
Repeat the operation until the sum gets to be a single digit number.
'''

num = input('Enter a number: ')

new1 = int(num)

while new1//10>0:
    res=0
    for i in num:
        res+=int(i)
    num = str(res)
    new1 = res
print(f'The result is {new1}')
