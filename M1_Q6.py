'''
6.Write a program to accept a number from the user;
then display the reverse of the entered number.
(Example: Entered number = 12345; Reversed number = 54321)

'''

def rever(num):
    rev = 0
    while num!=0:
        rev = rev*10 + num%10
        num //= 10
    return rev

num = int(input('Enter a number: '))

n = rever(num)
print(n)
