'''
accept a five digit number and increment each digit by 1
digit 9 gets incremented to 0
'''

#this program is to avoid maths
n = input('Enter a number: ')
n_list = list(n)
res_list = []
a = ''
for i in n_list:
    if int(i)!=9:
        res_list.append(str(int(i)+1))
    else:
        res_list.append('0')
print(a.join((res_list)))