'''
9.Write a program to accept a five-digit number, increment each digit by 1 and then display the new number formed.
Note that digit 9 gets incremented to 0.
'''
n = input('Enter a number: ')
lis = list()
newL = list()

for i in n:
    lis.append(i)
c=0
for i in lis:
    if i!='9':
        newL.append(int(i)+1)
    else:
        newL.append('0')
    c+=1

s=""
for i in newL:
    s=s + str(i)
print(s)
