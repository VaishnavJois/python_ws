'''
binary search with and without recursion
'''

ls = [1,2,3,4,0,9,6,7,8]
def binaryRecursion(ls,key):
    l = 0
    h = len(ls) - 1
    while l <= h:
        mid = (l+h)//2
        
        if ls[mid] == key:
            return mid
        elif ls[mid] < key:
            l = mid+1
        else:
            h = mid-1
    return -1



def bubbleSort(ls):
    for i in range(len(ls)-1,0,-1):
        for j in range(i):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] =  ls[j+1], ls[j]
bubbleSort(ls)

key = int(input('Enter the key to search: '))
f = binaryRecursion(ls,key)
print(f'key {key} found at position {f}')