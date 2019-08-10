
x = input('Enter the input: ')
l = ["Do you have a pen?", "I have an apple"]
x = ""
#while x != 'exit':
    #x = input('Enter the input: ')
    #l = list(x)
for i in l:
    if i.endswith('?'):
        print(f'{i} is Interrogative')
    else:
        print(f'{i} is Asserive')
