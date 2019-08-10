def searchLinear(ls, ele):
    index = 0
    for i in ls:
        if i == ele:
            return index
        index += 1
    return -1

ele = int(input('Enter the element to be searched: '))

res = searchLinear([1,2,3,4,2,3,6,7,8], ele)

print(f'Element {ele} found at location {res}')