#4. Write a program to accept a number “n” from the user;
#then display the sum of the following series:
#1/2^3 + 1/3^3 + 1/4^3 + …… + 1/n^3

num = int(input('Enter a number: '))

res = 0

for i in range(2,num+1):
    res += (1/(i**3))
print(res)
