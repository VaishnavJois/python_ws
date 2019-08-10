from inmemory import InMemoryImpl

while True:
    print('*'*100)
    print('1.Add 2.ViewAll 3.Update 4.Delete 5.Search 6.Exit')
    print('*'*100)
    c = int(input('Enter your choice: '))
    if c == 1:
        InMemoryImpl.addContact()
    elif c == 2:
        InMemoryImpl.viewContact()
    elif c == 3:
        InMemoryImpl.updateContact()
    elif c == 4:
        InMemoryImpl.deleteContact()
    elif c == 5:
        InMemoryImpl.search()
    else:
        break
        