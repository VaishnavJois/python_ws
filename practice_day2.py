name = "Python"
name_1 = name + "Programming"

newL = list()
newL = ['Alice','Will','Bob']

data1 = name_1[::-1]
data2 = name_1[3:-1]
print(data1)
print(data2)

data3 = "-".join(newL)

print(data3)

for index,name in enumerate(newL):
    print(f'{index} {name}')
    #print(name)
