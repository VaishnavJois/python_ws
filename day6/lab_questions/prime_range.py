'''
write a program to find prime numbers within given range:
lower bound(LB) and upper bound(UB)
'''

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num//2+1):
        if num%i == 0:
            return False
    return True


lower_bound = int(input('Enter the lower bound: '))
upper_bound = int(input('Enter the upper bound: '))

list_of_prime = []
for i in range(lower_bound,upper_bound):
    if is_prime(i):
        list_of_prime.append(i)

print(list_of_prime)
