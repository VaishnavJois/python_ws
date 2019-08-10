'''
accept 2 numbers , LB and UB
number divisible by 9 but not by 5
'''
LB = int(input('Enter upper bound: '))
UB = int(input('Enter upper bound: '))

for i in range(LB, UB):
    if i % 9 == 0 and i % 5 != 0:
        print(i)