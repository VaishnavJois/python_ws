#list compreshension
num = [j for j in range(100,500) if j%7 ==0 ]

print(f'\nNumbers between 100 & 500 , divisible by 7 : {num}')

################################################
nums = [1,2,3,4,5,6,7,8,9]

cube = [i**3 for i in nums]
print(f'\ncube of {nums} : {cube}')

#to single list

n3 = [[1,2,3], [4,5,6], [7,8,9]]

siList = [j for i in n3 for j in i]

print(f'\nlist of list into single list : {siList}')
