#calculate discount

amt = float(input('Enter bill amount:'))

if amt>=10000:
    dis = amt*0.2
else:
    dis = amt*0.05

net = amt-dis

print(f'Bill amount : {amt}\nDiscount : {dis}\nNet amount : {net}')



#calculate bill
'''
#minimum bill is 50
#per unit - >
#1-500 = 6rs/unit
#501-1000 = 8rs/unit
#>1000 12 rs/unit


min_bill = 50
rate=0
units = int(input('Enter the number of units:'))
if units in range(1,501):
    rate = 6
elif units in range(501,1001):
    rate = 8
elif units > 1000:
    rate = 12

final = units*rate
if final < 50:
    final = 50

print(f'Final amount : {final}')
'''
#another way to calculate bill
'''
if units>=1 and units<=500:
    rate = 6
elif units>=501 and units<=1000:
    rate = 8
elif units>1000:
    rate = 12

final = units*rate
print(f'Final amount : {final}')
'''

#calculate biggest of three
'''
n1 = int(input('Enter num1: '))
n2 = int(input('Enter num2: '))
n3 = int(input('Enter num3: '))

if n1>n2 and n1>n3:
    print('n1 is bigger')
elif n2>n3:
    print('n2 is bigger')
else:
    print('n3 is bigger')
'''

#multiple of a given number

n = int(input('Enter a number:'))

for i in range(1,11):
    print(f'{n}*{i} = {n*i}')






