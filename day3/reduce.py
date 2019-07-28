from functools import reduce

ls = [1,2,3,4,5,6,7,8,9,10]

res = reduce(lambda a,b:a+b,list(filter(lambda x:x%2==0, list(map(lambda x:x**2,ls)))))

print(res)