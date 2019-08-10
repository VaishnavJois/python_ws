'''
function that accepts 3 numbers as arguments
the function should find biggest of 3 numbers
'''

def bigest(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n3:
        return n2
    else:
        return n3

n1,n2,n3 = input('Enter 3 numbers separated by space:').split(' ')
print(bigest(int(n1),int(n2),int(n3)))