'''
count the number of prime digits
'''

p = ['2','3','5','7']
c = 0
n = list(input('Enter the number: '))
for i in n:
    if i in p:
        c += 1

print(c)