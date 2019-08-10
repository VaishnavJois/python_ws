
def showInfo(dic):
    for k,v in dic.items():
        print(f'{k} : {v}')


d = {}

k , v = input('Enter reg.no : name')
d = {'NCET-001':'Rajesh','NCET-002':'Suresh'}
showInfo(d)