#factorial
def fact(num):
    res=1
    if num==0 or num==1:
        res=1
    for i in range(1,num+1):
        res = res*i
    print(res)


# 1 + 1/2! + 1/3!

num = int(input('Enter a number: '))

res=1

for i in range(2,num+1):
    res = res + (1/fact(i))

print(res)
