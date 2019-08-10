'''
accept a string from user and remove vowels in that string
print the remaining string
'''
user_inp = input('Enter a string: ')
res = []
t = ''
q=''
for i in user_inp:
    if i not in ['a','e','i','o','u']:
        q += i
        #res.append(i)
print(q)
#print(t.join(res))