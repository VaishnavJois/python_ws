#5.Write a program to print the Fibonacci series up to the number 34. 
#(Example: 0, 1, 1, 2, 3, 5, 8, 13, … The Fibonacci Series always starts with 0 and 1,
#the numbers that follow are arrived at by adding the 2 previous numbers.)

n = int(input('Enter a number: '))

n1=0
n2=1
print('0, ',end='')

while n1<n:
    n1,n2 = n1+n2,n1
    print(n1,',',end='')
