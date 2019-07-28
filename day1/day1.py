#single line comment
'''
documentation
format
or multi line comment
'''

#from time import sleep
#sleep(3)


name = input('Enter your name: ')
print(f'Welcome {name} to python world')
#.format
print('Welcome {} to python world(before 3.6)'.format(name))

age = int(input('Enter your age: '))
gender = input('Enter your gender: ')

print(f'Welcome {name}\nage:{age},',end='')
print(f"gender:{gender}")

input('This is just like getc() in C programming')


#if , elif, for, while

sal = float(input('Enter your salary: '))
if sal<0:
    sal = -sal
sal += (sal*.1)
print(f'salary is {sal}')


#even or odd

n = int(input('Enter a number:'))
if n%2==0:
    print(f'{n} is even')
else:
    print(f'{n} is odd')
