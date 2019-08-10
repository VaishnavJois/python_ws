'''
singular to plural
'''

l = ['Story','Emergency','yyyyyy']

for i in l:
    if i.endswith('y'):
        s = i[:-1]+'ies'
        print(s)
