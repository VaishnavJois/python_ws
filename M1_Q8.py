'''
8.Write a program to accept 2 numbers “m” and “n” from the user;
determine the value of m^n without using predefined functions.
'''

m = int(input('enter m'))
n = int(input('enter n'))

res=1
for i in range(n):
    res*=m
print(res)
