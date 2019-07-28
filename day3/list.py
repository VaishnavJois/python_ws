import random as R

#list that contains names that starts with 'A' and endswith 'H'
data = "Ashith,Ankith,Mahesh,Suresh,Asha,Laxman"
s1 = data.upper()
print(s1)
ls = []
ls = s1.split(',')
print(ls)
new = []
for i in ls:
    if i.startswith('A') and i.endswith('H'):
        new.append(i)
        print(i)
new.sort()
print(f'sorted list : {new}')

#################################################################################
#unique names
C =  [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
F = [ "PKM", "ALN","RMZ","CS", "MCS"]
B = [ "PKM", "ALN", "NV", "KM","RMV"]

newL = []
newL.extend(C)
newL.extend(F)
newL.extend(B)
print(f'newL after combining all the list : {newL}')

new2 = []
for name in newL:
    if name not in new2:
        new2.append(name)

print(f'new2 contains elements of newL just once : {new2}')


#################################################################################
#append and extend
scores = [[1,2,3,4],[4,5,6,7],[6,7,8,9]]

newL = [10,20,30]
new2 = [100]

newL.append(scores)
print(f'\nnewL after appending scores : {newL}')

scores.append(newL)
print('scores after appending newL',scores)

new2.extend(scores)
print('new2 after extending scores',new2)

#################################################################################

res_score = [[1,2,3],[4,5,6],[7,8,9]]
res = 0
for a in res_score:
    for s in a:
        res += s
print(f'\nsum of elements of list of list : {res}')

#################################################################################
n = [1,2,3,4,5,6,7,8,9]
r = []
for i in n:
    r.append(i*i)
print(f'\nSquares of elements of the list : {r}')

########################################################################################
#first 20 random number in 1,50
#find max, min, put it in a list
num = []

for i in range(20):
    num.append(R.randint(1,50))

print(f'\n20 random numbers from 1 to 50 : {num}')

res = [max(num),min(num),sum(num)]
print(f'******max min sum = {res}')


########################################################################################
#generate first 100 random in (1,1000)
#get the number which is divisible by 3,6, but not 9
num = []
for i in range(100):
    num.append(R.randint(1,1000))
#print(len(num)) #to check the number of elements is actually hundred
print('\n****first hundred random number list : ')
print(num)

newL = []
for i in num:
    if i%3==0 and i%6==0 and i%9!=0:
        newL.append(i)
print('****Number which is divisible by 3,6, but not 9 : ')
print(newL)

########################################################################################
#map, add two consecutive elements in the list

l1 = [1,2,3,4]
l2 = [4,5,6,7]
print(f'\n****Original list : \n{l1}\n{l2}')
new = []
for i in range(len(l1)):
    new.append(l1[i]+l2[i])
print('****adding corresponding elements of 2 lists using append() :')
print(new)

res = list(map(lambda a,b : a+b, l1,l2))
print('****adding corresponding elements of 2 lists using map :')
print(res)

#######################################################################################
#add,delete, search, display, exit
#list operation as menu driven
lst =[]
def add(eke):
    lst.append(eke)
def delet():
    return lst.pop()
    
def search(s):
    if s in lst:
        print('Key found')

def display():
    if len(lst)==0:
        print('*****List empty*****')
    else:
        print('***List elements are: ***')
        for i in lst:
            print(i,end=' ')

c=0
while True:
    print('\n\n1.Add')
    print('2.Delete')
    print('3.Display')
    print('4.Search')
    print('5.Exit')

    c = int(input('Enter ur choice: '))
    if c == 1:
        ele = int(input('Enter element: '))
        add(ele)
    elif c == 2:
        if len(lst)!=0:
            d = delet()
            print(f'Deleted element is {d}')
        else:
            print('List empty')
    elif c == 3:
        display()
    elif c == 4:
        if len(lst) != 0:
            k = int(input('Enter element to be searched: '))
            search(k)
        else:
            print('****List empty****')
    else:
        break