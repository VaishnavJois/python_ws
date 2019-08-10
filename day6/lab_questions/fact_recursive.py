'''
accept and print factorial of a number
'''

def fact(NUM):
    return 1 if NUM == 0 else NUM * fact(NUM-1)

NUM_BER = int(input('Enter the number'))
print(fact(NUM_BER))
