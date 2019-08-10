p = {}
#k , v = input('Enter reg.no : name')
#p = {'NCET-001':'Rajesh','NCET-002':'Suresh'}
while True:
    print('1.Add 2.Display 3.EXIT')
    c = int(input('Enter your choice:'))
    if c==1:
        p_id = int(input('Enter product id: '))
        value = input('Enter name: ')
        p[p_id] = value
    elif c==2:
        print(f'{p_id} : {p[p_id]}')
    elif c==3:
        for i in p:
            pass
    else:
        break
