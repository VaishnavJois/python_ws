'''Program to check prime or not'''

def is_prime(num):
    if num < 2:
        return False
    for j in range(2,num//2+1):
        if num%j == 0:
            return False
    return True

num = int(input('Enter number of prime'))
i=2
c=0
while True:
    if is_prime(i):
        print(i)
        c+=1
    i+=1
    if c==num:
        break

