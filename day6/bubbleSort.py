
ls = [1,2,3,4,0,9,6,7,8]
def bubbleSort(ls):
    for i in range(len(ls)-1,0,-1):
        for j in range(i):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] =  ls[j+1], ls[j]

bubbleSort(ls)
print(ls)
