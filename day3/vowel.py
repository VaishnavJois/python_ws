#count vowels in name using filter
name = input('Enter your name: ')
ls = ['a','e','i','o','u']
print(len(list(filter(lambda x:x in ls,name))))
print(list(filter(lambda x:x in ls,name)))
